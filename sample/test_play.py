from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


"""
**********************************************************************
【要修正】設定値を編集
**********************************************************************
"""
username    = "coconara_check"  # ユーザー名
password    = "T2qYUgVR"   # パスワード
unfollownum = 4                 # フォロー解除する人数

"""
**********************************************************************
インスタグラム Topページ
**********************************************************************
"""
browser = webdriver.Chrome()
url = "https://www.instagram.com"
browser.get(url)
sleep(10)

"""
**********************************************************************
インスタグラム　ログイン
**********************************************************************
"""
# ログインフォームの要素取得
loginForm = browser.find_element(By.ID,"loginForm")

# ユーザー名入力
loginForm.find_element(By.NAME,"username").send_keys(username)

# パスワード
loginForm.find_element(By.NAME,"password").send_keys(password)

# ボタンクリック
btns = browser.find_elements(By.TAG_NAME,"button")
for i in btns:
    if i.text == 'Log In' or i.text == 'Log in':
        i.click()
        break
sleep(1000)

"""
**********************************************************************
インスタフォローページ
**********************************************************************
# """
# # 画面遷移
# browser.get("https://www.instagram.com/{}/following/".format(username))
# sleep(8)

# # フォローボタン一括取得
# following  = browser.find_element_by_class_name("_aano")
# followingbtns = following.find_elements_by_class_name("_acan._acap._acat")

# # フォロー解除数を定義
# if unfollownum > len(followingbtns):
#     unfollownum = len(followingbtns)

# # フォロー解除
# for i in range(unfollownum):
#     followingbtns[i].click()
#     sleep(1)
#     try:
#         unfollow = browser.find_element_by_class_name("_a9--._a9-_")
#         if unfollow.text == 'Unfollow':
#             unfollow.click()
#     except:
#         pass
#     sleep(1)
    
# print("{}人フォロー解除完了".format(unfollownum))