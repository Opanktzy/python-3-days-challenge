import requests

payload = {
    "ID": 1, "Name": "Alice", "Email": "alice@example.com",
    "ID": 2, "Name": "Bob", "Email": "bob@example.com",
    "ID": 3, "Name": "Charlie", "Email": "charlie@example.com",
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
print("Response-Code:", response.status_code)
print("Response-Server:", response.json())

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print("Response-Code:", response.status_code)
print("Response-Server:", response.json())

data = response.json()
print("Data:", data)
