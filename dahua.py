import json
import requests
from requests.auth import HTTPDigestAuth

xml="""<PTZData>
        <pan>120</pan>
        <tilt>0</tilt>
        <zoom>0</zoom>
    </PTZData>"""

xml1="""<PTZData>
        <pan>0</pan>
        <tilt>0</tilt>
        <zoom>0</zoom>
    </PTZData>"""

print('start')

query_args = {
    "method":"global.login",
    "params":{"userName":"admin","password":"","clientType":"Web3.0","loginType":"Direct"},
    "id":1
    }



#res = requests.get("http://109.253.2.3:8080/custom_lang/English.txt?version-170",auth=HTTPDigestAuth("admin","admin123"));
#res = requests.get("http://109.253.2.3:8080/RPC2_Login",auth=HTTPDigestAuth("admin","admin123"));
res = requests.post("http://109.253.2.3:8080/RPC2_Login",
                   auth=requests.auth.HTTPDigestAuth("admin","admin123"),
                     data=json.dumps(query_args))


print(res)

session = res.json()['session']

print(session)

global_auth_args = {
    "method":"global.login",
    "params": {
        "userName":"admin",
        "password":"F7C0FFA7643D5944AB67D308B808BB73",
        "clientType":"Web3.0",
        "loginType":"Direct",
        "authorityType":"Default"
        },
        "id":2,
        "session":session
        }

res1 = requests.post("http://109.253.2.3:8080/RPC2_Login",
                   auth=requests.auth.HTTPDigestAuth("admin","admin123"),
                     data=json.dumps(global_auth_args))
print(res1)
print(res1.text)

list_query_args = {
  "method":"mediaFileFind.findNextFile",
  "params":{"count":13},
  "id":2,
  "session":session,
  "object":1782976600
  }

res2 = requests.post("http://109.253.2.3:8080/RPC2",
                    auth=requests.auth.HTTPDigestAuth("admin","admin123"),
                    data=json.dumps(list_query_args))

#res = requests.put("http://192.168.1.64/ISAPI/PTZCtrl/channels/1/continuous",data=xml1)
#res = requests.get("http://109.253.2.3:8080")
print(res2)
print(res2.text)