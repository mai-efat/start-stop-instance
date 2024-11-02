# start-stop-instance

# EC2 Instance Management with AWS Lambda

This project automates the stopping and starting of AWS EC2 instances using AWS Lambda functions and CloudWatch Events. It consists of two Lambda functions: one to stop the instances and another to start them again. CloudWatch Events are used to trigger these functions based on a defined schedule.

## Prerequisites

- **IAM Role**: An IAM role with permissions to manage EC2 instances.

## Overview

### Lambda Functions

1. **StopEC2Instances**: This function stops specified EC2 instances at a scheduled time.
2. **StartEC2Instances**: This function starts the same EC2 instances a few minutes later.

### CloudWatch Events

- **Stop Rule**: A CloudWatch Events rule to trigger the `StopEC2Instances` function.
- **Start Rule**: A CloudWatch Events rule to trigger the `StartEC2Instances` function.

## Setup Instructions

### Step 1: Create an IAM Role

1. Go to the IAM Console.
2. Create a new role for Lambda with the following policy:

### Step 2: Create Lambda Functions
StopEC2Instances
Go to the Lambda Console.

Create a new Lambda function named StopEC2Instances.


### Step 3:StartEC2Instances
Create another Lambda function named StartEC2Instances.



### STEP 4 :Adjust the cron expressions based on your desired scheduling.
