# Clear Humming Words

## Overview of What the Script Does:

- Loads your Groq API key from a .env file.
- Sends an audio file to the Whisper model to transcribe.
- Filters out unclear segments (like [humming], [noise]).
- Saves the cleaned result as a .json file.
  
  ## Full Breakdown of the Script
  
1. Import Dependencies
   
  - os: Lets you interact with your system, including environment variables.
  - json: Saves the final transcription into .json format.
  - groq: Used to access Groq's API.
  - dotenv: Loads the .env file to securely fetch your API key.

2. Load API Key

   - load_dotenv() tells Python to look for a .env file in the current directory.
   - os.getenv("GROQ_API_KEY"): Grabs the API key from .env.
   - If the key isn’t found, it raises an error so you won’t run the script without credentials.

   ### Make sure your .env file looks like this:
```
   GROQ_API_KEY=your_actual_api_key_here
```
3. Initialize the Groq Client
```
client = Groq(api_key=api_key)
```
- You create a client that knows your API key.
- This client will be used to make transcription requests.
  
4. Transcription Function
   
 -  Opens the audio file in binary (rb) mode.

 -  Sends it to client.audio.transcriptions.create using the whisper-large-v3 model.

 - response_format="verbose_json" ensures detailed results (with timestamps and segments).

5. Filter Out Unclear Segments
   
-  Goes through each transcribed segment.
- Skips anything unclear (e.g., [noise], [humming]).
- Stores only clear speech, along with timestamps (start, end).

6. Save the Clean Transcription
   
- Creates a JSON file (output.json) in your working directory.
- Stores all the cleaned transcription data.

### How to Run It Properly

* Prerequisites:
  
1.Python 3.8+
2. Install dependencies:
```
pip install groq python-dotenv
```
3. Create a .env file in the same folder:

```
GROQ_API_KEY=your_actual_key_here
```
Place your audio file (e.g. audio.wav) in a known folder.

### Run the script:

*In your terminal:
```
python your_script_name.py
```
*You should see:

```
vbnet

 Transcription saved to 'output.json'
```

### Extra Ideas
1. Want subtitles? You can convert the results to .srt.

2. Want speaker identification? You’d need diarization tools.

3. Want a web interface? Add Streamlit or Flask.

























