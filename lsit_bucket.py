# List all the bucket name in AWS account
from turtle import clear
import boto3
client = boto3.client('s3')
response = client.list_buckets()
for Bucket in response['Buckets']:
    print(Bucket['Name'])
