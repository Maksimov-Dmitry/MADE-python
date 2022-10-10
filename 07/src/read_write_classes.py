import json


class BaseReader:
    """
    This class reads file and return string
    """

    def __init__(self, fileobj):
        self._fileobj = fileobj

    def read(self):
        return self._fileobj.read()


class BaseWriter:
    """
    This class write string in file
    """

    def __init__(self, fileobj):
        self.fileobj = fileobj

    def dump(self, data):
        return self.fileobj.write(data)


class TxtReader(BaseReader):
    """
    This class reads file and return list
    """

    def read(self):
        data = super().read()
        return data.splitlines()


class TxtWriter(BaseWriter):
    """
    This class write string or list in file
    """

    def dump(self, data):
        if isinstance(data, list):
            data = '\n'.join(data)
        super().dump(data)


class JsonReader(BaseReader):
    """
    This class reads file and return dict
    """

    def read(self):
        data = super().read()
        return json.loads(data)


class JsonWriter(BaseWriter):
    """
    This class write dict in file
    """

    def dump(self, data):
        new_data = json.dumps(data)
        super().dump(new_data)


class CSVReader(BaseReader):
    """
    This class reads file and return list of lists
    """

    def read(self):
        data = super().read()
        data = [
            line.split(';')
            for line in data.splitlines()
        ]
        return data


class CSVWriter(BaseWriter):
    """
    This class write list of lists in file
    """

    def dump(self, data):
        lines = [';'.join(line) for line in data]
        new_data = '\n'.join(lines)
        super().dump(new_data)
