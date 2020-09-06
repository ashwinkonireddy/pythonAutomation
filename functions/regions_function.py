import boto3
def get_regions(rName):
    # region_input = str(input("\nPlease enter your region name: "))
    ec2 = boto3.client('ec2',
                        aws_access_key_id='', 
                        aws_secret_access_key='',
                        region_name=rName
                        )
    # vms = ec2.describe_instances().get('Reservations', "No VM found")
    all_vms = ec2.describe_instances().get('Reservations', "Key Not Found")
    instance_type = []
    for vms in all_vms:
        for vm in vms['Instances']:
            instance_type.append(vm['InstanceId'] + " " + vm['InstanceType'])
            # print(vm['InstanceId'], vm['InstanceType']) 
    return(instance_type)

print(get_regions('us-east-1'))
print(100 * "=")
print(get_regions('us-east-2'))
print(100 * "=")
print(get_regions('us-west-1'))
print(100 * "=")
print(get_regions('us-west-2'))
print(100 * "=")