import boto3
import requests

s3 = boto3.client('s3')

def pull_down(key):
    response = s3.get()
    print(response)

pull_down('14828582348238424')

