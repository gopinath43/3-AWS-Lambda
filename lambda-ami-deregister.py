#!/usr/bin/env python
import boto3
import datetime
from datetime import datetime, timedelta
def lambda_handler(event, context):
    AMILIST=[]
    SNAPLIST=[]
    session=boto3.Session(region_name='ap-southeast-1')
    ec2=session.client('ec2')
    response=ec2.describe_images(
        Filters=[
            {
                'Name':'description',
                'Values':['TERRAFORM-AMI',]
            },
        ],
    )
    for items in response['Images']:
        AMILIST.append(items['ImageId'])

    print(AMILIST)


    #function to get the SNAPshots for the given AMI
    def GETSNAPLIST(AMIID):
        snaplist=[]
        response1=ec2.describe_images(
        ImageIds=[AMIID,])
        for k in response1['Images']:
            for items in k['BlockDeviceMappings']:
                snaplist.append(items['Ebs']['SnapshotId'])
        return snaplist


    # function to get the AMI creation date

    def AMICREATIONDATE(AMIID):
      response2=ec2.describe_images(
            ImageIds=[AMIID, ])
      for items in response2['Images']:
          creationdateformat = items['CreationDate']
          print(items['CreationDate'])
      creationdate = datetime.strptime(creationdateformat, "%Y-%m-%dT%H:%M:%S.%fZ")
      print(creationdate)
      return creationdate


    #function to deregister an AMI

    def DEREGISTER(AMIID):
        response3 = ec2.deregister_image(ImageId=AMIID)

    #function to delete the snapshots

    def DELETESNAPSHOT(SNAPSHOTID):
        response4 = ec2.delete_snapshot(SnapshotId=SNAPSHOTID)


    #AMI and SNAPSHOT Managemenet

    for i in range(len(AMILIST)):
        CREATIONDATE=AMICREATIONDATE(AMILIST[i])
        DELETEDATE=datetime.now()-timedelta(days=7)
        if CREATIONDATE<DELETEDATE:
            SNAPLIST=GETSNAPLIST(AMILIST[i])
            DEREGISTER(AMILIST[i])
            print("AMI Deregistered - "+AMILIST[i])
            for i in range(len(SNAPLIST)):
                DELETESNAPSHOT(SNAPLIST[i])
                print(SNAPLIST[i]+"-SNAPSHOT-DELETED")
