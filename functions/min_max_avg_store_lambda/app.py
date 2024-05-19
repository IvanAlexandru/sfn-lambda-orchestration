import csv
import boto3
import json
import statistics

def lambda_handler(event, context):
    payload = event['Payload']
    s3 = boto3.resource('s3')
    bucketName = payload['bucket']
    bucket = s3.Bucket(bucketName)
    key = 'result.csv'
    
    arr = payload['result']
    
    minValue = min(arr)
    maxValue = max(arr)
    avgValue = statistics.mean(arr)

    with open('/tmp/result.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow((minValue, maxValue, avgValue))
    bucket.upload_file('/tmp/result.csv', key)
