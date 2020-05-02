import requests
#爬取银行验证码
def get(num, url, path, headers):
    i = 0
    while i<num:
        picture = requests.get(url, headers = headers)
        with open(path+'code'+str(i)+'.jpg', 'wb') as f:
            f.write(picture.content)
        i = i+1

url = "https://epass.icbc.com.cn/servlet/com.icbc.inbs.person.servlet.Verifyimage2?disFlag=2&randomKey=1580537733595658615&width=70&height=28&appendRandom=1580537819345"
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
num = 10000
path = "C:\\Users\\Lenovo\\Desktop\\graduation design\\code\\"
get(num, url, path, headers)