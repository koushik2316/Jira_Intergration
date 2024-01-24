# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://demo03437.atlassian.net/rest/api/3/issue"

API_TOKEN="ATATT3xFfGF0NyiDiwEKgG77nBIMDl1nnWqK2N5WGX2p869lNHscGP8cyVv4dWIKs2ipjV6qOCrP_mOvcposhUTikTxzPclw_vSAAkhm-zhCjjaoTYwGGFcW6hsUXY4B-eDVTfP2hRvFWfMOKVtcYM325erUCCdpQUYoaorSOyVPkLQqT0HBK0A=2A47753B"
auth = HTTPBasicAuth("demo03437@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "First jira.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   "issuetype": {
      "id": "10007"
    },
    "project": {
      "key": "MYP"
    },
    "summary": "My_jira testing",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))