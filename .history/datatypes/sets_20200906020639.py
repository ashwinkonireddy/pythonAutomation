'''
Example of Set
[] List
() tuple
{} Set
'''
import boto3
my_all_regions = []
ec2 = boto3.client('ec2',
                        aws_access_key_id='AKIARANTI7G6UJEJJ44F', 
                        aws_secret_access_key='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',
                        # region_name='us-east-1'
                        )
aws_regions = ec2.describe_regions().get('Regions', "Key not found")
for region in aws_regions:
    my_all_regions.append(region['RegionName'])
    print(region['RegionName'])

for region in aws_regions:
    my_all_regions.append(region['RegionName'])
    print(region['RegionName'])

print(len(my_all_regions))
print(len(set(my_all_regions))) #Set Remove duplicates

print('us-east-1' in my_all_regions)

fixed_regions = tuple(my_all_regions)
print(fixed_regions) 



# print(type(aws_regions)) #<class 'dict'>
# print(aws_regions.keys()) #dict_keys


# aws_regions = ec2.describe_regions().get('Regions', "Key not found")
# all_vms = ec2.describe_instances().get('Reservations', "Key Not Found")
# # print(all_vms)



# for vms in all_vms:
#     for vm in vms['Instances']:
#         print(vm['InstanceId'], vm['InstanceType']) 
#     print(100 * "=")


# # fixed_regions = tuple(my_all_regions)

# # print(fixed_regions)

# # for region in fixed_regions:
# #     print(region)

