# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

response=requests.get("https://reqres.in/api/users?page=2")
print(response.json())
print(response.status_code)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
