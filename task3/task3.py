import json
import re

import boto3
from boto3.dynamodb.conditions import Key


class InvalidResponse(Exception):
    def __init__(self, status_code):
        self.status_code = status_code


# Don't modify this function name and arguments
def query_user_notes(user_email):
    dynamo_db = boto3.resource('dynamodb')
    user_notes_table = dynamo_db.Table('user-notes')
    result = user_notes_table.query(
        KeyConditionExpression=Key('user').eq(user_email),
        Limit=10,
        ScanIndexForward=False
    )
    items = result.get('Items', [])
    notes = []
    for item in items:
        note = {
            'id': item['id'],
            'create_date': item['create_date'],
            'text': item['text']
        }
        notes.append(note)
    return notes


# Don't modify this function name and arguments
def get_authenticated_user_email(token):
    dynamo_db = boto3.resource('dynamodb')
    tokens_table = dynamo_db.Table('token-email-lookup')

    # Validate the given token with one from the database
    response = tokens_table.get_item(
        Key={
            'token': token
        }
    )
    # and return user email if the tokens match ...
    item = response.get('Item', {})
    if not item:
        raise InvalidResponse(403)

    return item.get('email')


def authenticate_user(headers):
    if 'Authentication' not in headers:
        raise InvalidResponse(400)    
    authentication_header = headers['Authentication']

    # Validate the Authentication header
    if not authentication_header or not authentication_header.startswith('Bearer '):
        raise InvalidResponse(400)

    token = authentication_header.split(' ')[1]
    user_email = get_authenticated_user_email(token)

    return user_email


def build_response(status_code, body=None):
    result = {
        'statusCode': str(status_code),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }
    if body is not None:
        result['body'] = body

    return result


# Don't modify handler, make other functions feet it
def handler(event: dict, context):
    try:
        user_email = authenticate_user(event['headers'])
        notes = query_user_notes(user_email)
    except InvalidResponse as e:
        return build_response(status_code=e.status_code)
    else:
        return build_response(
            status_code=200,
            body=json.dumps(notes)
        )
