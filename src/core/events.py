from dataclasses import dataclass

@dataclass
class PlayNoteEvent:
    nota: str

@dataclass
class StopNoteEvent:
    nota: str

@dataclass
class SetVolumeEvent:
    volume: int  # 0 to 127

@dataclass
class SetInstrumentEvent:
    instrument_id: int  # 0 to 127

@dataclass
class PlaySequenceEvent:
    nodes: list
    bpm: int = 120
    velocity: int = 100

@dataclass
class StopSequenceEvent:
    pass

@dataclass
class UpdateStatusEvent:
    message: str

@dataclass
class ProcessTextEvent:
    text: str

@dataclass
class ExportMidiEvent:
    text: str
    filepath: str

@dataclass
class ErrorEvent:
    error_message: str
