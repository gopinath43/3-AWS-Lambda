#!/usr/bin/env python
import boto3
def lambda_handler(event, context):
    session = boto3.Session(
        region_name='ap-southeast-1')
    ec2 = session.client('ec2')
    response = ec2.create_image(
          Description='BACKUP-AMI',
          InstanceId='i-xxxxxxxxxxxxx',
        Name='BACKUP-AMI',
        NoReboot=False
    )
    
    print(response)
