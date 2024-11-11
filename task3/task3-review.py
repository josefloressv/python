import json
import re
from boto3.dynamodb.conditions import Key
import boto3


class InvalidResponse(Exception):
    def __init__(self, status_code):
        self.status_code = status_code


def query_user_notes(user_email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user-notes')
    response = table.query(
        KeyConditionExpression=Key('user').eq(user_email),
        Limit=10,
        ScanIndexForward=False
    )
    items = response.get('Items', [])
    notes = []
    for item in items:
        note = {
            'id': item['id'],
            'create_date': item['create_date'],
            'text': item['text']
        }
        notes.append(note)
    return notes


def get_authenticated_user_email(token):
    if not token or not token.startswith('Bearer '):
        raise InvalidResponse(403)

    token = token.split(' ')[1]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('token-email-lookup')
    response = table.get_item(
        Key={
            'token': token
        }
    )
    item = response.get('Item', {})
    if not item:
        raise InvalidResponse(403)
    email = item.get('email')
    if not email:
        raise InvalidResponse(403)
    return email


def authenticate_user(headers):
    if 'Authentication' not in headers:
        raise InvalidResponse(400)
    authentication_header = headers['Authentication']
    user_email = get_authenticated_user_email(authentication_header)
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
        result['body'] = json.dumps(body)
    return result


def handler(event, context):
    try:
        user_email = authenticate_user(event['headers'])
        notes = query_user_notes(user_email)
    except InvalidResponse as e:
        return build_response(status_code=e.status_code)
    else:
        return build_response(status_code=200, body=notes)
