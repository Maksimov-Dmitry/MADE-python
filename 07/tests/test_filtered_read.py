import unittest
from unittest.mock import MagicMock, patch

import io

from src.filtered_read import filtered_read


class TestReadFilteredFile(unittest.TestCase):
    """
    This class tests read,write functions/classes
    """

    def setUp(self):
        self.text = ("Hello world!\n"
                     "I am\n"
                     "Dima\n"
                     "\n"
                     "Maksim\n"
                     "Sorry, Maksimov\n"
                     "Call me Dima Maksimov\n")
        self.words = ["Dima", "Maksimov"]
        self.filtered_lines = [
            "Dima",
            "Sorry, Maksimov",
            "Call me Dima Maksimov"
        ]

    def test_filtered_read_fileobject(self):
        with io.StringIO() as buf:
            buf.write(self.text)
            buf.seek(0)
            for i, line in enumerate(filtered_read(buf, self.words)):
                self.assertEqual(line, self.filtered_lines[i])
            self.assertEqual(buf.getvalue(), self.text)
            self.assertEqual(self.words, ["Dima", "Maksimov"])

    @patch("src.filtered_read._get_filtered_line")
    @patch("builtins.open")
    def test_filtered_read_filename(self, m_open, m__get_filtered_line):
        m_file_obj = MagicMock()
        m_open.return_value.__enter__.return_value = m_file_obj
        file_name = 'file_name'
        m__get_filtered_line.side_effect = [
            -1,
            "Dima",
            -1,
            -1,
            "Sorry, Maksimov",
            "Call me Dima Maksimov",
            None,
        ]
        for i, line in enumerate(filtered_read(file_name, self.words)):
            self.assertEqual(line, self.filtered_lines[i])

    @patch("src.filtered_read._get_filtered_line")
    @patch("builtins.open")
    def test_filtered_read_filename_error(self, m_open, m__get_filtered_line):
        m_file_obj = MagicMock()
        m_open.return_value.__enter__.return_value = m_file_obj
        file_name = 'file_name'
        m__get_filtered_line.side_effect = [
            -1,
            "Dima",
            -1,
            -1,
            IOError,
            "Sorry, Maksimov",
            "Call me Dima Maksimov",
            None,
        ]
        with self.assertRaises(IOError):
            for i, line in enumerate(filtered_read(file_name, self.words)):
                self.assertEqual(line, self.filtered_lines[i])
