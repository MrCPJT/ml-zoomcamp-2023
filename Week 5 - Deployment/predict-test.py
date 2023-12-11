import requests

url = 'http://localhost:5000/predict'

customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 30,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}
response = requests.post(url, json=customer).json()
print(); print(response)

if response['churn'] == True:
    print('Sending promotional email to {0:}'.format('Customer ID'))
else:
    print('Not sending promotional email to {0:}'.format('Customer ID'))