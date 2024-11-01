import boto3
import os

ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    
    instance_id = os.environ['INSTANCE_ID']
    
    # Stop the instance
    print(f"Stopping EC2 instance {instance_id}")
    ec2_client.stop_instances(InstanceIds=[instance_id])
    
    return {
        'statusCode': 200,
        'body': f"EC2 instance {instance_id} stopped."
    }
