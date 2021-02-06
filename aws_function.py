"""
Python file for AWS Lambda function handler in order to help process events.
"""
import json
from typing import Dict, ContextManager


def lambda_handler(event: Dict, context: ContextManager) -> Dict:
    """Function that when invoked, Lambda run the handler method

    Args:
        event (Dict): JSON formatted doc that contains data for lambda function to process
        context (ContextManager): Provides methods and properties that provide information
        about the invocation, function, and execution environment

    Returns:
        JSON payload that contains status code and message.
    """
    print("Hello from Lambda!")
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
