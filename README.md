# Speech-to-Text with OpenAI Whisper

A lightweight Python tool that converts spoken audio to text **100% offline** using OpenAI's Whisper model. Perfect for transcribing meetings withoout cloud dependencies.


##  Features
-  **No Internet Required** - Runs entirely locally
-  **100+ Languages** - Automatic language detection
-  **Background Noise Robust** - Works in imperfect audio conditions
-  **Simple API** - Just python lines of core code

##  Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/speech-to-text-whisper.git
   cd speech-to-text-whisper

```
```bash
 pip install -r requirements.txt
```
```bash
python whisper_stt.py
```

``` bash
speech-to-text-whisper/
├── README.md
├── requirements.txt
└── whisper_stt.py         # Main application code
```
How It Works
Records audio using sounddevice

Converts to 16kHz WAV format

Feeds audio to Whisper's transformer model

Returns punctuated text with language detection

**Expected Output**
'''bash
    Speak now... (Recording for 5 seconds)
Saved as recording.wav

--- Transcription ---
"Hello this is a test of the speech recognition system"
```
