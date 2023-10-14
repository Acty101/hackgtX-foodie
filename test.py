import os
import time
import json
from utils import InputGenerator

URL = "https://api.runpod.ai/v2/mi1w7cfskbr6up"


def main():
    import requests
    from dotenv import load_dotenv

    load_dotenv()
    img = "test_img.webp"
    InputGenerator(img).generate_input_file()
    with open("./test_input.json", "r") as json_file:
        data = json.load(json_file)
    payload = data
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": os.getenv("RUNPOD_API_KEY"),
    }

    response = requests.post(os.path.join(URL, "run"), json=payload, headers=headers)
    response = response.json()
    print(response)
    STATUS = response["status"]
    result_url = os.path.join(URL, "status", response["id"])
    print(result_url)
    while STATUS == "IN_QUEUE" or STATUS == "IN_PROGRESS":
        # wait awhile and update
        print("waiting for response...")
        time.sleep(5)
        response = requests.get(result_url, headers=headers)
        response = response.json()
        STATUS = response["status"]

    print("Not in queue anymore")

    if STATUS == "COMPLETED":
        print("Output received!")
        print(response)
    else:
        print("Couldn't receive output")
        print("Response:", response)


if __name__ == "__main__":
    main()
