#!/usr/bin/env python3
"""
Voice-to-Text System for Windows - Simple Version
Using keyboard library for better Windows hotkey support.

Usage:
- Press Ctrl+Shift+3 to start recording
- Press Ctrl+Shift+3 again to stop and convert to text
- The text will be automatically typed at your cursor position
"""

import os
import time
import threading
import tempfile
import wave
import pyaudio
import whisper
import pyautogui
import pyperclip
import keyboard



class VoiceToTextSimple:
    def __init__(self):
        self.recording = False
        self.audio_frames = []
        self.audio_stream = None
        self.p = None
        self.model = None
        self.pasting = False
        self.last_toggle_time = 0
        
        # Audio settings
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000
        
        print("🚀 Voice-to-Text for Windows starting up...")
        self.setup_audio()
        self.load_whisper_model()
        print("✅ Ready! Press Ctrl+Shift+3 🎤 to start/stop recording")
    
    def setup_audio(self):
        """Initialize PyAudio"""
        self.p = pyaudio.PyAudio()
    
    def load_whisper_model(self):
        """Load Whisper model"""
        print("📥 Loading Whisper model (small for better performance)...")
        self.model = whisper.load_model("small")
        print("✅ Whisper model loaded")
    
    def toggle_recording(self):
        """Toggle recording state with debounce"""
        current_time = time.time()
        
        # Short debounce to prevent double-triggers from single keypress
        if current_time - self.last_toggle_time < 0.3:
            print("🔇 Ignoring rapid hotkey trigger")
            return
            
        self.last_toggle_time = current_time
        
        if self.pasting:
            print("🔇 Ignoring hotkey during text pasting")
            return
            
        if not self.recording:
            print("🎤 Starting recording...")
            self.start_recording()
        else:
            print("🛑 Stopping recording...")
            self.stop_recording()
    
    def start_recording(self):
        """Start audio recording"""
        if self.recording:
            return
            
        print("🔴 Recording started...")
        self.recording = True
        self.audio_frames = []
        
        try:
            self.audio_stream = self.p.open(
                format=self.format,
                channels=self.channels,
                rate=self.rate,
                input=True,
                frames_per_buffer=self.chunk,
                input_device_index=None
            )
            
            threading.Thread(target=self._record_audio, daemon=True).start()
            
        except Exception as e:
            print(f"❌ Failed to start recording: {e}")
            self.recording = False
    
    def _record_audio(self):
        """Record audio in background thread"""
        while self.recording and self.audio_stream:
            try:
                if self.audio_stream.is_active():
                    data = self.audio_stream.read(self.chunk, exception_on_overflow=False)
                    self.audio_frames.append(data)
                else:
                    break
            except Exception as e:
                if self.recording:
                    print(f"Recording error: {e}")
                break
    
    def stop_recording(self):
        """Stop recording and process speech-to-text"""
        if not self.recording:
            return
            
        print("⏹️  Recording stopped, processing...")
        self.recording = False
        
        time.sleep(0.1)
        
        if self.audio_stream:
            try:
                if self.audio_stream.is_active():
                    self.audio_stream.stop_stream()
                self.audio_stream.close()
            except Exception as e:
                print(f"Stream cleanup error: {e}")
            finally:
                self.audio_stream = None
        
        if not self.audio_frames:
            print("❌ No audio data recorded")
            return
        
        # Save audio to temporary file
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
            try:
                with wave.open(temp_file.name, 'wb') as wf:
                    wf.setnchannels(self.channels)
                    wf.setsampwidth(self.p.get_sample_size(self.format))
                    wf.setframerate(self.rate)
                    wf.writeframes(b''.join(self.audio_frames))
                
                self.process_speech_to_text(temp_file.name)
                
            except Exception as e:
                print(f"Error processing audio: {e}")
            finally:
                # Give time for file to be released, then clean up
                try:
                    time.sleep(0.2)
                    if os.path.exists(temp_file.name):
                        os.unlink(temp_file.name)
                except PermissionError:
                    # File still in use, will be cleaned up by OS later
                    pass
    
    def process_speech_to_text(self, audio_file):
        """Convert audio to text using Whisper"""
        try:
            print("🤖 Converting speech to text...")
            result = self.model.transcribe(
                audio_file,
                language="en",
                fp16=False,
                verbose=False
            )
            text = result["text"].strip()
            
            if text:
                print(f"📝 Transcribed: {text}")
                self.type_text(text)
            else:
                print("❌ No speech detected")
                
        except Exception as e:
            print(f"Speech-to-text error: {e}")
    
    def type_text(self, text):
        """Insert text at current cursor position"""
        self.pasting = True
        
        try:
            
            # Try direct typing first (most reliable)
            print(f"⌨️  Typing: {text}")
            pyautogui.typewrite(text, interval=0.001)  # Much faster typing
            print("✅ Text typed successfully")
            
        except Exception as e:
            print(f"Direct typing failed: {e}")
            
            # Fallback to clipboard method
            try:
                print("🔄 Trying clipboard method...")
                original_clipboard = pyperclip.paste()
                pyperclip.copy(text)
                time.sleep(0.3)
                pyautogui.hotkey('ctrl', 'v')
                print("✅ Text pasted via clipboard")
                time.sleep(0.3)
                pyperclip.copy(original_clipboard)
                
            except Exception as e2:
                print(f"Clipboard method also failed: {e2}")
                print(f"📝 Manual copy: {text}")
        
        finally:
            self.pasting = False
    
    def run(self):
        """Start the hotkey listener"""
        try:
            # Register hotkey combinations for both left and right side keys
            keyboard.add_hotkey('ctrl+shift+3', self.toggle_recording)
            keyboard.add_hotkey('ctrl+alt+shift+3', self.toggle_recording)
            print("🎯 Listening for Ctrl+Shift+3 🎤 ... (Ctrl+C to quit)")
            
            # Keep the program running
            keyboard.wait()
            
        except KeyboardInterrupt:
            print("\n👋 Shutting down...")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        if hasattr(self, 'p') and self.p:
            self.p.terminate()
        print("🧹 Cleanup complete")


if __name__ == "__main__":
    try:
        app = VoiceToTextSimple()
        app.run()
    except Exception as e:
        print(f"Error starting application: {e}")
        exit(1)