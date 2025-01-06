# client.py

import requests

# Define the FastAPI endpoint
url = "http://127.0.0.1:8007/ask-question/"

# Define the query payload
question_payload = {
    "question": "How loans are processed?"
}

# Send the POST request to the FastAPI server
response = requests.post(url, json=question_payload)

print()

# Check response status and print the answer
if response.status_code == 200:
    answer = response.json()
    print(f"Answer: {answer['answer']}")
else:
    print(f"Error: {response.status_code}")
