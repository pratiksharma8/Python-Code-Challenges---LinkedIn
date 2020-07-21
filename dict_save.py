import json


def save_dict(dict_to_save, file_path):
    with open(file_path, 'w') as file:
        json.dump(dict_to_save, file)


def load_dict(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


test_dict = {1: 'a', 2: 'b', 3: 'c'}
save_dict(test_dict, 'test_dict.json')
recovered = load_dict('test_dict.json')
print(recovered)
