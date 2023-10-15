import runpod
from dotenv import load_dotenv
import os
from model import CVModelYolo
from recipe import RecipeFinder

# Get the Base64 encoded string from the environment variable
roboflow_api = os.getenv("ROBOFLOW_API_KEY")
# load model
load_dotenv()
CONFIG_PATH = "./config"
model = CVModelYolo(
    weights=os.path.join(CONFIG_PATH, "best.pt"),
    yaml_path=os.path.join(CONFIG_PATH, "class_names.yaml"),
)


def handler(event):
    """
    Expected event object:
    "input": {
        "img": base_64 image to run prediction on (str)
        "threshold": float 0-1 to determine percentage of ingredients matched before returning
        "conf": confidence threshold to predict (int 0-100)
    }
    """
    # model inference, returns classes
    input = event["input"]
    b64_img = input["img"]
    img_path = model.process_save_b64(b64_img)
    try:
        conf = input["conf"]
        classes = model.predict(img_path, conf=conf)
    except KeyError:
        classes = model.predict(img_path)
    recipe_finder = RecipeFinder(
        class_names=classes,
        json_ingredients_filepath=os.path.join(
            CONFIG_PATH, "ingredient_to_recipes.json"
        ),
        json_recipe_filepath=os.path.join(CONFIG_PATH, "recipe_to_ingredients.json"),
    )
    # get recipes
    try:
        threshold = input["threshold"]
        recipes = recipe_finder.get_recipes(threshold)
    except KeyError:
        recipes = recipe_finder.get_recipes()
    
    return {"classes": classes, "recipes": recipes}


# from utils import InputGenerator

# gen = InputGenerator("test1.jpg")
# gen.generate_input_file()

# start the local serverless instance
runpod.serverless.start({"handler": handler})
