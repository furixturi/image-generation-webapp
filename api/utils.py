import boto3
import json
from PIL import Image
import numpy as np

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


def save_image(pixels):
    arr = np.array(pixels, dtype=np.uint8)
    img = Image.fromarray(arr)
    img.save("new.png")
