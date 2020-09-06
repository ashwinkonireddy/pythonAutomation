import boto3
my_all_regions = []
ec2 = boto3.client('ec2',
                        aws_access_key_id='AKIARANTI7G6XAUZPBWY', 
                        aws_secret_access_key='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',
                        # region_name='us-east-1'
                        )
aws_regions = ec2.describe_regions()

print(type(aws_regions)) #<class 'dict'>
print(aws_regions.keys()) #dict_keys


aws_regions = ec2.describe_regions().get('Regions', "Key not found")

print(aws_regions)

for region in aws_regions:
    my_all_regions.append(region['RegionName']);
    # print(region['RegionName'])

