import boto3

ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name ='/myweb/database1_password',WithDecryption=True)
print(parameter['Parameter']['Value'])