
# 📦 AWS Lambda S3 to DynamoDB + Email Notification

This project is an **AWS Lambda function** that automatically runs when a file is uploaded to an **S3 bucket**. It performs **two main tasks**:

1. ✅ Stores file upload details in a **DynamoDB table**
2. 📧 Sends an **email notification** using **SNS (Simple Notification Service)**



## 🚀 Features

- Automatically triggers when a file is uploaded to S3
- Stores file name, bucket, size, event type, and timestamp in DynamoDB
- Sends email alerts with full file upload details
- Uses UUID as a unique identifier for each record
- Serverless and cost-effective


## 🧠 How It Works (Simple Flow)

1. A file is uploaded to the S3 bucket
2. S3 triggers the Lambda function
3. Lambda does two things:
   - Saves file information to a DynamoDB table called `newtable`
   - Sends an email via SNS containing file details



## ⚙️ Technologies Used

- AWS Lambda (Python)
- Amazon S3
- Amazon DynamoDB
- Amazon SNS
- Python `boto3` library
- UUID for unique record IDs



## 📁 Project Structure

```
.
├── lambda_function.py   # Main Lambda code
└── README.md            # This file
```


## ✅ Prerequisites

Before you run the Lambda function, make sure you have:

1. **S3 bucket** (for file uploads)
2. **DynamoDB table** named `newtable`  
   - Primary key: `unique` (String)
3. **SNS Topic** with your **email address subscribed and confirmed**
4. Proper **IAM role permissions** for the Lambda function:
   - `dynamodb:PutItem`
   - `sns:Publish`



## 🔧 Setup Instructions

### 1. Create a DynamoDB Table

- Table Name: `newtable`
- Primary Key: `id` (String)

### 2. Create an SNS Topic

- Go to **SNS > Topics > Create topic**
- Name it anything (e.g., `MySNSTopic`)
- Create a **subscription** to this topic with:
  - **Protocol:** Email
  - **Endpoint:** Your email address
- **Confirm the email** from your inbox

### 3. Update Lambda Code

Replace the SNS Topic ARN in your code:

```python
SNS_TOPIC_ARN = "arn:aws:sns:your-region:your-account-id:MySNSTopic"
```

### 4. Set IAM Permissions for Lambda

Attach the following policy to the Lambda execution role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "sns:Publish"
      ],
      "Resource": "*"
    }
  ]
}
```

### 5. Create and Deploy the Lambda Function

- Go to AWS Lambda → Create function
- Use **Python 3.8 or 3.9**
- Paste the code from `lambda_function.py`
- Set the timeout to 1 minute

### 6. Add S3 Trigger to Lambda

- Go to your S3 bucket → Properties → Event Notifications
- Add new notification:
  - Event type: `All object create events`
  - Destination: **Lambda function**
  - Select your Lambda



## 🧪 Test the Project

1. Upload any file to your S3 bucket.
2. Check:
   - ✅ DynamoDB → New record is added
   - 📧 Email → You receive a file upload notification



## 📝 Sample Email Content

```
📂 New S3 Event Detected

Bucket: your-bucket-name
Object: example.png
Size: 3425 bytes
Event: ObjectCreated:Put
Time: 2025-07-07T12:00:00Z
```



## 📌 Use Cases

- File upload logs
- Real-time monitoring
- Simple alerting system
- Cloud automation practice
- Serverless project for DevOps portfolios


## 📚 Useful AWS Docs

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Amazon S3 Events](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)
- [Amazon SNS Email Notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html)
- [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)



## 👨‍💻 Author

**Muhammad Umair**  
*DevOps & Cloud Engineer*



## 📌 License

This project is for educational/demo use. You may modify and use it in your own serverless projects.
