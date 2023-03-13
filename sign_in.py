import infos
import sys
import time
import requests
import json

token = infos.infos().get_token()
id = input("id\n")

# if shift_id == False:
#     sys.exit()
# elif shift_id == -2:
#     sys.exit()
# else:
#     print(shift_id, shifts.index(shift_id))

checktime = int(round(time.time()))
url = "https://open.feishu.cn/open-apis/attendance/v1/user_flows/batch_create?employee_type=employee_no"
payload = json.dumps({
	"flow_records": [
		{
			"check_time": str(checktime),
			"comment": "打卡",
			"creator_id": f"{id}",
			"location_name": "睿信书院社区",
			"user_id": f"{id}"
		}
	]
})


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer '+token
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)