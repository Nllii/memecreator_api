# public account:
from json import dump
import requests
import pprint
import json


def get_account(Access_Token,page_number,account_id,user_id,viewer_account_id,viewer_user_id):
    cookies = {
    }

    headers = {
        'Accept': '*/*',
        'AccessToken': Access_Token,
        'User-Agent': 'Meme Creator/11.2.5 (iPhone; iOS 14.0; Scale/3.00)',
        'Accept-Language': 'en-US;q=1',
        'AccountId': '2815489',
        'Accept-Encoding': 'gzip, deflate, br',
        'AppVersion': '11.2.5',
    }

    params = (
        ('account_id', account_id),
        ('page', page_number),
        ('user_id', user_id),
        ('viewer_account_id', viewer_account_id),
        ('viewer_user_id',viewer_user_id),
    )

    response = requests.get('https://memecreatorapi.com/api/meme-server/v3/users/get_public.php', headers=headers, params=params, cookies=cookies)
    rep = response.json()
    # pprint.pprint(response.json())
    return rep






def Remove_userVotes(Access_Token, meme_id, account_id):
    cookies = {
    }

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'AccessToken': Access_Token,
        'User-Agent': 'Meme Creator/11.2.5 (iPhone; iOS 14.0; Scale/3.00)',
        'Accept-Language': 'en-US;q=1',
        'AccountId': '_replace_me',
        'Accept-Encoding': 'gzip, deflate, br',
        'AppVersion': '11.2.5',
    }

    data = '{"account_id":"_replace_me","meme_id":"_replace_me"}'
    dump_data = json.dumps(data)
    response = requests.post('https://memecreatorapi.com/api/meme-server/v3/memes/remove_vote.php', headers=headers, cookies=cookies, data=dump_data)
    # rep = response.json()
    pprint.pprint(response.json())