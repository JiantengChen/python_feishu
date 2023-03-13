import requests
import json
import infos
import datetime
token = infos.infos().get_token()
url = "https://open.feishu.cn/open-apis/attendance/v1/user_daily_shifts/query?employee_type=employee_no"
date = eval(datetime.datetime.now().strftime("%Y%m%d"))
user_id = input("请输入该同学学号\n")
payload = json.dumps({
    "check_date_from": date,
    "check_date_to": date,
    "user_ids": [
        user_id
    ]
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
}
response = requests.request("POST", url, headers=headers, data=payload)
txt = json.loads(response.text)

class employee_shift:
    def judge(self):
        try:
            shift_id = txt['data']['user_daily_shifts'][0]['shift_id']
            if shift_id == "":
                print("NoShiftError")
                return False
            elif shift_id == "0":
                print("Rest")
                return -2  # rest
            else:
                return shift_id
        except:
            if txt['code'] == 0:
                print("NotArrange")
            else:
                print(txt['code'])
            return False
                
