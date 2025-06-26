


import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Missing GROQ_API_KEY in .env file")

# Initialize Groq client
client = Groq(api_key=api_key)



# Transcribe audio using Groq + Whisper
def transcribe_with_groq(audio_path: str) -> list:
    with open(audio_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file,
            response_format="verbose_json"
        )
    
    # Filter out unclear parts
    result = []
    for segment in response.segments:
        text = segment["text"]
        if not any(bad in text.lower() for bad in ["[inaudible]", "[noise]", "[humming]", "(?)"]):
            result.append({
                "start": segment["start"],
                "end": segment["end"],
                "text": text.strip()
            })
    return result

# Save transcription to JSON
def save_to_json(data: list, output_file="output.json"):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"transcription": data}, f, indent=2, ensure_ascii=False)

# Main logic
def main():
    audio_path = "C:\\Users\\Shifu05\\Downloads\\WhatsApp Ptt 2025-06-26 at 11.31.29 AM.wav"  # Replace with your file
    transcription = transcribe_with_groq(audio_path)
    save_to_json(transcription)
    print("✅ Transcription saved to 'output.json'")

if __name__ == "__main__":
    main()

