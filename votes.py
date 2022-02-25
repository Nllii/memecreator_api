import binascii
import os
import requests
import json
from get_public_Account import get_account
import time

def encode_multipart_formdata(fields):
    boundary = binascii.hexlify(os.urandom(16)).decode('ascii')

    body = (
        "".join("--Boundary+%s\r\n"
            
                "Content-Disposition: form-data; name=\"%s\"\r\n"
                "\r\n"
                "%s\r\n" % (boundary, field, value)
                for field, value in fields.items()) +
        "--Boundary+%s--\r\n" % boundary
        
    )

    content_type = "multipart/form-data; boundary=Boundary+%s" % boundary
    print(content_type)

    return body, content_type





def vote(zero_down_1_upvote,id):
    file_ = encode_multipart_formdata({
    "account_id": "",
    "location": "user_public_memes",
    "user_id": "",
    f"votes[{id}]": zero_down_1_upvote })
    body, content_type = file_

    cookies = {
    }

    headers = {
        'Accept': '*/*',
        'Content-Type': content_type,
        'AccountId': '',
        'AccessToken': '',
        'User-Agent': 'Meme Creator/11.2.5 (iPhone; iOS 14.0; Scale/3.00)',
        'Accept-Language': 'en-US;q=1',
        'Content-Length': '398',
        'Accept-Encoding': 'gzip, deflate, br',
        'AppVersion': '11.2.5',
    }
    # dum_header = json.dumps(headers)

    response = requests.post('https://memecreatorapi.com/api/meme-server/v3/memes/vote.php', headers=headers, data = body, cookies=cookies)
    print(response.text)
    # return response.text
    # response = response.text



def cast_vote():
    upvote_ = 1
    downvote_ = 0
    for page_ in range(0,1000):

        print(int(page_))
        time.sleep(1)
        id = get_account(page_number=page_)  
        for ids in id:
            meme_ids = ids['id']
            # time.sleep(1)
            vote(downvote_,meme_ids)
            # if no_respon == []:
            #     break
            # else:
            #     continue



# cast_vote()


def remove_votes():
    pass

# https://julien.danjou.info/handling-multipart-form-data-python/
