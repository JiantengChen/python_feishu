import requests
import json
import infos
token = infos.infos().get_token()
url = "https://open.feishu.cn/open-apis/attendance/v1/shifts"
payload = ''


headers = {
  'Authorization': 'Bearer '+ token
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)