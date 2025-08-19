import json


def set_config_key(key, value):
    globals()[key] = value


with open("config.json") as json_config:
    for key, value in json.load(json_config).items():
        set_config_key(key, value)


print(database)


# config = {
#     "base_url": "https://example.com/api",
#     "timeout": 3,
# }


# def update_config(**kwargs):
#     for key, value in kwargs.items():
#         if key in {"api_key", "base_url", "timeout"}:
#             config[key] = value
#         else:
#             raise KeyError(key)


# update_config(api_key="111222333")
# # print(config)

# update_config(timeout=5)
# print(config)
