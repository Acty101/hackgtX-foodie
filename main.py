import runpod
from dotenv import load_dotenv
import os
from model import CVModel
import utils

# Get the Base64 encoded string from the environment variable
roboflow_api = os.getenv("ROBOFLOW_API_KEY")
# load model
load_dotenv()
model = CVModel(roboflow_api)


def handler(event):
    """
    Expected event object: 
    "input": {
        "img": base_64 image to run prediction on (str)
        "conf": confidence threshold to predict (int 0-100)
        "overlap": acceptable overlap (int 0-100)
    }
    """
    # model inference, returns classes
    input = event["input"]
    b64_img = input["img"]
    img_path = model.process_save_b64(b64_img)
    try:
        conf = input["conf"]
        overlap = input["overlap"]
        classes = model.predict(img_path, conf=conf, overlap=overlap)
    except KeyError:
        classes = model.predict(img_path)
    return classes
    # hit api


# from utils import InputGenerator

# gen = InputGenerator("./vegan-food-and-ingredients.webp")
# gen.generate_input_file()

# start the local serverless instance
runpod.serverless.start({"handler": handler})
