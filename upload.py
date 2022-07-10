import boto3
import os
import json
client = boto3.client('s3')
response = client.upload_part(
    Body="",
    Bucket='',
    Key='',
    PartNumber=2,
    UploadId='',
)
print(json.dumps(response, sort_keys=False, indent=4))
