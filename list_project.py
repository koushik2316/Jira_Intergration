# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://demo03437.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0NyiDiwEKgG77nBIMDl1nnWqK2N5WGX2p869lNHscGP8cyVv4dWIKs2ipjV6qOCrP_mOvcposhUTikTxzPclw_vSAAkhm-zhCjjaoTYwGGFcW6hsUXY4B-eDVTfP2hRvFWfMOKVtcYM325erUCCdpQUYoaorSOyVPkLQqT0HBK0A=2A47753B"
auth = HTTPBasicAuth("demo03437@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output=json.loads(response.text)

name=output[0]["name"]
name=output[1]["name"]
print(name)
