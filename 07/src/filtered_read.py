def _get_filtered_line(fileobj, words):
    line = fileobj.readline()
    if not line:
        return None

    is_matched = False
    for word_line in line.split():
        for word_filt in words:
            if word_line == word_filt:
                is_matched = True
                break
    if is_matched:
        return line[:-1]
    return -1


def filtered_read(file, words):
    if isinstance(file, str):
        with open(file, 'r') as file_obj:
            try:
                while True:
                    filtered_line = _get_filtered_line(file_obj, words)
                    if filtered_line is None:
                        break
                    if filtered_line != -1:
                        yield filtered_line
            except IOError as error:
                raise IOError from error
            finally:
                file_obj.close()
    else:
        while True:
            filtered_line = _get_filtered_line(file, words)
            if filtered_line is None:
                break
            if filtered_line != -1:
                yield filtered_line
