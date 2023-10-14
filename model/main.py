from roboflow import Roboflow
import base64
import json
from PIL import Image
from io import BytesIO


class CVModel:
    def __init__(self, api_key) -> None:
        rf = Roboflow(api_key=api_key)
        project = rf.workspace().project("group_work")
        self.model = project.version(2).model

    def get_model(self):
        return self.model

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

    def predict(self, img_file, conf=40, overlap=30):
        datas = self.model.predict(img_file, confidence=conf, overlap=overlap).json()
        return self._get_classes(datas["predictions"])

    def _get_classes(self, data):
        """Function to process data and get class names out of it"""
        result = []
        for entry in data:
            result.append(entry["class"])
        return result
