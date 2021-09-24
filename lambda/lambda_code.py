import json
import random

def broken_func():
    random_num=random.randint(0,9)
    return 'Hello, CDK! Your number is {}\n'.format(random_number)

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': broken_func()
    }