import boto3
from uuid import uuid4

# Initialize AWS clients globally
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

# Replace with your actual SNS topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:MySNSTopic"

def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        size = record['s3']['object'].get('size', -1)
        event_name = record['eventName']
        event_time = record['eventTime']

        # Save to DynamoDB
        dynamoTable = dynamodb.Table('newtable')  # name of dynamic db 
        dynamoTable.put_item(
            Item={
                'id': str(uuid4()),
                'Bucket': bucket_name,
                'Object': object_key,
                'Size': size,
                'Event': event_name,
                'EventTime': event_time
            }
        )

        # Send email via SNS
        message = (
            f"📂 New S3 Event Detected\n\n"
            f"Bucket: {bucket_name}\n"
            f"Object: {object_key}\n"
            f"Size: {size} bytes\n"
            f"Event: {event_name}\n"
            f"Time: {event_time}"
        )
        
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="🔔 New File Uploaded to S3",
            Message=message
        )
