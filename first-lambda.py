import json
import boto3

snsclient = boto3.client('sns')
s3client = boto3.client('s3')

def lambda_handler(event, context):
  
   bucket = event['Records'][0]['s3']['bucket']['name']
   key = event['Records'][0]['s3']['object']['key']

   response = s3client.get_object(
      Bucket = bucket,
      Key = key
      )
   
   text = response['Body'].read()

   words = text.split()
   numberOfWords = len(words)
   
   message = 'Number of words in text file {} is {}'.format(key, numberOfWords)
   
   print(message)

   # Use arn of the sns. Check for same Region!
   snsclient.publish(TargetArn = "arn:aws:sns:us-west-2:694046024538:drop-file-mail", Message = message)