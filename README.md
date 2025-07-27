# 🎤 Voice-to-Text System for Windows

Fast, local voice-to-text using OpenAI Whisper with global hotkey support.

## 🚀 Quick Start

### 1. Open Terminal
- Press `Win + R`, type `cmd`, press Enter

### 2. Navigate and Run
```cmd
cd C:\Users\tangy69\Documents\GitHub\voice-to-text-windows
venv\Scripts\activate
python voice_to_text.py
```

### 3. Use the App
- Press `Ctrl+Shift+3` to start recording
- Speak clearly
- Press `Ctrl+Shift+3` again to stop and transcribe
- Text appears at cursor position

### 4. Stop the App
- Press `Ctrl+C` in terminal

## 📋 Requirements
- Windows 10/11
- Python 3.8+
- Microphone access

## 🔧 Setup (One-time)
```cmd
cd C:\Users\tangy69\Documents\GitHub\voice-to-text-windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 💡 Notes
- Works in any application (Notepad, Word, browser, etc.)
- Compatible with PowerToys keyboard manager
- Keep terminal open while using
- First run downloads Whisper model (~74MB)