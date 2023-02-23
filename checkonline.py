# import requests
# url = "http://192.168.50.3:8080/"

# request_response = requests.head(url)
# status_code = request_response.status_code
# website_is_up = status_code == 200
# def checkonline():
    # import requests
    # url = "http://103.82.249.178:8080/"
    # count = 0
    # try:
    #     website_is_up = requests.head(url).status_code == 200
    #     return True
    # except:
    #     return False
# import urllib3

import socket

def internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        # print(ex)
        return False

while True:
    print(internet())


