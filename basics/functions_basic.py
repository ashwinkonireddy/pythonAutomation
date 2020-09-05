
def getAwsRegions():
        import boto3
        ec2 = boto3.client('ec2',
                        aws_access_key_id='AKIARANTI7G6XDRIPYXE',
                        aws_secret_access_key='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',
                        region_name='us-east-1'
                        )
        aws_regions = ec2.describe_regions()

        aws_regions = ec2.describe_regions().get('Regions', [])

        # print(aws_regions)
        allRegions = []

        for region in aws_regions:
            allRegions.append(region['RegionName'])
            # print(region['RegionName'])

        # print(allRegions)
        print(allRegions[0])
        print(allRegions[1])
        print(allRegions[2])
        print(allRegions[3])
        print(allRegions[4])
