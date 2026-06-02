import unittest
import os
from src.parser.tokenizer import RegexTokenizer
from src.audio.midi_builder import MidiBuilder
import mido

class TestMidiSync(unittest.TestCase):
    def test_midi_creation(self):
        tokenizer = RegexTokenizer()
        nodes = tokenizer.parse("<120> A B C")
        filepath = "test_output.mid"
        
        MidiBuilder.build_midi(nodes, filepath)
        
        self.assertTrue(os.path.exists(filepath))
        
        mid = mido.MidiFile(filepath)
        self.assertGreater(len(mid.tracks[0]), 0)
        
        os.remove(filepath)

if __name__ == '__main__':
    unittest.main()
