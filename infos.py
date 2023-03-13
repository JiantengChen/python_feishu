import requests
import json
# 对应各个排班
ls = ["7124276719061647361",
      "7124277031717568513",
      "7124277390179647516",
      "7142397481077194753",
      "7162914877575528451",
      "7140187272372043779",
      "7140187707692515332",
      "7162916488477736988",
      "7162918275783933953",
      "7162918878983536641",
      "7162920398057226268",
      "0000000000000000000"]


class infos:

    def get_token(self) -> str:
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        param = {
            "app_id": "cli_a35d2d57b5b8500e",
            "app_secret": "JLdw1OwcTWeykjxyVdI7qhLOr84X5cqd"
        }
        r = requests.post(url, params=param)
        txt = json.loads(r.text)
        token = txt['tenant_access_token']
        return token

    def get_shift_id(self, shift_no: int) -> str:
        shift_id = ls[shift_no-1]
        return shift_id
