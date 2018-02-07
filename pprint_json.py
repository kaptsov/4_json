import json
import argparse


def load_data(filepath):
    with open(filepath) as json_file:
        filedata = json_file.read()
    return json.loads(filedata)


def pretty_print_json(json_data):
    print(
        json.dumps(
            json_data,
            sort_keys=True,
            indent=2,
            ensure_ascii=False
        )
    )


def get_commandline_arguments():
    parser = argparse.ArgumentParser(description='Get the link to json file.')
    parser.add_argument('filepath', type=str)
    return parser.parse_args()


if __name__ == '__main__':
    try:
        json_data = load_data(get_commandline_arguments().filepath)
        pretty_print_json(json_data)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print('Wrong file structure or file missing.')
