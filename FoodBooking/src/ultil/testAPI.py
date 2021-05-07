import requests

payload = """{"userName": "hotuhi",
               "password":"asdas",
               "fullName":"ho tu hi",
               "dateOfBirth":"12/12/2000",
               "major":"coder"}"""
url = "http://127.0.0.1:5000/user"
headers = {
    'Connection': "keep-alive",
    'Cache-Control': "max-age=0",
    'sec-ch-ua': "^\^Chromium^^;v=^\^88^^, ^\^Google",
    'Content-Type': "application/json"
}
res = requests.request("POST", url, data=payload, headers=headers)
print(res.text)
