import base64
import json

class InputGenerator:
    def __init__(self, img_path) -> None:
        self.img_path = img_path

    def generate_input_file(self):
        imgdata = self._configure_data()
        with open("test_input.json", 'w') as json_file:
            json.dump(imgdata, json_file)

    def _configure_data(self):
        with open(self.img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        img_b64 = encoded_string.decode("utf-8")
        return {"input": {"img": img_b64}}
