from selenium import webdriver
from time import sleep
import tkinter,tkinter.font
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from get_oneway_love_follow_users import get_unfollow_users

#----ログイン操作---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")    # ウィンドウを最大化
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36") # User-Agentの設定
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

# 片思いフォロー中のユーザIDリスト(filterd_list)とフォロー中のユーザ数(following_num)を取得
filterd_list,following_num = get_unfollow_users(profile_name,password)


#---フォロー解除処理---
# プロフィール画面へ遷移
driver.get(f"https://www.instagram.com/{profile_name}/following/")
sleep(8)


# 自動スクロール
scroll = following_num / 5 # スクロール数を自動で計算
li = driver.find_element(By.CLASS_NAME,"_aano")
for i in range(int(scroll)): # スクロール数を入力 10スクロールで58人　100スクロールで580人　1000スクロールで5800人
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", li)
    sleep(random.randint(1000,10000)/1000) # 1~10秒のランダム秒数間隔でスクロール


# フォローボタン一括取得
following  = driver.find_element(By.CLASS_NAME,"_aano")
followingbtns = following.find_elements(By.CLASS_NAME,"_acan._acap._acat")
user_names = following.find_elements(By.CLASS_NAME,"_ap3a")


# filterd_listと一致した行のフォロー中ボタンをクリックし、フォローを解除する
index = 0
for name in user_names:
  if name.text in "フォロー中":
    continue
  if name.text in filterd_list:
    # followingbtns[index].click()                                        # フォロー中クリック
    # unfollow = driver.find_element(By.CLASS_NAME,"_a9--._a9-_").click() # フォローをやめるクリック
    print(name.text)
    sleep(3)
  index+=1


sleep(2000)

