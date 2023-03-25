import json
import boto3


def lambda_handler(event, context):
    sentimentClient = boto3.client("comprehend")
    Text = event.get("Text", None)
    response = sentimentClient.detect_sentiment(
        Text=Text,
        LanguageCode='en'
    )

    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Response from Lambda!'),
        'Response': response
    }
