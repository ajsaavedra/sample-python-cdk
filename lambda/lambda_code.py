import json
import random

def broken_func():
    random_num=random.randint(0,9)
    if random_num >= 5:
        return 'Hello, CDK! Your number is {}\n'.format(random_num)
    return 'Hello, CDK! Your number is {}\n'.format(other_num)

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': broken_func()
    }