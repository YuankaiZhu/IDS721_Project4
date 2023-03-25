# IDS721 Project 4 

## Serverless Data Engineering Pipeline for Sentiment Analysis 

In this project, language sentiment analysis is deployed using AWS Lambda serverless technologies. 

The basic architecture is showed in following image:

![image-20230325120545523](./IDS721 Project 4.assets/image-20230325120545523.png)

1. lambda_handler function is implemented for getting sentiment analysis result from AWS Comprehend and returning the response. 
2. AWS API Gateway is implemented for deploying this AWS Lambda function. 

![image-20230325120929856](./IDS721 Project 4.assets/image-20230325120929856.png)