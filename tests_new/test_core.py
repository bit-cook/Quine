import unittest
import subprocess
import os

class TestQuine(unittest.TestCase):
    def test_classic_quine(self):
        result = subprocess.check_output(['python', 'classic/quine.py'], text=True)
        with open('classic/quine.py', 'r') as f:
            expected = f.read()
        # Normalize newlines
        self.assertEqual(result.replace('\r\n', '\n'), expected.replace('\r\n', '\n'))

    def test_short_quine(self):
        result = subprocess.check_output(['python', 'classic/quine_short.py'], text=True)
        with open('classic/quine_short.py', 'r') as f:
            expected = f.read()
        self.assertEqual(result.strip(), expected.strip())

if __name__ == '__main__':
    unittest.main()
