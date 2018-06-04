from selenium import webdriver
import secret
from selenium.webdriver import DesiredCapabilities
import requests
import json

login_url = "http://150.95.147.189:8000/login"
correct_url = "http://150.95.147.189:8000/admin/correct_keys/1"
hook_url = secret.hook_url
user = secret.user
password = secret.password

# loginをする関数
def login(url):
    browser.get(url)
    id = browser.find_element_by_id("name-input")
    id.clear()
    id.send_keys(user)
    passwd = browser.find_element_by_id("password-input")
    passwd.clear()
    passwd.send_keys(password)

    # send form
    frm = browser.find_element_by_id("submit")
    frm.submit()
    print("Login WebPage")

# 前回の確認時から更新されたか、確認


# ctfdから回答されたリストを取得
def scriping_data():
    browser.get(correct_url)
    browser.save_screenshot("aaa.png")
    # idの一番上のものをとってくる
    id = browser.find_element_by_xpath('//*[@id="teamsboard"]/tbody/tr[1]/td[1]')
    with open("/web/data.json", "r") as f:
        old_id = f.read()
    if int(id.text) > int(old_id):
        content = ''
        for i in range(1, int(id.text)-int(old_id)+1):
            challenge = browser.find_element_by_xpath('//*[@id="teamsboard"]/tbody/tr[' + str(i)  + ']/td[3]')
            team = browser.find_element_by_xpath('//*[@id="teamsboard"]/tbody/tr[' + str(i)  + ']/td[2]/a')
            content += team.text + "によって、" +  challenge.text + "が解かれました!!\n"
            with open("/web/data.json", "w") as f:
                f.write(id.text)
    else:
        print("No person get flag")
        browser.quit()
        exit(1)

    browser.quit()
    return content

# slackにWebhookを用いて、投稿
def push_slack(content):
    payload = {"text": content}
    r = requests.post(hook_url, data = json.dumps(payload))
    print(r.status_code)


options = webdriver.ChromeOptions() 
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('--headless') 
browser = webdriver.Chrome(chrome_options=options)
browser.implicitly_wait(3)

login(login_url)
content = scriping_data()
push_slack(content)
