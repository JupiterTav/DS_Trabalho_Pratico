import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import threading
import queue
from src.gui.app import App
from src.audio.engine import AudioEngine

def main():
    # Setup queues
    audio_queue = queue.Queue()
    gui_queue = queue.Queue()

    # Start audio worker thread
    audio_engine = AudioEngine(audio_queue, gui_queue)
    audio_thread = threading.Thread(target=audio_engine.run, daemon=True)
    audio_thread.start()

    # Start GUI
    app = App(audio_queue, gui_queue)
    app.mainloop()

if __name__ == "__main__":
    main()
