# ------------------------------- Serialization ------------------------------ #
# def serialize_ip_format(data):
#     # custom data serialization (NOT USED IN PRACTICE):
#     data_string = ""
#     for user in data:
#         data_string += f"{user['name']}-{user['age']}\n"

#     with open("data.txt", "w") as f:
#         f.write(data_string)


# data = [{"name": "Maria", "age": 23}, {"name": "Pesho", "age": 32}]
# serialize_ip_format(data)

# # ------------------------------ Deserialization ------------------------------ #
# def deserialize_ip_format(file_path):
#     data = []
#     with open(file_path) as f:
#         for line in f:
#             tmp = line.strip().split("-")
#             user = {"name": tmp[0], "age": tmp[1]}
#             data.append(user)
#     return data


# data = deserialize_ip_format("data.txt")
# for user in data:
#     print(user)


# ----------------------------------- JSON ----------------------------------- #
# import json
# from json.decoder import JSONDecodeError


# def serialize_to_json_string(data):
#     try:
#         data_string = json.dumps(data)
#         return data_string
#     except JSONDecodeError as e:
#         print("Invalid JSON", e)


# def serialize_to_json_file(data, file_path):
#     try:
#         with open(file_path, "w") as f:
#             json.dump(data, f)
#     except FileNotFoundError as e:
#         print("No such file", e)
#     except JSONDecodeError as e:
#         print("Invalid JSON", e)


# def deserialize_json_string(json_data):
#     return json.loads(json_data)


# def deserialize_json_file(file_path):
#     with open(file_path) as f:
#         return json.load(f)


# json_data = """
#     [
#         {"name": "Maria", "age": 23, "smoker":true},
#         {"name": "Pesho", "age": 32, "smoker":false}
#     ]
# """
# # data = deserialize_json_string(json_data)
# # data = deserialize_json_file("./data.json")
# # print(data)

# data = [{"name": "Maria", "age": 23}, {"name": "Pesho", "age": 32}]
# # print(serialize_to_json_string(data))
# serialize_to_json_file(data, "./data.json")

### List of objects
# import json


# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def __dict__(self):
#         return {"name": self.name, "age": self.age}

#     def __str__(self):
#         return "..."

# data = [Person("Maria", 23), Person("Pesho", 32)]
# data_converted = [p.__dict__() for p in data]
# json_string = json.dumps(data_converted)
# print(json_string)


# # ------------------------------------ CSV ----------------------------------- #
# import csv


# def serialize_to_csv(data, file_path):
#     with open(file_path, "w") as f:
#         writer = csv.DictWriter(f, fieldnames=["name", "age"])
#         writer.writeheader()
#         writer.writerows(data)


# data = [{"name": "Maria", "age": 23}, {"name": "Pesho", "age": 32}]
# serialize_to_csv(data, "./data.csv")
