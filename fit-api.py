# import requests

# url = "https://v1.nocodeapi.com/vaibhavr42/fit/McsSKrXlnsaKjLFm/aggregatesDatasets?dataTypeName=steps_count&timePeriod=today&durationTime=hourly"
# params = {}
# r = requests.get(url = url, params = params)
# result = r.json()
# print(result)

import requests

url = "https://v1.nocodeapi.com/vaibhavr42/fit/McsSKrXlnsaKjLFm/aggregatesDatasets?dataTypeName=steps_count&timePeriod=today&durationTime=hourly"
params = {}
r = requests.get(url = url, params = params)
result = r.json()

# Extract the step count value from the JSON response
steps = result['steps_count'][0]['value']

print(steps) # Output: 3272
# import requests

# url = "https://v1.nocodeapi.com/vaibhavr42/fit/McsSKrXlnsaKjLFm/aggregatesDatasets?dataTypeName=weight&timePeriod=today"
# params = {}
# r = requests.get(url = url, params = params)
# result = r.json()
# weightt=result['weight'][0]['value']
# print(weightt)
