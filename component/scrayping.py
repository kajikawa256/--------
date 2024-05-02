from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def auto_operation(id, password):
  # Chrome Webドライバー の インスタンスを生成
  driver = webdriver.Chrome()

  # ウィンドウを全画面にする
  driver.maximize_window()

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

  # プロフィール画面へ遷移
  driver.get(f"https://www.instagram.com/{id}/")
  # 3秒待機
  time.sleep(5)

  driver.get(f"https://www.instagram.com/{id}/following/")
  driver.refresh()
  # driver.find_element(By.XPATH,'//*[@id="mount_0_0_Ti"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section[3]/ul/li[2]/a').click()

  # フォローユーザ一覧を取得
  # users_raw_data = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div")

  # print(users_raw_data.text)


  time.sleep(1000)