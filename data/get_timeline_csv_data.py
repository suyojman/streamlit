import csv
import requests

response2 = requests.get('https://data.nepalcorona.info/api/v1/covid/timeline')
json_response2 = response2.json()

print('Converting.........')
with open('nepal_timeline.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ["SN", "Date", "Total Cases", "New Cases", "Total recoveries", "New Recoveries", "Total Death", "New Death"])
    for index, data in enumerate(json_response2, 1):
        writer.writerow(
            [index, data['date'], data['totalCases'], data['newCases'], data['totalRecoveries'], data['newRecoveries'],
             data['totalDeaths'], data['newDeaths']])
print('Done!!')
