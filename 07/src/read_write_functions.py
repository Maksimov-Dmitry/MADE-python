def read_data(fileobj, reader):
    return reader(fileobj).read()


def dump_data(data, fileobj, writer):
    writer(fileobj).dump(data)
