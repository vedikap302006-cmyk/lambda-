def lambda_handler(event, context):
    num1 = event["num1"]
    num2 = event["num2"]

    result = num1 + num2

    return {
        "statusCode": 200,
        "body": {
            "num1": num1,
            "num2": num2,
            "sum": result
        }
    }