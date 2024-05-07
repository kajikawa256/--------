from selenium import webdriver
from time import sleep
import tkinter,tkinter.font
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from get_oneway_love_follow_users import get_unfollow_users

 #----ログイン操作---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # ウィンドウを最大化
# options.add_argument("--headless")         # ヘッドレスモードで実行

driver = webdriver.Chrome(options=options) # オプションを設定し、インスタンス作成


profile_name = "coconara_check"
password = "T2qYUgVR"

#instagramにアクセス
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)
sleep(1)
#ログインID・PWを入力
elem_search_word = driver.find_element(By.NAME,"username")
elem_search_word.send_keys(profile_name)
sleep(3)
ppassword= driver.find_element(By.NAME,'password')
ppassword.send_keys(password)
sleep(2)
ppassword.send_keys(Keys.ENTER)
sleep(4)

# # 片思いフォロー中のユーザIDを取得
# filterd_list = get_unfollow_users(profile_name,password)
# # 片思いフォロー中のユーザIDを表示
# print(filterd_list)


#---フォロー解除処理---
# プロフィール画面へ遷移
driver.get(f"https://www.instagram.com/{profile_name}/following/")
sleep(5)

li = driver.find_element(By.CLASS_NAME,"_aano")
# 自動スクロール
scroll = 10
for i in range(int(scroll)): #スクロールさせたいかを入力 10スクロールで58人　100スクロールで580人　1000スクロールで5800人
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", li)
    sleep(random.randint(500,1000)/1000)

# フォローボタン一括取得
following  = driver.find_element(By.CLASS_NAME,"_aano")
followingbtns = following.find_elements(By.CLASS_NAME,"_acan._acap._acat")

print(len(followingbtns))

sleep(2000)

