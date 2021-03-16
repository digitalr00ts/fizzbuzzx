#!/bin/bash

zip -r aws_fizzbuzzx.zip aws_function.py

aws lambda create-function \
    --function-name "aws_fizzbuzzx" \
    --runtime "python3.8" \
    --role "arn:aws:iam::019263404189:role/fizzbuzzx_role" \
    --handler "aws_function.lambda_handler" \
    # To deploy the function code to lambda, a deployment package is needed.
    # Lambda supports two types of packages: container images and .zip files. 
    # AWS documentation on deploying python lambda functions with .zip: 
    # https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
    # Command to make .zip file deployment package:
    #       zip -r <file_name>.zip <folder_to_compress>
    --zip-file "fileb://aws_fizzbuzzx.zip" \
    --timeout 5 \
    --region "us-east-2"

