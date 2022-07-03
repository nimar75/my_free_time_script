import boto3
import yaml

client = boto3.client('iam')
access_key = client.create_access_key(
    UserName='nasim'
)
print = yaml.dump(access_key)
