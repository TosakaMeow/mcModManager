import os
import re
import json

import requests


def getModList():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    url = "此处填写MOD列表"
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    t = re.findall('<br>(.*?)</br>', str(r.text))
    return t

with open("./setting.json",'r', encoding='utf-8') as load_f:
  gamePath = json.load(load_f)



path = gamePath["gamePath"] + "/.minecraft/mods"
print(path)


def localModList():
    F = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # print file.decode('gbk')    #文件名中有中文字符时转码
            if os.path.splitext(file)[1] == '.jar':
                t = os.path.splitext(file)[0]
                F.append(t)  # 将所有的文件名添加到L列表中
    return F  # 返回L列表


serverModList = getModList()

print(serverModList)
print(localModList())

for i in serverModList:
    if i in localModList():
        print("存在mod，无需下载")
    else:
        print("正在下载MOD:", i)
        fileName = str(i) + ".jar"
        url = "http://" + fileName  # 填写下载源
        storgePath = path + "/" + fileName
        r = requests.get(url)
        with open(storgePath, "wb") as code:
            code.write(r.content)
