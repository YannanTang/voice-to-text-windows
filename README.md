# 🎤 Voice-to-Text System for Windows

A fast, local voice-to-text system for Windows that works globally across all applications. Similar to ChatGPT's voice feature, but runs entirely on your Windows PC using OpenAI's Whisper model.

## ✨ Features

- **Global hotkey**: Works in any application (Notepad, Slack, Visual Studio Code, etc.)
- **Instant text**: Transcribed text appears immediately via clipboard paste
- **Local processing**: Uses Whisper model locally - no internet required
- **High accuracy**: Uses Whisper "small" model for fast, accurate transcription
- **Simple setup**: Just clone and run!

## 🚀 Quick Setup

### 1. Prerequisites

Before starting, ensure you have:
- **Windows 10 or 11**
- **Python 3.8+** installed ([Download from python.org](https://www.python.org/downloads/))
- **Git** installed ([Download from git-scm.com](https://git-scm.com/downloads))

### 2. Clone the Repository
```cmd
cd %USERPROFILE%\Documents\GitHub # C:\Users\tangy69\Documents\GitHub\voice-to-text-windows
git clone https://github.com/YayunLovesCoding/voice-to-text-windows.git
cd voice-to-text-windows
```

### 3. Install Dependencies
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install Python packages
pip install -r requirements.txt
```

### 4. Run the Application
```cmd
cd %USERPROFILE%\Documents\GitHub\voice-to-text-windows
venv\Scripts\activate
python voice_to_text.py
```

## 🎯 How to Use

1. **Start the app** - You'll see: `✅ Ready! Press Ctrl+Alt 🎤 to start/stop recording`
2. **Position your cursor** anywhere you want text to appear
3. **Press Ctrl+Alt** to start recording (you'll see `🔴 Recording started...`)
4. **Speak clearly** - say whatever you want transcribed
5. **Press Ctrl+Alt again** to stop and transcribe
6. **Text appears instantly** at your cursor position!

## 🔧 System Requirements

- **Windows 10 or 11**
- **Python 3.8+**
- **Microphone access** (built-in or external microphone)
- **At least 2GB RAM** (for Whisper model)

## 🔐 Required Permissions

When you first run the app, Windows may request permissions:

### 1. Microphone Access
- Windows may show a microphone permission dialog
- **Click "Allow"** to grant microphone access

### 2. Windows Defender / Antivirus
- Some antivirus software may flag the global hotkey functionality
- **Add the script to your antivirus whitelist** if needed
- The application only listens for hotkeys and types text - it's completely safe

### 3. UAC (User Account Control)
- The app doesn't require administrator privileges
- Run as a normal user for best compatibility

## 🎛️ Hotkey

- **Ctrl+Alt**: Start/stop recording
- Works globally in any Windows application
- No conflicts with common system shortcuts

## 📝 Example Usage

```cmd
# Start the app
cd %USERPROFILE%\Documents\GitHub\voice-to-text-windows
venv\Scripts\activate
python voice_to_text.py

# You'll see:
# 🚀 Voice-to-Text for Windows starting up...
# 📥 Loading Whisper model (small for better performance)...
# ✅ Whisper model loaded
# ✅ Ready! Press Ctrl+Alt 🎤 to start/stop recording
# 🎯 Listening for Ctrl+Alt 🎤 ... (Ctrl+C to quit)

# Now use Ctrl+Alt to record in any app!
```

## 🔧 Troubleshooting

### "No module named 'pyaudio'" or installation errors
- Install Microsoft Visual C++ 14.0 or greater
- Download from: [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
- Or try: `pip install pipwin` then `pipwin install pyaudio`

### "Stream closed" or audio errors
- Check microphone permissions in Windows Settings > Privacy > Microphone
- Try unplugging/replugging external microphones
- Restart the application
- Check if another application is using the microphone

### Text appears slowly or character-by-character
- This should not happen with the latest version
- The app now uses instant clipboard paste
- If issues persist, check your antivirus settings

### "Command not found: python"
- Make sure Python is installed and added to your PATH
- Try using `py` instead of `python`
- Restart your command prompt after installing Python

### Hotkey not working
- Check if another application is using Ctrl+Alt
- Try running as administrator (though not usually required)
- Restart the application
- Some games or full-screen applications may block global hotkeys

### Performance issues
- Close other applications that use the microphone
- Ensure you have sufficient RAM (2GB+ recommended)
- The first transcription may be slower as the model loads

## 🛠️ Technical Details

- **Speech Recognition**: OpenAI Whisper (small model)
- **Audio Processing**: PyAudio with 16kHz sampling
- **Global Hotkeys**: pynput library (Windows-compatible)
- **Text Insertion**: Clipboard paste via pyautogui (Ctrl+V)
- **Language**: English (optimized for speed)
- **Platform**: Windows 10/11 compatible

## 📁 File Structure

```
voice-to-text-windows/
├── voice_to_text.py           # Main application
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🚀 Advanced Usage

### Running at Startup
1. Create a batch file `start_voice_to_text.bat`:
```batch
@echo off
cd /d "%USERPROFILE%\Documents\GitHub\voice-to-text-windows"
call venv\Scripts\activate
python voice_to_text.py
```
2. Add this batch file to Windows Startup folder:
   - Press `Win+R`, type `shell:startup`, press Enter
   - Copy the batch file to this folder

### Custom Hotkeys
- Edit line 223 in `voice_to_text.py` to change the hotkey combination
- Current hotkey: `Ctrl+Shift+3`

## 🤝 Contributing

Feel free to submit issues and feature requests! This project is designed to be simple and fast for Windows users.

## 📄 License

MIT License - feel free to use and modify!

## 🔗 Related Projects

- [macOS Version](../voice-to-text/) - The original macOS implementation
- [OpenAI Whisper](https://github.com/openai/whisper) - The underlying speech recognition model