import requests
import json

url = "https://wsgx.cisco.com/wwchannels/services/external/getData"

payload = json.dumps({
  "service": "getRessellerData",
  "ccoId": "rubend@synnex.com",
  "profileId": "975",
  "entity": [
    {
      "sourceName": "COMSTOR",
      "resellerAccNo": "",
      "soldToName": "",
      "partnerName": "24/7 NETWORKS LLC",
      "city": "",
      "state": "",
      "postalCode": "",
      "country": "USA",
      "specialization": "",
      "certification": "",
      "authorization": "",
      "theaterCode": "USA",
      "partnerType": "",
      "partnerSiteid": "",
      "pageNumber": 1,
      "pageSize": 50
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGlzdGlfc2VydmljZXMuZ2VuOkQhc3RyaWJ1dDFu',
}

response = requests.request("POST", url, headers=headers, data=payload)

my_response = json.loads(payload,  )

print(my_response)
#print(f'partnerNameBeGeoName: {my_response["entity"][0]["partnerName"]}, country: {my_response["entity"][0]["country"]}')

# ToDo: Print out Every partnerNameBeGeoName,certification returned in the object

# Output:
# 24/7 NETWORKS LLC,REGISTERED
# 24/7 NETWORKS LLC,PREMIER

# Current Output:
# partnerNameBeGeoName: 24/7 NETWORKS LLC, certifications:

# Parse data for specific key;value pair

