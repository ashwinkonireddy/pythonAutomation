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


for file in objects['Contents']:
    key = file['Key']
    if key == filename:
        print(f'{filename} found ... existing the existing search!!!')
        continue
    else:
        print("File not found")



if(len(fileNames) > 1 and len(fileNames) <2):
    print(f'Files are between {len(fileNames)}')
else:
    print(f'Files are not between {len(fileNames)}')

 