import unittest
import io
import json

from src.read_write_classes import (TxtReader, JsonReader, CSVReader,
                                    TxtWriter, JsonWriter, CSVWriter)
from src.read_write_functions import read_data, dump_data


class TestReadWriteFormats(unittest.TestCase):
    """
    This class tests filtered read
    """

    def test_txt_read_write(self):
        data_1 = ("Hello world!\n"
                  "I am\n"
                  "Dima\n"
                  "\n"
                  "Maksimov\n")
        data_2 = ["Hello world!", "", "This assignment is DONE!!!!"]

        with io.StringIO() as buf:
            dump_data(data_1, buf, TxtWriter)
            self.assertEqual(buf.getvalue(), data_1)

            buf.seek(0)
            expected_readed_data = [
                "Hello world!",
                "I am",
                "Dima",
                "",
                "Maksimov",
            ]
            self.assertListEqual(read_data(buf, TxtReader),
                                 expected_readed_data)

            buf.seek(0)
            data_2_copy = data_2.copy()
            dump_data(data_2, buf, TxtWriter)
            self.assertListEqual(data_2, data_2_copy)
            self.assertEqual(buf.getvalue(), '\n'.join(data_2))

            buf.seek(0)
            self.assertEqual(read_data(buf, TxtReader), data_2)
            self.assertListEqual(data_2, data_2_copy)
            self.assertEqual(buf.getvalue(), '\n'.join(data_2))

            buf.seek(0)
            dump_data(data_1, buf, TxtWriter)
            dump_data(data_2, buf, TxtWriter)
            self.assertEqual(buf.getvalue(), data_1 + '\n'.join(data_2))

            buf.seek(0)
            self.assertEqual(read_data(buf, TxtReader),
                             expected_readed_data + data_2)

    def test_json_read_write(self):
        data = {
            "name": "jane doe",
            "salary": 9000,
            "skills": [
                "Raspberry pi",
                "Machine Learning",
                "Web Development",
                ],
            "email": "JaneDoe@pynative.com",
            "projects": [
                "Python Data Mining",
                "Python Data Science",
                ]
            }

        with io.StringIO() as buf:
            data_copy = data.copy()
            dump_data(data, buf, JsonWriter)
            self.assertEqual(data, data_copy)
            self.assertEqual(buf.getvalue(), json.dumps(data))

            buf.seek(0)
            self.assertEqual(read_data(buf, JsonReader), data)
            self.assertEqual(data, data_copy)
            self.assertEqual(buf.getvalue(), json.dumps(data))

    def test_csv_read_write(self):
        data = [
            ['Username', ' Identifier', 'First name', 'Last name'],
            ['booker12', '9012', 'Rachel', 'Booker'],
            ['grey07', '2070', 'Laura', 'Grey'],
            ['johnson81', '4081', 'Craig', 'Johnson'],
        ]

        with io.StringIO() as buf:
            data_copy = data.copy()
            dump_data(data, buf, CSVWriter)
            self.assertEqual(data, data_copy)
            self.assertEqual(
                buf.getvalue(),
                '\n'.join([';'.join(line) for line in data])
                )

            buf.seek(0)
            self.assertEqual(read_data(buf, CSVReader), data)
            self.assertEqual(data, data_copy)
            self.assertEqual(
                buf.getvalue(),
                '\n'.join([';'.join(line) for line in data])
                )

            buf.write('\n')
            data_add = [['jenkins46', '9346', 'Mary', 'Jenkins'],
                        ['smith79', '5079', 'Jamie', 'Smith']]
            dump_data(data_add, buf, CSVWriter)
            data.extend(data_add)
            self.assertEqual(
                buf.getvalue(),
                '\n'.join([';'.join(line) for line in data])
                )

            buf.seek(0)
            self.assertEqual(read_data(buf, CSVReader), data)
