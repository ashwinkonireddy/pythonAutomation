import boto3


def s3Bucket(bucketName, searchFileName):
    s3 = boto3.client('s3',
                      aws_access_key_id='',
                      aws_secret_access_key='',
                      # region_name='us-east-1'
                      )
    objects = s3.list_objects(
        Bucket=bucketName,
        # Bucket='ashwinkonireddy2019',
        # MaxKeys=1
    )
    fileNames = []
    for file in objects['Contents']:
        if file['Key'] == searchFileName:
            # fileNames.append(file['Key'])
            print(f'{searchFileName} File Found!!')
            break
            # continue
        else:
            print(f'File not found!!')
    print(fileNames)


s3Bucket('ashwinkonireddy2019', 'Screenshot 2019-11-28 at 04.43.23.png')
