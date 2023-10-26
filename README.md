# HackGT X `Let's Cook!` Microservice Architecture Backend
## Winner - 1st place sustainability track

Backend for recipe recommender web-app deployed on [RunPod](https://docs.runpod.io/docs)

Check out the frontend here: [link](https://github.com/ghubnerr/pots_n_pans)


## Usage
- POST a request to the following URL `https://api.runpod.ai/v2/mi1w7cfskbr6up/runsync` with proper credentials and a payload of a base_64 encoded image
- Returns an object with the following schema:
  ```<JSON>
  {
  delayTime: number;
  executionTime: number;
  id: string;
  output: {classes: string[], recipes: string[]};
  status: string;
  }
  ```

## Microservices
- Object detection model (Ultralytics YOLOv8 [repo](https://github.com/ultralytics/ultralytics))
- Recipe finder script
