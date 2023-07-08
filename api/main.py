from typing import Union

from fastapi import FastAPI

import utils

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/generate-image")
def generate_image(prompt: str):
    image, prmpt = utils.parse_response(utils.query_endpoint(prompt))
    utils.save_image(image)
    return {"prompt": prmpt}
