import boto3
import json

endpoint_name = "jumpstart-dft-stable-diffusion-v2-1-base"


def query_endpoint(text):
    client = boto3.client("runtime.sagemaker")

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
