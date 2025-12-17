import os
from dotenv import load_dotenv
import requests
import json
import time

load_dotenv()


def gemini(user_input):
    gemini_API_key = 'Your Api key '

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_API_key}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": "Hello, how are you?"}
                ]
            }
        ]
    }


    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json() 
    output=response_json["candidates"][0]["content"]["parts"][0]["text"]   
    print("Gemini Response:", output)




user_input = input("Enter your query: ")

time_start = time.time()
gemini(user_input)
time_end = time.time()
print(f"Time taken for Gemini API call: {time_end - time_start:.2f} seconds")