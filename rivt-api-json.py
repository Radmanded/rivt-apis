import json


json_data = '''{
	"errorFlag": "N",
	"statusCode": "SUCCESS",
	"message": "SUCCESS",
	"entity": [
		[{
				"distiValRid": "639254",
				"distiValSoldTo": "24/7 NETWORKS, INC.",
				"partnerNameBeGeoName": company_name,
				"partnerName": "24/7 NETWORKS LLC",
				"address1": "116 INVERNESS DR E",
				"address2": "STE 200 ",
				"city": "ENGLEWOOD",
				"state": "CO",
				"postalCode": "80112",
				"country": "UNITED STATES",
				"partnerSiteID": "2910350",
				"partnerType": "VAR",
				"certification": "PREMIER",
				"certEffectiveStartDate": "27-FEB-2022",
				"certificationExpiryDate": "28-MAY-2023",
				"specialization": "AENAS[Until13-JAN-23],ASAS[Until29-DEC-22],CAS[Until21-NOV-22],CEES[Until20-APR-23],CESDC[Until10-OCT-23],DCAS[Until26-OCT-23]",
				"authorization": "ATTAB[Until14-NOV-21],COMCERT[Until25-APR-23],CPIA[Until12-NOV-68],CSAAS-AUTH[Until08-JUL-23],CSCS[Until07-JUL-09],CSPP[Until26-JAN-23],CTMP[Until12-NOV-68],Duo-CP[Until20-AUG-21],EA2_C1ACWN[Until10-JUN-23],EA2_C1DCCN[Until10-JUN-23],EA2_Secure[Until13-JUN-23],EA2_Spark[Until10-JUN-23],ETF[Until27-JUL-19],HYPRFLX[Until13-NOV-22],LCI[Until12-NOV-22],LCIAC[Until12-NOV-20],LCIAC-ACI[Until12-NOV-20],LCIAC-DNAC[Until12-NOV-68],LCIAC-TET[Until12-NOV-20],LCIAD[Until12-NOV-68],LCIAD-COL[Until12-NOV-68],LCIAD-DC[Until12-NOV-68],LCIAD-EA[Until12-NOV-68],LCIAD-EN[Until12-NOV-68],LCIAD-SEC[Until12-NOV-68],LCIU-COLAB[Until12-NOV-68],Meraki-CP[Until31-DEC-99],NFR-std[Until12-NOV-68],NFR1[Until31-JUL-27],NFRSAAS_B[Until12-NOV-68],OIPTIP[Until12-NOV-68],PP_FY18_BR[Until27-OCT-18],PP_FY20_BR[Until25-JAN-20],PP_US_PRT4[Until28-JUL-18],PP_US_SVT4[Until28-JUL-18],REGISTERED[Until26-JAN-23],RESL_HOST[Until10-JUN-23],RWD-US[Until31-JUL-20],SRP[Until12-NOV-68],SS_ACI[Until27-JUL-30],SS_DNA[Until27-JUL-30],TAB[Until14-NOV-21],UCATAB[Until14-NOV-21],VIP31-NBAB[Until26-JAN-20],VIP33-NBAB[Until30-JAN-21],VIP40-COLL[Until28-JAN-23],VIP40-DC[Until28-JAN-23],VIP40-DCA[Until28-JAN-23],VIP40-EN[Until28-JAN-23],VIP40-ENA[Until28-JAN-23],VIP40-IOT[Until28-JAN-23],VIP40-IOTA[Until28-JAN-23],VIP40-MER[Until28-JAN-23],VIP40-MERA[Until28-JAN-23],VIP40-SEC[Until28-JAN-23],VIP40-SECA[Until28-JAN-23],VIP40COLLA[Until28-JAN-23]",
				"registrationStatus": "REGISTERED",
				"regEffectiveStartDate": "27-JAN-2022",
				"registrationExpiryDate": "26-JAN-2023",
				"phoneNumber": "3039912224",
				"website": "www.247networks.com"
			},
			{
				"distiValRid": "639255",
				"distiValSoldTo": "247 NETWORKS INC",
				"partnerNameBeGeoName": "24/7 NETWORKS LLC",
				"partnerName": "24/7 NETWORKS LLC",
				"address1": "116 INVERNESS DR E",
				"address2": "STE 200 ",
				"city": "ENGLEWOOD",
				"state": "CO",
				"postalCode": "80112",
				"country": "UNITED STATES",
				"partnerSiteID": "2910350",
				"partnerType": "VAR",
				"certification": "PREMIER",
				"certEffectiveStartDate": "27-FEB-2022",
				"certificationExpiryDate": "28-MAY-2023",
				"specialization": "AENAS[Until13-JAN-23],ASAS[Until29-DEC-22],CAS[Until21-NOV-22],CEES[Until20-APR-23],CESDC[Until10-OCT-23],DCAS[Until26-OCT-23]",
				"authorization": "ATTAB[Until14-NOV-21],COMCERT[Until25-APR-23],CPIA[Until12-NOV-68],CSAAS-AUTH[Until08-JUL-23],CSCS[Until07-JUL-09],CSPP[Until26-JAN-23],CTMP[Until12-NOV-68],Duo-CP[Until20-AUG-21],EA2_C1ACWN[Until10-JUN-23],EA2_C1DCCN[Until10-JUN-23],EA2_Secure[Until13-JUN-23],EA2_Spark[Until10-JUN-23],ETF[Until27-JUL-19],HYPRFLX[Until13-NOV-22],LCI[Until12-NOV-22],LCIAC[Until12-NOV-20],LCIAC-ACI[Until12-NOV-20],LCIAC-DNAC[Until12-NOV-68],LCIAC-TET[Until12-NOV-20],LCIAD[Until12-NOV-68],LCIAD-COL[Until12-NOV-68],LCIAD-DC[Until12-NOV-68],LCIAD-EA[Until12-NOV-68],LCIAD-EN[Until12-NOV-68],LCIAD-SEC[Until12-NOV-68],LCIU-COLAB[Until12-NOV-68],Meraki-CP[Until31-DEC-99],NFR-std[Until12-NOV-68],NFR1[Until31-JUL-27],NFRSAAS_B[Until12-NOV-68],OIPTIP[Until12-NOV-68],PP_FY18_BR[Until27-OCT-18],PP_FY20_BR[Until25-JAN-20],PP_US_PRT4[Until28-JUL-18],PP_US_SVT4[Until28-JUL-18],REGISTERED[Until26-JAN-23],RESL_HOST[Until10-JUN-23],RWD-US[Until31-JUL-20],SRP[Until12-NOV-68],SS_ACI[Until27-JUL-30],SS_DNA[Until27-JUL-30],TAB[Until14-NOV-21],UCATAB[Until14-NOV-21],VIP31-NBAB[Until26-JAN-20],VIP33-NBAB[Until30-JAN-21],VIP40-COLL[Until28-JAN-23],VIP40-DC[Until28-JAN-23],VIP40-DCA[Until28-JAN-23],VIP40-EN[Until28-JAN-23],VIP40-ENA[Until28-JAN-23],VIP40-IOT[Until28-JAN-23],VIP40-IOTA[Until28-JAN-23],VIP40-MER[Until28-JAN-23],VIP40-MERA[Until28-JAN-23],VIP40-SEC[Until28-JAN-23],VIP40-SECA[Until28-JAN-23],VIP40COLLA[Until28-JAN-23]",
				"registrationStatus": "REGISTERED",
				"regEffectiveStartDate": "27-JAN-2022",
				"registrationExpiryDate": "26-JAN-2023",
				"phoneNumber": "3039912224",
				"website": "www.247networks.com"
			}
		]
	],
	"totalItems": "2",
	"success": true
}
'''

#loads the json data into a python dictionary
data = json.loads(json_data)

# input company name to search for in the json data and returns the company data if found else returns None if not found
def search_company(company_name):
	for company in data['entity']:
		for partner in company[0]:
			if partner['partnerNameBeGeoName'] == company_name:
				return partner



#prints the company data if found else prints None if not found
def print_company(company_name):
    company = search_company(company_name)
    if company is None:
        print('Company not found')
    else:
        print(company)

def main():

#input company name to search for in the json data and prints the company data if found else prints None if not found
    company_name = input('Enter company name: ')
    print_company(company_name)

if __name__ == '__main__':
    main()




# Return companies certification results for a given company name and certification type (e.g. PREMIER) and returns the company data if found else returns None if not found

'''
# query the dictionary for the company name
for item in data['items']

print(data['entity'][0][0]['partnerNameBeGeoName'], data['entity'][0][0]['certification'] )
print(data['entity'][0][0]['partnerNameBeGeoName'], data['entity'][0][0]['specialization'] )



for i in data['entity']:
    for j in i:
        print(j['partnerNameBeGeoName'], j['certification'])
        print(j['partnerNameBeGeoName'], j['specialization'])

'''


