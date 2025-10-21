# Jarvis-The-Virtual-Assistant
A simple Python-based AI voice assistant inspired by CodeWithHarry’s tutorial, customized to greet me personally and open my favorite songs and websites. This project helped me learn speech recognition, text-to-speech, and basic AI integration.

Features
1)Greets the user personally: “Hello Swastika”
2)Opens popular websites like Google, YouTube, Facebook, LinkedIn, and Spotify
3)Plays songs from a custom music library
4)Handles general questions using OpenAI GPT-3.5
5)Uses Google Text-to-Speech (gTTS) and Pygame for voice output

Installation:-
Clone this repository:
git clone <your-repo-link>
cd jarvis-ai


Install the required packages:

pip install -r requirements.txt


Requirements include:

1)speechrecognition
2)pyttsx3
3)gtts
4)pygame
5)requests
6)openai

Add your API keys:

newsapi key if using news features, i removed this.

OpenAI API key for AI responses


Run the program:

python jarvis.py


Usage

Run the script. Jarvis will say: “Initializing Jarvis…” then Say the wake word “Jarvis”



Give commands like:

“Open Google” or “Play Opalite” (or any song from your music library)


Ask general questions for AI responses

Notes

The assistant uses Google Speech Recognition for command input.
Offline speech recognition using pocketsphinx is possible but less accurate.

The project is mainly for learning purposes and experimenting with Python voice assistants.




