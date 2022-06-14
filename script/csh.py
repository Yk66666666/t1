import json


def csh():
    js_path = "../data/login.json"
    a = []
    with open(js_path,encoding='utf-8') as f:
        result = json.load(f)

        for i in result:
            username = i.get('username')
            password = i.get('password')
            verify_code = i.get('verify_code')
            Content_Type = i.get('Content_Type')
            status = i.get('status')
            status_code = i.get('status_code')
            msg = i.get('msg')
            a.append((username,password,verify_code,Content_Type,status,status_code,msg))
    return a

