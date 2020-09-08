import boto3
s3 = boto3.client('s3',
                        aws_access_key_id='', 
                        aws_secret_access_key='',
                        # region_name='us-east-1'
                        )
objects = s3.list_objects(
    Bucket='ashwinkonireddy2019',
    # MaxKeys=1
)
print("Using list Comp")
print([file['Key'] for file in objects['Contents'] ])

# print(objects['Contents'])
# fileNames = []
# for file in objects['Contents']:
#     fileNames.append(file['Key'])

# print(fileNames)
# print(len(fileNames))
# print(len(set(fileNames))) #To remove duplicates

# if(len(fileNames) > 1 and len(fileNames) <2):
#     print(f'Files are between {len(fileNames)}')
# else:
#     print(f'Files are not between {len(fileNames)}')

 