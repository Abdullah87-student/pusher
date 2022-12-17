import requests

name=input("What would you like your employee to be named ")
employee={"name":name}
headers={"Content type":"application/json"}

response=requests.post("https://reqres.in/api/users", json=employee, headers=headers)

print(response.content)
print(response.headers)
print(response.status_code)
