from cgitb import reset
import yaml
import boto3
import json
name = ['nasim', 'niloo']
client = boto3.client('iam')
for i in name:
    response = client.create_user(
        UserName=i,
    )
    with open("user.yaml", "w") as outfile:
        yaml.dump(reset, outfile)
    access_key = client.create_access_key(
        UserName=i,
    )
    with open("access.yaml", "w") as outfile:
        yaml.dump(access_key, outfile)
