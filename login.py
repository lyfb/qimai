import requests
import time
from urllib.request import urlretrieve
from PIL import Image
import execjs
from urllib.parse import urlencode

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.qimai.cn',
    'Referer': 'https://www.qimai.cn/account/signin/r/%2Frank%2Findex%2Fbrand%2Ffree%2Fcountry%2Fcn%2Fgenre%2F5000%2Fdevice%2Fiphone',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

def get_verifyCode():
    timestamp = int(time.time() * 1000)
    verifyCode_url = f'https://api.qimai.cn/account/getVerifyCodeImage?{timestamp}'
    urlretrieve(verifyCode_url, 'captcha.png')
    captcha = Image.open('captcha.png')
    captcha.show()
    verify_code = input('请输入验证码>> ')
    return verify_code

def get_synct():
    resp = requests.get('https://www.qimai.cn/rank', headers=headers)
    cookies = resp.cookies.get_dict()
    synct = cookies.get('synct')
    print(synct)
    return synct

def get_analysis(synct):
    with open('./qimai/analysis.js', 'rb') as f:
        js = f.read().decode()
    ctx = execjs.compile(js)
    analysis = ctx.call('getLoginAnalysis', synct)
    print(analysis)
    return analysis

def login():
    synct = get_synct()
    url = 'https://api.qimai.cn/account/signinForm?'
    params = {
        'analysis': get_analysis(synct)
    }
    data = {
        'username': input('请输入账号>> '),
        'password': input('请输入密码>> '),
        'code': get_verifyCode()
    }
    login_url = url + urlencode(params)
    print(login_url)
    r = requests.post(login_url, data=data, headers=headers)
    if r.json()['code'] == 10000:
        print(r.json()['msg'])
        cookies = r.cookies.get_dict()
        return cookies

if __name__ == '__main__':
    cookies = login()
    print(cookies)