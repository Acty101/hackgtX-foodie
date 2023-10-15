from roboflow import Roboflow
from ultralytics import YOLO
from PIL import Image
from io import BytesIO
from abc import ABC
import base64
import yaml


class CVModel(ABC):
    def process_save_b64(self, base64_string):
        """Function to process b64 img and return path to it"""
        # Decode the Base64 string
        image_data = base64.b64decode(base64_string)

        # Create an image object
        img = Image.open(BytesIO(image_data))

        # Save the image
        img_path = "./output_image.png"
        img.save(img_path)

        return img_path


class CVModelYolo(CVModel):
    def __init__(self, weights, yaml_path=".class_names.yaml") -> None:
        # load the model from weights
        self.model = YOLO(weights)
        # Read and parse the YAML file
        with open(yaml_path, "r") as yaml_file:
            data = yaml.safe_load(yaml_file)
        self.class_names = data["names"]

    def predict(self, img_file, conf=0.4):
        results = self.model.predict(img_file, conf=conf, save=False)
        class_index = []
        for result in results:
            last_column_tensor = result.boxes.data[:, -1]

            # Convert the PyTorch tensor to a list of integers
            class_index = last_column_tensor.cpu().int().tolist()
        names = []
        for index in class_index:
            names.append(self.class_names[index])
        return names


class CVModelRoboflow(CVModel):
    def __init__(self, api_key) -> None:
        rf = Roboflow(api_key=api_key)
        project = rf.workspace().project("detection-cuaeq")
        self.model = project.version(6).model    

    def predict(self, img_file, conf=0.4, overlap=0.3):
        datas = self.model.predict(
            img_file, confidence=conf * 100, overlap=overlap * 100
        ).json()
        return self._get_classes(datas["predictions"])

    def _get_classes(self, data):
        """Function to process data and get class names out of it"""
        result = []
        for entry in data:
            result.append(entry["class"])
        return result
