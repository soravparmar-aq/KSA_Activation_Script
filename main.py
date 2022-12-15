"""
Created on 2-Nov-2022
@author: sorav.parmar@airlinq.com

Script to Bulk activation API, an array of IMSI passed in activation api
and write imsi_from in config.

"""

# Import the required libraries and modules
import requests
import json
import urllib3
from config import api_url, imsi_from, batch_count, service_profile_id, api_token
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# configuration of logs
logging.basicConfig(filename='activation_api_info.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

# certificate and key for passing in request POST
clientCrt = "prod.airlinq.com.cer"
clientKey = "prod.airlinq.com.key"


def auth_api():
    """
    Method to generate auth token
    and write Auth token in
    config file
    """

    # Required parameters and Authentication
    data = 'grant_type=password&username=airlinqapiuser&password=Airlinq%402022'

    headers = {
        'Authorization': 'Basic QXRMMzFrUm45TXk0a2pxTXNhSjVidXRUZms2QUFmN1N5QjhrQk9iOjJHZXN1dzhHYWhHMElZOGs2cFQ4RUM4WjgyM2ZIWk1iMkJUSEE=',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'postman-token': 'f0053eb0-3981-d1c0-408f-d46ad5b05f6f'
    }

    response = requests.request("POST", api_url["api_url"], headers=headers,
                                data=data, cert=(clientCrt, clientKey))

    """
    If auth API Hit successfully ,
    then api_token is edit into the config file
    """
    if response.status_code == 200:
        auth_resp = json.loads(response.content)
        token = auth_resp["access_token"]

        with open('config.py', 'r') as file:
            filedata = file.read()

        filedata = filedata.replace(f'{api_token["api_token"]}', str(token))
        with open('config.py', 'w') as file:
            file.write(str(filedata))

        print(response.text)
    return token


def activation_api(token):
    """
    Method to execute bulk activation api using imsi_from
    :return:
    """
    # Auth API called everytime when script(activation api) is executed

    imsi_value_start = int(imsi_from["imsi_from"])

    # Empty array for storing imsi_from values
    results = []

    counter = batch_count["batch_count"]

    """
        Generating an array of imsi to be passed in activation api 
        and write last imsi in imsi_from 
        variable in config
    """
    for i in range(counter):
        imsi_value_start += 1
        results.append(imsi_value_start)
    print(results)

    last_value = results[-1]
    print('last value', last_value)
    # from config import api_token
    # token = api_token["api_token"]

    header = {
        'Authorization': "Bearer " + token,
        'Content-Type': 'application/json'
    }

    print(header["Authorization"])

    str_results = [str(x) for x in results]

    """
        Passing parameters in body like identifier 
        , simIds, serviceProfile
    """
    payload = json.dumps({
        "identifier": "IMSI",
        "simIds": str_results,
        "serviceProfile": service_profile_id["serviceProfile"]
    })
    # Activation API request sent
    resp = requests.request("POST", api_url["activated_sim_api_url"], headers=header,
                            data=payload, cert=(clientCrt, clientKey))
    """
        Storing logs values like imsi_from,
        batch_count, Activation_API_Response
    """
    logger.info(
        f'imsi_from : {imsi_from["imsi_from"]} batch_count : {batch_count["batch_count"]} Activation API Response : {resp}')

    print(resp.text)

    # If activation api is successfully , then edit imsi_from last value in config file
    if resp.status_code == 200:
        with open('config.py', 'r') as file:
            filedata = file.read()

        # write last value of imsi_from in config file
        filedata = filedata.replace(f'{imsi_from["imsi_from"]}', str(last_value))

        # Write the file out again
        with open('config.py', 'w') as file:
            file.write(str(filedata))


token = auth_api()
# calling the Activation API
activation_api(token)
