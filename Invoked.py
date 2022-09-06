import json
import uuid

def lambdahandler(event, context):
    customerId = event['CustomerId']
    transactionId = str (uuid.uuid1())
    
    return {'CustomerId':customerId,'TransactionId':transactionId}