def echo(event, context):

    response = {
        "statusCode": 200,
        "body": event['body']
    }

    return response
