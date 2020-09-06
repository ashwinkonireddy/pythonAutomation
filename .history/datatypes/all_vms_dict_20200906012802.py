'''
Example of list and tuples
'''
import boto3
my_all_regions = []
ec2 = boto3.client('ec2',
                        aws_access_key_id='AKIARANTI7G6UJEJJ44F', 
                        aws_secret_access_key='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',
                        region_name='us-east-1'
                        )
aws_regions = ec2.describe_regions()

# print(type(aws_regions)) #<class 'dict'>
# print(aws_regions.keys()) #dict_keys


aws_regions = ec2.describe_regions().get('Regions', "Key not found")
all_vms = ec2.describe_instances().get('Reservations', "Key Not Found")
# print(all_vms)

# for region in aws_regions:
    # my_all_regions.append(region['RegionName'])
    # print(region['RegionName'])

for vm in all_vms['Instances']:
    # print(vm['InstanceId']) 
    # print(vm['InstanceId']) 
    print(100 * "=")


# fixed_regions = tuple(my_all_regions)

# print(fixed_regions)

# for region in fixed_regions:
#     print(region)

