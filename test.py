from selenium import webdriver
from time import sleep
import tkinter,tkinter.font
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from get_oneway_love_follow_users import get_unfollow_users
 #----ログイン操作---
driver = webdriver.Chrome() # インスタンス作成
driver.maximize_window()    # 全画面表示

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
driver.get("https://www.instagram.com/{}/following/".format(profile_name))
sleep(8)

li = driver.find_element(By.CLASS_NAME,"_aano")
# 自動スクロール
scroll = 10
for i in range(int(scroll)): #スクロールさせたいかを入力 10スクロールで58人　100スクロールで580人　1000スクロールで5800人
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", li)
    sleep(random.randint(500,1000)/1000)

# # 操作できる画面の一覧を取得(Popup後に処理)
# handle_array = driver.window_handles

# print(handle_array)

sleep(2000)

