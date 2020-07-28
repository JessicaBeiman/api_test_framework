# encoding = 'utf-8'
# author = 'jessica'
import requests
import json

# login Salesforce
username = 'jessica.test@dev.com'
password = 'G00djob123'
host = 'https://ap8.salesforce.com'  # 访问REST接口域名不要设置成lightning的，切换成classic才能访问，否则会报找不到接口。
grant_service = '/services/oauth2/token?grant_type=password'
client_id = '3MVG9pe2TCoA1Pf5rH8DfBl9d2fFp8HjLb_qT2kinLYayyZW0ROHTrQH44dsrveZRkrVGOC9tST2MfmcGPY6s'
client_secret = 'FC5F7F6836001F41055D7A83AF3B282A3C2C1A8C3E1B1EBDA3BD17CABEFE4C53'
login_url = host + grant_service +\
           '&client_id=' + client_id +\
           '&client_secret=' + client_secret + \
           '&username=' + username + \
           '&password=' + password
response = requests.request('post', login_url)
print('response status code: ', response.status_code)
if response.status_code == 200:  # 200 "OK" success code, for GET or HEAD request.
    json_str = response.json()
    access_token = json_str.get('access_token')
    token_type = json_str.get('token_type')

# New an Account record
uri = '/services/data/v48.0/sobjects/Account'
headers = {
    "Authorization": token_type + ' ' + access_token,
    "Content-Type": 'application/json'
}
data = json.dumps({"Name": "jessicatest20200728"})
response = requests.request(method='post', url=host + uri, headers=headers, data=data)
print(response.status_code)
if response.status_code == 201:  # 201 "Created" success code, for POST request.
    print(response.json())
    account_id = response.json().get('id')

# Get the Account record
uri = '/services/data/v48.0/sobjects/Account/id/' + account_id
headers = {
    "Authorization": token_type + ' ' + access_token,
    "Content-Type": 'application/json'
}
response = requests.request(method='get', url=host + uri, headers=headers)
print(response.status_code)
if response.status_code == 200:
    print(response.json())

# Edit the Account record
uri = '/services/data/v48.0/sobjects/Account/' + account_id
headers = {
    "Authorization": token_type + ' ' + access_token,
    "Content-Type": 'application/json'
}
data = json.dumps({"Name": "jessicatest20200728update"})
response = requests.request(method='patch', url=host + uri, headers=headers, data=data)
print(response.status_code)
if response.status_code == 204:  # 204 "No Content" success code, for DELETE request.
    print('Account is updated successfully.')

# Query updated account record
soql_query = f"SELECT Id, Name FROM Account WHERE Id = '{account_id}'"
uri = '/services/data/v48.0/query/?q=' + soql_query
print('uri: ', uri)
headers = {
    "Authorization": token_type + ' ' + access_token,
    "Content-Type": 'application/json'
}
response = requests.request(method='get', url=host + uri, headers=headers)
print(response.status_code)
if response.status_code == 200:
    print(response.json())
    if response.json().get('records')[0].get('Name') == 'jessicatest20200728update':
        print('Account is really updated.')

# Delete the Account record
uri = '/services/data/v48.0/sobjects/Account/' + account_id
headers = {
    "Authorization": token_type + ' ' + access_token,
    "Content-Type": 'application/json'
}
response = requests.request(method='delete', url=host + uri, headers=headers)
print(response.status_code)
if response.status_code == 204:  # 204 "No Content" success code, for DELETE request.
    print('Account is deleted successfully.')
