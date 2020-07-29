# encoding = 'utf-8'
# author = 'jessica'
import requests
import json


class HttpClient(object):
    def __init__(self):
        pass

    def __post(self, url, data=None, json=None, **kwargs):
        response = requests.post(url=url, data=data, json=json)  # 只要这3个参数，其他的不要
        return response

    def __get(self, url, params=None, **kwargs):
        response = requests.get(url=url, params=params)
        return response

    def request(self, method, url, params_type, request_data=None, headers=None):
        if method.lower() == 'post':
            if params_type == 'form':
                response = self.__post(url=url, data=request_data, headers=headers)
                return response
            elif params_type == 'json':
                response = self.__post(url=url, json=request_data, headers=headers)
                return response
        elif method.lower() == 'get':
            if params_type == 'url':
                url = url + request_data
                response = self.__get(url=url, headers=headers)
                return response
            elif params_type == 'params':
                response = self.__get(url=url, params=request_data, headers=headers)
                return response


if __name__ == '__main__':
    hc = HttpClient()
    url = 'https://ap8.salesforce.com/services/oauth2/token?'
    username = 'jessica.test@dev.com'
    password = 'passwordtest'
    client_id = '3MVG9pe2TCoA1Pf5rH8DfBl9d2fFp8HjLb_qT2kinLYayyZW0ROHTrQH44dsrveZRkrVGOC9tST2MfmcGPY6s'
    client_secret = 'FC5F7F6836001F41055D7A83AF3B282A3C2C1A8C3E1B1EBDA3BD17CABEFE4C53'
    data = {
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password
    }
    response = hc.request(method='post', url=url, params_type='form', request_data=data)
    print(response.status_code)
    print(response.text)
