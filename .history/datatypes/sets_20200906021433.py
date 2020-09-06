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
                        region_name='us-east-1'
                        )
aws_regions = ec2.describe_regions().get('Regions', "Key not found")
all_vms = ec2.describe_instances().get('Reservations', "Key Not Found")
for region in aws_regions:
    my_all_regions.append(region['RegionName'])
    print(region['RegionName'])

for region in aws_regions:
    my_all_regions.append(region['RegionName'])
    print(region['RegionName'])

print(100 * "=")
print(len(my_all_regions))
removed_dups = set(my_all_regions) #Set Remove duplicates
print(len(set(removed_dups))) 
print(removed_dups) 

print('us-east-1' in removed_dups)# bool




for vms in all_vms:
    for vm in vms['Instances']:
        print(vm['InstanceId'], vm['InstanceType']) 
user_input = str(input("Please enter the instance type"))
if(user_input in instance_type):
    print(f,"Machine type {user_input} exist")
else:
    print(f,"Machine type not {user_input} exist")
    print(100 * "=")

# fixed_regions = tuple(my_all_regions)
# print(fixed_regions) 



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

