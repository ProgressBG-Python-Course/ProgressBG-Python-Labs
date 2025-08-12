# # Writing data into json
# data = {"name": "Ivan", "age": 34, "is_male": True, "other": [None, None]}

# # # save as json string
# # data_as_json = json.dumps(data)

# # print(data)
# # print(data_as_json)


# # save in json file
# with open("./data.json", "w") as f:
#     json.dump(data, f)


# Read (Parse) data from json:
# with open("./data.json", "r") as f:
#     data = json.load(f)
#     print(type(data))


# Examples:
# import json

# json_string = '[1,2,"Ada"]'
# data = json.loads(json_string)
# print(json_string)
# print(data)

import json
from json import JSONDecodeError


def get_transactions(file_path):
    with open(file_path, "r") as f:
        try:
            transaction = json.load(f)
            return transaction
        except JSONDecodeError as f:
            return []


def process_transation():
    return {"type": "withdraw", "amount": 300}


def save_transactions(file_path, transations):
    with open(file_path, "w") as f:
        json.dump(transations, f)


if __name__ == "__main__":
    transations = get_transactions("./data.json")
    print(transations)

    transation1 = process_transation()
    transations.append(transation1)

    save_transactions("./data.json", transations)
