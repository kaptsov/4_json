import json
import argparse

def load_data(filepath):
    f = open(filepath, "r")
    filedata = f.read()
    f.close()
    return json.loads(filedata)

def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=2, ensure_ascii = False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the link to json file.')
    parser.add_argument('filepath', type=str)
    args = parser.parse_args()
    filepath = args.filepath
    data = load_data(filepath)
    pretty_print_json(data)


