import json
import typing

import requests

from src import config

TG_API_URL = 'https://api.telegram.org/bot'

def create_tg_post(attachments: typing.List[str], post_text: str) -> None:
    """
    Create a telegram post via vk post's attachments
    """
    url = TG_API_URL + config.TG_TOKEN
    params = {'chat_id': config.TG_CHANNEL}

    if len(attachments) == 0:
        url += '/sendMessage'
        params.update(text=post_text)
    elif len(attachments) == 1:
        url += '/sendPhoto'
        params.update(caption=post_text, photo=attachments[0])
    else:
        url += '/sendMediaGroup'

        media_params = []
        count = 0
        for attach in attachments:
            count += 1
            media_params.append({
                'type': 'photo',
                'media': attach,
                'caption': post_text if count == 1 else ''
            })

        params.update({'media': json.dumps(media_params)})

    resp = requests.post(url, params=params).json()
    if not resp['ok']:
        raise Exception(f'TG API Error: {resp}')
        
    return resp
