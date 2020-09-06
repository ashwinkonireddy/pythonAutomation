import boto3
        ec2 = boto3.client('ec2',
                        aws_access_key_id='AKIARANTI7G6XAUZPBWY', 
                        aws_secret_access_key='AWS_SECTREPMjpmhZy7Zr2vetqMn1KiEST60cpGlcQBuq2vm/rT_KEY',
                        region_name='us-east-1'
                        )
        aws_regions = ec2.describe_regions()

        aws_regions = ec2.describe_regions().get('Regions', [])