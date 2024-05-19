import json
import os
import boto3
import csv

def lambda_handler(event, context):
    payload=event['Payload']
    s3_uri=payload['s3uri']
    arr=s3_uri.split('/')
    bucket=arr[2]
    key=''
    for i in range(3,len(arr)):
        key=key+arr[i]+'/'
        
    key = key[:-1]
    
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object(bucket, key)

    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()

    lines = csv.reader(data)
    numbers = next(lines)
    
    result = list(map(lambda x: float(x) * 2, numbers))
    
    return {'result':result, 'bucket':bucket}
