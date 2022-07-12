import boto3
import json
client = boto3.client('s3')
response = client.abort_multipart_upload(
    Bucket='',
    Key='',
    UploadId='',
)
print(json.dumps(response, sort_keys=False, indent=4))
