import json
import base64

def msk_handler(event, context):
    for key in event['records']:
        data = event['records'][key]
        for value in data:
            topic_data = base64.b64decode(value['value'])
            return topic_data
