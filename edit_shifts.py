import requests
import json
url = "https://open.feishu.cn/open-apis/attendance/v1/user_daily_shifts/batch_create?employee_type=employee_no"
import infos
token = infos.infos().get_token()
operator_id = eval(input("请输入操作人学号\n"))
user_id = input("请输入该同学学号\n")
month = input("请输入两位数月份\n")
day_no = eval(input("日期\n"))
shift_no = input(
    "请输入值班类型\n1.上午值班\n2.下午值班\n3.晚上值班\n4.全天值班\n5.中午值班\n6.上午下午值班\n7下午晚上值班\n8.上午晚上值班\n9.中午晚上值班\n10.中午下午值班\n11.上午中午值班\n12.休息\n")
shift_no = int(shift_no)
shift_id = infos.infos().get_shift_id(shift_no)
payload = json.dumps({
    "operator_id": operator_id,
    "user_daily_shifts": [
        {
            "day_no": day_no,
            "group_id": "7124275834562609156",
            "month": int("2023"+month),
            "shift_id": shift_id,
                        "user_id": user_id
        }
    ]
})


headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+token
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
