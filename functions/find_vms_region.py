import boto3
my_all_regions = []
ec2 = boto3.client('ec2',
                        aws_access_key_id='', 
                        aws_secret_access_key='',
                        region_name='us-east-1'
                        )
allRegions =  ec2.describe_regions().get('Regions', [])

for region in allRegions:
    print(region['RegionName'])
    print(100 * "=")