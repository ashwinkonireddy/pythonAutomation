import boto3
ec2 = boto3.client('ec2', 
aws_access_key_id='AWS_ACCESSKEY', 
aws_secret_access_key='AWS_SECTRET_KEY',
region_name='us-east-1' 
)
aws_regions = ec2.describe_regions()

aws_regions = ec2.describe_regions().get('Regions', [])

# print(aws_regions)
 
for region in aws_regions:
    print(region['RegionName'])



# ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# print(response)
