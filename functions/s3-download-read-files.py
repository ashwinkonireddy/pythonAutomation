import boto3
import urllib.request


def s3DownloadRead(bucketName, searchFileName):
    s3 = boto3.client('s3',
                        aws_access_key_id='', 
                        aws_secret_access_key='',
                        # region_name='us-east-1'
                      )
    # objects = s3.list_objects(
    #     Bucket=bucketName,
    #     # Bucket='ashwinkonireddy2019',
    #     # MaxKeys=1
    # )

    s3.download_file(bucketName, searchFileName, searchFileName)
    f1 = open(searchFileName, "r")
    print(f1.read())
    exit(0)
    # f1.write("python is fun and hard")
    # print(f1.read()) 
    # f1.close()



    # f1 = open(searchFileName, "r")
    # print(f1.read())
    # print(100 * "=")
    # with open(searchFileName, "r") as file:
    #     print(file.read())



'''

    fileNames = []
    for file in objects['Contents']:
        print(file['Key'])
        if file['Key'] == searchFileName:
            # fileNames.append(file['Key'])
            print(f'{searchFileName} File Found!!')
            # location = s3.get_bucket_location(Bucket=bucketName)
            url = "https://s3.amazonaws.com/%s/%s" % (bucketName, searchFileName)
            # url = location
            print(url)
            with urllib.request.urlopen(url) as f:
                html = f.read().decode('utf-8')
                # f1 = open(f, "r") 
            print(html)
            
            # print(f1.read())
            break 
            # continue
        else:
            print(f'File not found!!')
    print(fileNames)

'''
s3DownloadRead('ashwinkonireddy2019', 'datatypes.txt')
