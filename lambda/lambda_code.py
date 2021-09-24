import json
import random

def broken_func():
    random_num=random.randint(0,9)
    if random_num >= 5:
        try:
            raise ValueError('Represents a hidden bug, catch this')
            raise Exception('This is the exception you expect to not handle')
        except ValueError as error:
            print('Caught this error: ' + repr(error))
    return 'Hello, CDK! Your number is {}\n'.format(random_num)

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': broken_func(event['path'])
    }