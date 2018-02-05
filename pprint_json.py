import json
import argparse

def load_data(filepath):
    json_file = open(filepath, "r")
    filedata = json_file.read()
    json_file.close()
    return json.loads(filedata)

def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=2, ensure_ascii = False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the link to json file.')
    parser.add_argument('filepath', type=str)
    args = parser.parse_args()
    filepath = args.filepath

    json_data = load_data(filepath)
    pretty_print_json(json_data)


