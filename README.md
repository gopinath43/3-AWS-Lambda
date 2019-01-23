# AWS-Lambda
AMI backup of the instances using AWS Lambda function with CloudWatch event triggers.

An Amazon Machine Image (AMI) provides the information required to launch an instance, which is a virtual server in the cloud. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations.

This lambda function will create AMI(Amazon Machine Images) of instances , only when you add instance id into the lambda function.

 Pre-Requisities
 ----------------
  •	Create a IAM role choosing Lambda ( Allows Lambda functions to call AWS services on your behalf ) with AmazonEC2FullAccess policy attached with role name as "AMIBackupRole".
  
  •	Few instances , running or stopped. ( In our case: Ansible-Master , WEB01 , APP01 and DB01 instance )
  
  •	We are expermenting this lambda function on all the instances accordingly.

 Configure Lambda Function
 -------------------------
 This is very basic lambda function written Python3.6 to takeup the ami backup of the instance.
 Remember to choose the same in lambda function.
 
  • Copy the code from lambda-ami-backup.py in this repo to the lambda function and attach the "AMIBackupRole" created.
  
  • If you have a lot of Instances, then consider increasing the lambda run time, the default is 3 seconds.
  
  • Save the lambda function
  
  Configure Lambda Triggers
  -------------------------
  We are going to use Cloudwatch Scheduled Events to take backup everyday.
  
  rate(1 minute)
  or
  rate(5 minutes)
  or
  rate(1 day)
  
  # The below example creates a rule that is triggered every day at 12:00pm UTC.
  
  cron(0 12 * * ? *)
  
  Testing the solution
  --------------------
  Before we start testing , make sure you have added the instance id respectively and save it to take the backup of the instance.
  
  Summary
  -------
  We have demonstrated how we can identify instances with instances id that require AMI Backup, create AMIs and tag them.
