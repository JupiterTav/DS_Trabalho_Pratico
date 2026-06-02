import unittest
from src.parser.tokenizer import RegexTokenizer
from src.parser.ast_nodes import MusicNode

class TestParser(unittest.TestCase):
    def test_clean_dsl(self):
        tokenizer = RegexTokenizer()
        nodes = tokenizer.parse("A B C")
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].valor, 'A')
        self.assertEqual(nodes[1].valor, 'B')
        self.assertEqual(nodes[2].valor, 'C')

    def test_silencing_proxy_garbage(self):
        tokenizer = RegexTokenizer()
        nodes = tokenizer.parse("A @ X Y C#")
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].valor, 'A')
        self.assertEqual(nodes[1].valor, 'C#')

    def test_tempo_changes(self):
        tokenizer = RegexTokenizer()
        nodes = tokenizer.parse("<140> A <80> B")
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].tipo, 'tempo')
        self.assertEqual(nodes[0].valor, '140')
        self.assertEqual(nodes[1].tipo, 'nota')
        self.assertAlmostEqual(nodes[1].duration_ms, 60000/140, places=2)

if __name__ == '__main__':
    unittest.main()
