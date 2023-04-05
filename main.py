import json
import boto3
import datetime
dynamodb = boto3.client('dynamodb')
table_name = 'ids721-p4'
def lambda_handler(event, context):
    sentimentClient = boto3.client("comprehend")
    Text = event.get("Text",None)
    response = sentimentClient.detect_sentiment(
        Text = Text,
        LanguageCode = 'en'
        )
    score = response['Sentiment']
    tz = datetime.timezone.utc
    ft = "%Y-%m-%dT%H:%M:%S%z"
    currTime = datetime.datetime.now(tz=tz).strftime(ft)
    item = {
    'time': {'S': currTime},
    'message': {'S': Text},
    'score': {'S': response['Sentiment']}
    }

    # Insert the item into the DynamoDB table
    dynamodb.put_item(TableName=table_name, Item=item)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Response from Lambda!'),
        'Response':response
    }
