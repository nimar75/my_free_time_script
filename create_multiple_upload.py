import boto3
import json
client = boto3.client('s3')
response = client.create_multipart_upload(
    Bucket='',
    Key='',
)

print(json.dumps(response, sort_keys=False, indent=4))
