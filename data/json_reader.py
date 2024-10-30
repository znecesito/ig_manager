import json

def load_json(directory_path):

    # directory_path = input("Enter file path for %s: " % (input_file))

    with open(directory_path, 'r') as f:
        return json.load(f)
