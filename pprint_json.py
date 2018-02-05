import json
import argparse


def load_data(filepath):
    with open(filepath) as json_file:
        filedata = json_file.read()
    return json.loads(filedata)


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True,
          indent=2, ensure_ascii=False))


def commandline_link_parser():
    parser = argparse.ArgumentParser(description='Get the link to json file.')
    parser.add_argument('filepath', type=str)
    return parser.parse_args().filepath


if __name__ == '__main__':
    json_data = load_data(commandline_link_parser())
    pretty_print_json(json_data)
