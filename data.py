import requests

parameters = {
    "amount": 10,
    "type":  "boolean",
}

#https://www.freeformatter.com/html-escape.html#before-output - HTML freeformatter
# better to import HTML module in quiz_brain.
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


