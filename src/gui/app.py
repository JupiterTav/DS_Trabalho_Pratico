import customtkinter as ctk
import queue
import tkinter.filedialog as filedialog
from src.gui.tabs.tab_text import TabText
from src.gui.tabs.tab_piano import TabPiano
from src.core.io_manager import IOManager
from src.core.events import PlayNoteEvent, SetVolumeEvent, SetInstrumentEvent, PlaySequenceEvent
from src.parser.tokenizer import RegexTokenizer
from src.audio.midi_builder import MidiBuilder

class App(ctk.CTk):
    def __init__(self, audio_queue: queue.Queue, gui_queue: queue.Queue):
        super().__init__()
        self.audio_queue = audio_queue
        self.gui_queue = gui_queue
        self.is_recording = False
        
        self.title("Piano Virtual & Synth")
        self.geometry("900x700")
        self.resizable(False, False)
        ctk.set_appearance_mode("Dark")
        
        self.frm_transport = ctk.CTkFrame(self, height=50)
        self.frm_transport.pack(fill="x", padx=10, pady=10)
        
        self.btn_play = ctk.CTkButton(self.frm_transport, text="Play", width=60, command=self.on_play)
        self.btn_play.pack(side="left", padx=5)

        self.btn_pause = ctk.CTkButton(self.frm_transport, text="Pause", width=60, command=self.on_pause)
        self.btn_pause.pack(side="left", padx=5)

        self.btn_record = ctk.CTkButton(self.frm_transport, text="Record", width=60, command=self.on_record, fg_color="gray")
        self.btn_record.pack(side="left", padx=5)

        self.btn_open = ctk.CTkButton(self.frm_transport, text="Upload", width=70, command=self.on_open)
        self.btn_open.pack(side="left", padx=5)
        
        self.btn_save = ctk.CTkButton(self.frm_transport, text="Salvar", width=70, command=self.on_save)
        self.btn_save.pack(side="left", padx=5)
        
        self.btn_export = ctk.CTkButton(self.frm_transport, text="Exp .mid", width=70, command=self.on_export)
        self.btn_export.pack(side="left", padx=5)

        self.btn_settings = ctk.CTkButton(self.frm_transport, text="⚙️", width=40, fg_color="transparent", border_width=1, command=self.on_settings)
        self.btn_settings.pack(side="right", padx=5)

        self.btn_help = ctk.CTkButton(self.frm_transport, text="?", width=40, fg_color="transparent", border_width=1, command=self.on_help)
        self.btn_help.pack(side="right", padx=5)

        self.slider_vol = ctk.CTkSlider(self.frm_transport, width=80, command=self.on_volume_change)
        self.slider_vol.set(1.0)
        self.slider_vol.pack(side="right", padx=5)
        ctk.CTkLabel(self.frm_transport, text="Vol:").pack(side="right")
        
        self.lbl_status = ctk.CTkLabel(self.frm_transport, text="Status: Ready")
        self.lbl_status.pack(side="right", padx=10)
        
        self.tab_text = TabText(self, width=600, height=200)
        self.tab_text.pack(pady=10, padx=20, fill="both", expand=True)

        self.tab_piano = TabPiano(self, self.audio_queue, self.get_is_recording, self.tab_text.append_text, width=600, height=180)
        self.tab_piano.pack(pady=10, padx=20, fill="x")

        self.is_recording_state = False
        self.current_instrument = 0
        self.current_bpm = 120
        self.current_octave = 4
        
        self.bind("<Control-o>", lambda e: self.on_open())
        self.bind("<Control-s>", lambda e: self.on_save())
        self.bind("<Control-r>", lambda e: self.on_record())
        
        self.check_queue()
        
    def check_queue(self):
        try:
            while True:
                event = self.gui_queue.get_nowait()
        except queue.Empty:
            pass
        self.after(20, self.check_queue)
        
    def on_play(self):
        self.lbl_status.configure(text="Status: Playing...")
        text = self.tab_text.get_text()
        tokenizer = RegexTokenizer()
        nodes = tokenizer.parse(text)
        self.audio_queue.put(PlaySequenceEvent(nodes=nodes, bpm=getattr(self, 'current_bpm', 120)))

    def on_pause(self):
        self.lbl_status.configure(text="Status: Paused")
        from src.core.events import StopSequenceEvent
        self.audio_queue.put(StopSequenceEvent())

    def on_volume_change(self, value):
        vol = int(value * 127)
        self.audio_queue.put(SetVolumeEvent(volume=vol))

    def on_settings(self):
        modal = ctk.CTkToplevel(self)
        modal.title("Configurações")
        modal.geometry("400x350")
        modal.transient(self)
        modal.grab_set()
        
        ctk.CTkLabel(modal, text="BPM Padrão:").pack(pady=(10, 5))
        bpm_entry = ctk.CTkEntry(modal)
        bpm_entry.insert(0, str(getattr(self, 'current_bpm', 120)))
        bpm_entry.pack(pady=5)
        
        ctk.CTkLabel(modal, text="Oitava Inicial:").pack(pady=(10, 5))
        oct_entry = ctk.CTkEntry(modal)
        oct_entry.insert(0, str(getattr(self, 'current_octave', 4)))
        oct_entry.pack(pady=5)
        
        ctk.CTkLabel(modal, text="ID do Instrumento (0-127):").pack(pady=(10, 5))
        inst_entry = ctk.CTkEntry(modal)
        inst_entry.insert(0, str(getattr(self, 'current_instrument', 0)))
        inst_entry.pack(pady=5)
        
        def save_settings():
            try:
                bpm_val = bpm_entry.get().strip()
                if bpm_val:
                    bpm_int = int(bpm_val)
                    if bpm_int > 0:
                        self.current_bpm = bpm_int
                        
                oct_val = oct_entry.get().strip()
                if oct_val:
                    oct_int = int(oct_val)
                    if oct_int > 0:
                        self.current_octave = oct_int
                        self.tab_piano.set_octave(oct_int)
                        
                val = inst_entry.get().strip()
                if val:
                    inst_id = int(val)
                    if 0 <= inst_id <= 127:
                        self.current_instrument = inst_id
                        self.audio_queue.put(SetInstrumentEvent(instrument_id=inst_id))
            except ValueError:
                pass
            modal.destroy()
            
        ctk.CTkButton(modal, text="Salvar", command=save_settings).pack(pady=20)
        self.bind("<Escape>", lambda e: modal.destroy())

    def on_help(self):
        modal = ctk.CTkToplevel(self)
        modal.title("Ajuda - Lista de Comandos")
        modal.geometry("400x300")
        modal.transient(self)
        modal.grab_set()
        help_text = "Comandos Suportados:\n\n- Notas: A, B, C, D, E, F, G\n- Acidentes: # (Sustenido) ou b (Bemol)\n- Andamento: <BPM> (ex: <120>)\n\nAtalhos:\n- Ctrl+O: Abrir\n- Ctrl+S: Salvar\n- Ctrl+R: Gravar"
        ctk.CTkLabel(modal, text=help_text, justify="left").pack(padx=20, pady=20)
        ctk.CTkButton(modal, text="Fechar", command=modal.destroy).pack(pady=10)
        self.bind("<Escape>", lambda e: modal.destroy())
        
    def get_is_recording(self):
        return self.is_recording
        
    def on_record(self):
        self.is_recording = not self.is_recording
        if self.is_recording:
            self.btn_record.configure(fg_color="red")
            self.lbl_status.configure(text="Status: Recording")
        else:
            self.btn_record.configure(fg_color="gray")
            self.lbl_status.configure(text="Status: Ready")
            
    def on_open(self):
        text, _ = IOManager.load_text()
        if text is not None:
            self.tab_text.set_text(text)
            self.lbl_status.configure(text="Status: Loaded")
            
    def on_save(self):
        text = self.tab_text.get_text()
        IOManager.save_text(text)
        self.lbl_status.configure(text="Status: Saved")
        
    def on_export(self):
        path = IOManager.get_midi_save_path()
        if path:
            try:
                text = self.tab_text.get_text()
                tokenizer = RegexTokenizer()
                nodes = tokenizer.parse(text)
                MidiBuilder.build_midi(nodes, path)
                self.lbl_status.configure(text="Status: Exported MIDI")
            except Exception as e:
                self.lbl_status.configure(text="Status: Export Error")
