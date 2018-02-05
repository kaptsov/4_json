import json


def load_data(filepath):
    f = open(filepath, "r")
    filedata = f.read()
    f.close()
    return filedata

def pretty_print_json(data):
    print(json.dumps(json.loads(data), sort_keys=True, indent=2, ensure_ascii = False))


if __name__ == '__main__':
    data = load_data(input('Input a link: '))
    pretty_print_json(data)


