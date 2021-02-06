#!/bin/bash

aws lambda create-function \
    --function-name "aws_fizzbuzzx" \
    --runtime "python3.8" \
    --role "arn:aws:iam::019263404189:role/fizzbuzzx_role" \
    --handler "aws_function.lambda_handler" \
    --zip-file "fileb://aws_fizzbuzzx.zip" \
    --timeout 5 \
    --region "us-east-2"

