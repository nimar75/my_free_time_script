import boto3
import json
client = boto3.client('s3')
response = client.complete_multipart_upload(
    Bucket='',
    Key='',
    MultipartUpload={
        'Parts': [
            {
                'ETag': '""',
                'PartNumber': '',
            },

        ],
    },
    UploadId='',
)

print(json.dumps(response, sort_keys=False, indent=4))
