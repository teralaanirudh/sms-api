
import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'IPVH1SPMZVB01RSVYSY6XEN5ZXVBP99N', 'TSM698ARKNLTK2A4', 'stage', '6281000675', 'evaditey nik enti', 'Your a/c no.XXXXXXXX0245 is Credited for Rs. 500 on 16-05-2020' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print (response.text)
