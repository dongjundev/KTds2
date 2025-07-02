import requests
import os
from dotenv import load_dotenv

load_dotenv()

SUBSCRPTION_KEY=os.getenv("SUBSCRPTION_KEY")
ENDPOINT=os.getenv("ENDPOINT")

def analyze_image(image_path):
    ENDPOINT_URL = ENDPOINT + "vision/v3.2/analyze"

    params = {"visualFeatures": "Categories,Description,Color"}
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRPTION_KEY,
        "Content-Type": "application/octet-stream"
    }

    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
    except Exception as e:
        print(f"Error reading image file: {e}")
        return None
    
    response = requests.post(ENDPOINT_URL, params=params, headers=headers, data=image_data)
    if response.status_code == 200:
        analysis = response.json()
        return analysis
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
# Object detect function
def object_detect(image_path):
    ENDPOINT_URL = ENDPOINT + "vision/v3.2/detect"

    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRPTION_KEY,
        "Content-Type": "application/octet-stream"
    }

    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
    except Exception as e:
        print(f"Error reading image file: {e}")
        return None
    
    response = requests.post(ENDPOINT_URL, headers=headers, data=image_data)
    if response.status_code == 200:
        detection = response.json()
        return detection
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def main():
    image_path = input("Enter the path to the image file: ")

    print("1. Analyze Image")
    print("2. Object Detect")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        result = analyze_image(image_path)
    elif choice == '2':
        result = object_detect(image_path)
    else:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    if result:
        print("Analysis Result:")
        print(result)

if __name__ == "__main__":
    main()