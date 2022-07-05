# DCIM= Data Center Infrastructure Management
from lib2to3.pgen2.pgen import DFAState
import boto3
import json
client = boto3.client('s3')
Region = [""]
Bucket_name = [""]
counter = 0

for az in Region:
    response = client.create_bucket(
        ACL='private',
        Bucket=Bucket_name[counter],
        CreateBucketConfiguration={
            'LocationConstraint': az
        },
    )

print(json.dumps(response, sort_keys=False, indent=4))
