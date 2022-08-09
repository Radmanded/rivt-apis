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
  'Cookie': 'a79f8307c5db34ee3f6ffd933dd657a9=bbafdea3f4a8e5b5450320700f656451; d9c4bd7d7cdfdd17f7f220ce2c1d6546=3bd8e4cf58f23dd67066f9e5cd4cb59a'
}

response = requests.request("POST", url, headers=headers, data=payload)

my_response = json.loads(payload,  )


print(f'partnerNameBeGeoName: {my_response["entity"][0]["partnerName"]}, certifications: {my_response["entity"][0]["certification"]}')

# ToDo: Print out Every partnerNameBeGeoName,certification returned in the object

# Output:
# 24/7 NETWORKS LLC,REGISTERED
# 24/7 NETWORKS LLC,PREMIER

Current Output:
partnerNameBeGeoName: 24/7 NETWORKS LLC, certifications:

# Parse data for specific key;value pair

# partner_list = []
# # Start the iteration cycle
# for partner in my_response["entity"]:
#     # "item" is each individual dictionary, so do an if check to see if the "price" key is 2.25
#     if partner["partnerNameBeGeoName"] == 'True':
#         # If so, append it to the list called item_list
#         partner_list.append(partner["id"])
# # print the item_list to console
# print(partner_list)