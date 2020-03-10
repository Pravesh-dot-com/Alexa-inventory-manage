# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 00:24:36 2020

@author: Pravesh
"""

import uuid
import requests
import json


def make_api_call(method, url, token, payload = None, parameters = None):
    # Send these headers with all API calls
    headers = { 'User-Agent' : 'testing1.0',
              'Authorization' : 'Bearer {0}'.format(token),
              'Accept' : 'application/json' }
    
    # Use these headers to instrument calls. Makes it easier
    # to correlate requests and responses in case of problems
    # and is a recommended best practice.
    request_id = str(uuid.uuid4())
    instrumentation = { 'client-request-id' : request_id,
                      'return-client-request-id' : 'true' }
    
    headers.update(instrumentation)
    
    response = None

    if (method.upper() == 'GET'):
        response = requests.get(url, headers = headers, params = parameters)
    elif (method.upper() == 'POST'):
        headers.update({ 'Content-Type' : 'application/json' })
        response = requests.post(url, headers = headers, data = json.dumps(payload), params = parameters)
    
    return response

tok = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjgzMWJiZTJlLTcwMjQtNDY0ZS04YmZkLTEyYmI2YjhlYTEzNiIsImV4cCI6MTU4Mzg3MjAyNSwiaWF0IjoxNTgzODcxNzI1LCJuYmYiOjE1ODM4NzE3MjUsInByaXZhdGVDbGFpbXMiOnsiY29udGV4dCI6IkFBQUFBQUFBQVFBVlIyMGlWZlk4NENsZVJRdFd2L3VtS1FFQUFBQUFBQUFsejh1UGpLMjJHOHFDTTAyWnY5b1htWTBPK3JkSi81b29SWkJ3K1UrUHdSc1p4MUpnSUZWNVo1MHNjN3EzcC9sNGp0TEttbDlPYUxtV2NvUFMzNXIzYzAwZzVYMk1DUzhHVGw5TXZyZVZLK2Z6dDZscFdOMkJKWUVvTWRxb3JiK1piL1diZ3dhQk9lMUI0NjJhT21YTW9vUE1LTjF4WFF2RktueVd5SE55MEZJWjQ5UnpUMExGVFJWNTByVzAyeE5jWWF3UkhiU2VjY0JScC9NQi9sNGxaWWRtYWE4YS9KM1l2clMzeXA1MXVTKzFSd0x3N2txZGdhbUF2WUlDZlk5TlNJWlVSVVRHdk1oeVpjbElJUk9rUzBwK0FUODdmcllEVW4xTkltUkJ4bzR1ZUI5dXZvODRCN1hYOHA2eTJjb1lCcVFEdmkzZ281V0ZYQVZQL0RMVHpvMWF0bGVyV2gzejU1eW5rZWEvRldNWjVDZVF6cG9xMjNaV0lvNCtHSzdscFR6UmliN2FZUzQ9IiwiY29uc2VudFRva2VuIjoiQXR6YXxJd0VCSURtNjc0dEM5cVc4RHRLdjVyMzR2cHBCNWpQeUV1ck1tVWVjX1Byb29GdVpHOHJOaGpKOWxJRDNfTk14RzBYNHlvT3ZubGFJTmtXZTZybHhYa0tCTmVNLXJ4T0ladE5zbWQzdGM0NDVhelc4TThDcFF6MUhlSUhPaFdBOWt5TC1uOWNFU3EyUDdpM3l2TzNmS2dfZGQwLUVYbFNHVG53UUNUa251bGNBVlJBMTIyZDBUQnhiMW5oUHFtX0ZfN1NLU292NzlHVXFNWXJmM1AwOEx5aEZ0Vk5zbTh1bUh0UzBKQVZxejJGcnhvVHdibTRXWHZaUk0xd29JeGZWdVBQX2FEc2h6TU1KV1VRdTNvOENpbElHVUF0VlBxT1FCektlR1c3Y1F3WWFPYzNKcDJBaHJ4cmNCUGlwWjkzZHUxcktBOHNqVmd1dnEwZ1dRbWU4cjRLblJma3dlYVZYamp2ZW02SW5JRVVqS3BzYmhvVWZNRjRJTm5KSDV3VU9PaVU2OTZTTjJ5OVhyTnRrdzZFcGdEcklhc3R5dS1oenEwRVNlYTc1bno1Q0ZhbHBxUnJqU0VNeWJORUZCbWZxX0NuVHN5NnV3RlN3dkVLSHN5cHNyWVJmR0w5OTFqLTJRcFhyWjQ4TXNONDdHcEJpbXhTR0lGVHBHT3lWRGdKYnZaZUhfRzAiLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUhQRk9CSllYTVhKTjRJQkw1M1NQM09QVjVCWEg3UVA1VjU3S1VMMzM3N0VYVkVTTUdTUFVHRVRONlhNUldLRk9QRkdUUFZGRUpPNkJZNElRVVhXNlVBSExNTDRRQlFNNEVGU1BVNVpOT1pURklRTkVQSEVRMzRSMzdaWEIySllBTVVSRVhURzQ2WkVCUEZUVE01REhQUjJVRExONE9INkUzM0I3VjdRQU1VVURaRzM1QjRRTyIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFIM1NMRFVOWkVPNjZVSERRV1RDUzdWNUNFU0Y1UFA3RzRGVU1HNzNFTzI1UE1WTzNaR1lIUVRWV09JM1VKRzJZUkFMV1VMUU9EVzNNUUJTSUtPU0s3QlE0QU4yV1U2M1NKVE1QTUY0UU5OWDdDTUFLWUxTSlBXWjJBMjVGQjRDQ1dHV1BLSjQzU0tDU0lESVdMU0xUQ0xDNjVISEtNVjVDM1hHWTVXQkxPTkZONTNRV09WSEhQRldNWlhBQjdaQldES0lLS0gyNjRFRjRBSSJ9fQ.Hi-q-BddZiVMl3HFNFJMgRvO9dCRsEHha0P-UerTiM7VYgsuLZC1UJ6AyPmNwny68mc3e2jshFoEjtflfUHMBh_gOUygctsEr8baB_IS6iELNczmpjsNSq4U_PqcWLlMgXp_6PA9oqDqcDl-_1o4TYXIE6YEhCk3WkP-4IAM9icbVpavMW8xgaqMjWehApqtvU01cvrWhXff0BF6r1E8pVU-G-EhqI4uiJ8MLpuKYCHx81gSxwi-l9-1ofeXJD0vn1ab3fid3PSU8iRhjwW-uAXZswyTlJnNmTq7LPMd5pdj-_qPK4ra29ZSqupGT6vWGcVt0ZxCRKC0n7X2vZsvXg"




subject = ' Alexa Passcode Test outlook 2'
user_mail = '172343@nttdata.com'
content_type = "Text"
recipient_list = [{'EmailAddress': {'Address': user_mail}}]
body = ' This is att testing '

base_url = 'https://graph.microsoft.com/v1.0/me/{}'#sendMail'
send_url = base_url.format('sendMail')
get_url = base_url.format('mailfolders/inbox/messages')


#send_passcode_payload  = {'Message': {'Subject': subject, 'Body': {'ContentType': content_type, 'Content': body}, 'ToRecipients': recipient_list},'SaveToSentItems': 'true'}

query_parameters_get = {'$top': '1', '$select': 'receivedDateTime,subject,from, body', '$orderby': 'receivedDateTime DESC'}

#send_mail_response = make_api_call('POST', send_passcode_url, tok, payload = send_passcode_payload)

r = make_api_call('GET', get_url, tok ,parameters = query_parameters_get )

data = json.loads(r.content)



att_url = base_url.format('messages/{}/attachments')
mid = 'AAMkAGExM2M3OGFmLTQ5MWItNDc3MS1hZTM3LTVkNmQ2MTFlOGU5NgBGAAAAAAAK-7BOTnYARoPcqyIr9E2xBwDn2p1HfBBXTIihouz1KukzAAAAAAEMAADn2p1HfBBXTIihouz1KukzAAFHFc4pAAA='
aid = 'AAMkAGExM2M3OGFmLTQ5MWItNDc3MS1hZTM3LTVkNmQ2MTFlOGU5NgBGAAAAAAAK-7BOTnYARoPcqyIr9E2xBwDn2p1HfBBXTIihouz1KukzAAAAAAEMAADn2p1HfBBXTIihouz1KukzAAFHFc4pAAABEgAQAAvJwZ3w1lZCkJxZandGnxc='

att_url = att_url.format(mid)#, aid)

query_parameters_att = { '$expand' : 'attachments' }

r = make_api_call('GET', att_url, tok)# ,parameters = query_parameters_att)

data = json.loads(r.content)

att_data = data['value'][0]['contentBytes']

import base64

#base64String = "data:application/pdf;base64,JVBERi0xLjQKJeHp69MKMSAwIG9iago8PC9Qcm9kdWNlciAoU2tpYS9..."

dec_att = base64.b64decode(att_data)


with open('temp.xlsx', 'wb') as theFile:
  theFile.write(base64.b64decode(att_data))
  
  



