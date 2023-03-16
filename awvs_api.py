import json
import time
from datetime import datetime

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

tarurl = "https://localhost:3443"
apikey = "1986ad8c0a5b3df4d7028d5f3c06e936cdc6aa4f2e08c49f0bc2cd907066d8e05"
headers = {"X-Auth": apikey, "Content-type": "application/json;charset=utf8"}


# 查看所有目标结果
def targets():
    api_url = tarurl + '/api/v1/targets'
    r = requests.get(url=api_url, headers=headers, verify=False)
    print(r.json())


# 添加targets目标，获取target_id
def post_targets(url):
    api_url = tarurl + '/api/v1/targets'
    data = {
        "address": url,
        "description": "wyt_target",
        "criticality": "10"
    }
    data_json = json.dumps(data)
    r = requests.post(url=api_url, headers=headers, data=data_json, verify=False)
    target_id = r.json().get("target_id")
    print('target_id:', target_id)
    return target_id


# 添加scans
def scans(url):
    api_url = tarurl + '/api/v1/scans'
    data = {
        "target_id": url,
        "profile_id": "11111111-1111-1111-1111-111111111112",
        "schedule":
            {"disable": False,
             "start_date": None,
             "time_sensitive": False
             }
    }
    data_json = json.dumps(data)
    r = requests.post(url=api_url, headers=headers, data=data_json, verify=False)
    # target_id = r.json().get("target_id")
    # print(r.json)


# 获取scan_id，通过start_date可知，最新生成的为第一个
def scan_id():
    api_url = tarurl + '/api/v1/scans'
    # print(api_url)
    r = requests.get(url=api_url, headers=headers, verify=False)
    scan_id = r.json().get("scans")[0].get("scan_id")
    print('scan_id:', scan_id)
    return scan_id


# 添加generate，并获取generate_id
def generate(url):
    api_url = tarurl + '/api/v1/reports'
    data = {
        "template_id": "11111111-1111-1111-1111-111111111115",
        "source": {
            "list_type": "scans",
            "id_list": [url]
        }
    }
    data_json = json.dumps(data)
    r = requests.post(url=api_url, headers=headers, data=data_json, verify=False)
    # print(r.json)


# 生成扫描报告,每次新生成的都在第一个
def html():
    api_url = tarurl + '/api/v1/reports'
    # print(api_url)
    r = requests.get(url=api_url, headers=headers, verify=False)
    html = r.json().get("reports")[0].get("download")[0]

    url_html = tarurl + html
    print('报告地址：', url_html)
    r_html = requests.get(url=url_html, headers=headers, verify=False)

    time_now = datetime.now().strftime('%Y-%m-%d %H%M%S')
    with open("report-" + time_now + ".html", "wb") as code:
        code.write(r_html.content)
        code.close()


def pdf():
    api_url = tarurl + '/api/v1/reports'
    # print(api_url)
    r = requests.get(url=api_url, headers=headers, verify=False)
    pdf = r.json().get("reports")[0].get("download")[1]

    url_pdf = tarurl + pdf
    print('报告地址：', url_pdf)
    r_html = requests.get(url=url_pdf, headers=headers, verify=False)

    time_now = datetime.now().strftime('%Y-%m-%d %H%M%S')
    with open("report-" + time_now + ".pdf", "wb") as code:
        code.write(r_html.content)
        code.close()


if __name__ == '__main__':
    # targets()
    # 添加到targets队列
    target_id = post_targets("http://8.8.8.8/")
    time.sleep(5)

    # 添加到scans队列
    scans(target_id)
    time.sleep(5)

    # 获取scan_id,并生成generate
    scan_id = scan_id()
    generate(scan_id)
    time.sleep(5)

    # 生成扫描报告
    # pdf()
    html()
