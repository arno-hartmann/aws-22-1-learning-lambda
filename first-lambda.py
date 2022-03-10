import json
import boto3

client = boto3.client('sns')
s3client = boto3.client('s3')

def lambda_handler(event, context):
  
   key = event['Records'][0]['s3']['object']['key']
   bucket = event['Records'][0]['s3']['bucket']['name']

   response = s3client.get_object(
      Bucket = bucket,
      Key = key
      )
   
   text = response['Body'].read()

   words = text.split()
   numberOfWords = len(words)
   
   message = 'Number of words in text file {} is {}'.format(key, numberOfWords)
   
   print(message)
   client.publish(TargetArn = "arn:aws:sns:us-west-2:694046024538:drop-file-mail", Message = message)