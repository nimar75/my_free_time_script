import boto3
import yaml

client = boto3.client('iam')
response = client.delete_user(
    UserName='nasim'
)
with open("sample.json", "w") as outfile:
    yaml.dump(response, outfile)

all_users = client.list_users(
)
with open("sample.json", "w") as outfile:
    yaml.dump(all_users, outfile)
#print(json.dumps(all_users, sort_keys=False, indent=8))
