from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#
# 2024/05/02 時点で動作確認済み
# 
# 【機能】instagramのログインユーザID、パスワード、揺らぎの感覚、フォロー解除人数の取得を行う
#

def unfolow_users(id, password, users_list):
  # Chrome Webドライバー の インスタンスを生成
  driver = webdriver.Chrome()

  # ウィンドウを全画面にする
  driver.maximize_window()

  #
  # instagramログインここから
  #
  # Webドライバーでインスタログインページを起動
  driver.get('https://www.instagram.com/')
  # NAME属性が”username”であるHTML要素を取得し、値をキーボード送信
  driver.find_element(By.NAME,"username").send_keys(id)
  # NAME属性が”password”であるHTML要素を取得し、パスワード文字列をキーボード送信
  driver.find_element(By.NAME,"password").send_keys(password)
  # CLASS属性が”ControlID-3”であるHTML要素を取得してクリック
  Xpath = '//*[@id="loginForm"]/div/div[3]/button'
  driver.find_element(By.XPATH,Xpath).click()
  # 3秒待機
  time.sleep(5)
  #
  # instagramログインここまで
  #


  # 画面遷移
  driver.get("https://www.instagram.com/{}/following/".format(id))
  time.sleep(8)

  # フォローボタン一括取得
  following  = driver.find_element(By.CLASS_NAME,"_aano")
  followingbtns = following.find_elements(By.CLASS_NAME,"_acan._acap._acat")


  unfollownum = 4

  # フォロー解除数を定義
  if unfollownum > len(followingbtns):
      unfollownum = len(followingbtns)

  # フォロー解除
  for i in range(unfollownum):
      followingbtns[i].click()
      time.sleep(1)
      try:
          unfollow = driver.find_element(By.CLASS_NAME,"_a9--._a9-_")
          if unfollow.text == 'Unfollow':
              unfollow.click()
      except:
          pass
      time.sleep(1)

  # for user in users_list:
  #   driver.get(f"https://www.instagram.com/{user}/")
  #   time.sleep(5)
  #   driver.find_element(By.XPATH,'//*[@id="mount_0_0_nz"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div/div[1]/button').click()
  #   time.sleep(5)
  #   driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[1]/div/div').click()

  time.sleep(1000)