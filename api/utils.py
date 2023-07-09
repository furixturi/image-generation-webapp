import boto3
import json
from PIL import Image
import numpy as np
from io import BytesIO
import base64

endpoint_name = "jumpstart-dft-stable-diffusion-v2-1-base"
client = boto3.client("runtime.sagemaker")


def query_endpoint(text):
    encoded_text = text.encode("utf-8")
    response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/x-text",
        Body=encoded_text,
        Accept="application/json",
    )

    return response


def parse_response(query_response):
    response_dict = json.loads(query_response["Body"].read())
    return response_dict["generated_image"], response_dict["prompt"]


def pixel_to_image(pixel_array):
    arr = np.array(pixel_array, dtype=np.uint8)
    img = Image.fromarray(arr)
    return img


def save_image(img, filePath="generated_images/new.png"):
    img.save(filePath)


def image_to_base64_str(img, format="PNG"):
    buffered = BytesIO()
    img.save(buffered, format=format)
    img_str = base64.b64encode(buffered.getvalue())
    return img_str
