import json
import boto3
import csv
import io

s3client = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(bucket)
    print(key)


    response = s3client.get_object(Bucket=bucket, Key = key)

    data = response['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(data))
    next(reader)
    for row in reader:
        print(str.format("id - {}, name - {}, email - {}",row[0],row[1],row[2]))

    client = boto3.client('lambda')
    inputForInvoker = {'CustomerId': '123', 'Amount': 50}
    

    response = client.invoke(
        FunctionName='Arn',
        InvocationType='RequestResponse',  # Event
        Payload=json.dumps(inputForInvoker)
    )

    responseJson = json.load(response['Payload'])

    print('\n')
    print("Data from Invoked Lambda")
    print(responseJson)
    print('\n')