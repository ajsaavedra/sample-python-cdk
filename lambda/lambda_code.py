import json
import random

def broken_func(event):
    random_num=random.randint(0,9)
    if random_num >= 5:
        try:
            raise ValueError('Represents a hidden bug, catch this')
        except ValueError as error:
            print('Caught this error: ' + repr(error))
    return 'Hello, CDK! You have hit {}\n'.format(event['path'])

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': broken_func(event)
    }