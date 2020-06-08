import csv
import requests

response = requests.get('https://nepalcorona.info/api/v1/data/nepal')
json_response = response.json()
print(json_response['tested_positive'])
data = [1, json_response['tested_positive'], json_response['tested_negative'], json_response['tested_total'],
        json_response['in_isolation'], json_response['quarantined'], json_response['tested_rdt'],
        json_response['pending_result'], json_response['recovered'], json_response['deaths']]

with open('nepal_detail.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ["SN", "Tested Positive", "Tested Negative", "Tested Total", "In Isolation", "Quarantined", "Tested RDT",
         "Pending Results", "Recovered", "Death"])
    writer.writerow(data)
