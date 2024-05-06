from selenium import webdriver
from time import sleep
import tkinter,tkinter.font
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from component.get_oneway_love_follow_users import get_unfollow_users


#区切り線#
split_line = "-" * 50
global liker
global liker_list
file_path = "profile_list.txt"


# --------------login_process-----------------
def button_click():

    profile_name= input_profile_name.get()  # id
    password= input_password.get()          # password
    interval = int(time_interval.get())          # 揺らぎの間隔
    nums = unfollow_nums.get()              # フォロー解除人数

    driver = webdriver.Chrome() # インスタンス作成
    driver.maximize_window()    # 全画面表示


    #----ログイン操作---

    #instagramにアクセス
    driver.get("https://www.instagram.com/accounts/login/")
    driver.implicitly_wait(10)
    sleep(1)
    #ログインID・PWを入力
    elem_search_word = driver.find_element(By.NAME,"username")
    elem_search_word.send_keys(profile_name)
    sleep(1)
    ppassword= driver.find_element(By.NAME,'password')
    ppassword.send_keys(password)
    sleep(1)
    ppassword.send_keys(Keys.ENTER)
    sleep(4)

    # 片思いフォロー中のユーザIDを取得
    filterd_list = get_unfollow_users(profile_name,password)
    # 片思いフォロー中のユーザIDを表示
    print(filterd_list)

    # # ユーザのページにいちいちアクセスする方式
    # for x in filterd_list:
    #     driver.get(f"https://www.instagram.com/{x}/")
    #     sleep(5)
    #     driver.find_element(By.CLASS_NAME," _acan _acap _acat _aj1- _ap30").click()
    #     sleep(3)
    #     driver.find_element(By.CLASS_NAME, "x1i10hfl").click()
    #     sleep(3)


    #---フォロー解除処理---
    # プロフィール画面へ遷移
    driver.get("https://www.instagram.com/{}/following/".format(profile_name))
    sleep(8)


    # フォローボタン一括取得
    following  = driver.find_element(By.CLASS_NAME,"_aano")
    followingbtns = following.find_elements(By.CLASS_NAME,"_acan._acap._acat")

    print(len(followingbtns))

    # フォロー解除数を定義
    if int(nums) > len(followingbtns):
        nums = len(followingbtns)

    # フォロー解除
    for i in range(int(nums)):
        followingbtns[i].click()
        sleep(3)
        try:
            unfollow = driver.find_element(By.CLASS_NAME,"_a9--")
            unfollow.click()
            sleep(interval)
        except:
            sleep(interval)
            pass

    scroll = 10

    li = driver.find_element(By.CSS_SELECTOR,"div.isgrP")
    # 自動スクロール
    for i in range(int(scroll)): #スクロールさせたいかを入力 10スクロールで58人　100スクロールで580人　1000スクロールで5800人
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", li)
        sleep(random.randint(500,1000)/1000)

    # フォローボタン一括取得
    following  = driver.find_element(By.CLASS_NAME,"_aano")
    followingbtns = following.find_elements(By.CLASS_NAME,"_acan._acap._acat")

    print(len(followingbtns))


    # followingbtns[0].click()
    # sleep(3)
    # driver.find_element(By.CLASS_NAME,"_a9--").click()

    print("{}人フォロー解除完了".format(nums))
    # sleep(1000)
    # for x in filterd_list:
    #     url = f'https://www.instagram.com/{x}/'
    #     driver.get(url)
    #     sleep(5)
    #     driver.find_element(By.CLASS_NAME,' _acan _acap _acat _aj1- _ap30').click()
    #     sleep(5)
    #     driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[1]/div/div').click()

    driver.close()




#-----------------以下tkinter(画面描画)の処理-------------------#

#ウインドウの作成
root = tkinter.Tk()
root.title("インスタ自動フォロー解除ツール")
root.geometry("300x150")


font=tkinter.font.Font(
    root,size =10
)


# ID label
input_profile_name_label = tkinter.Label(text="ID" ,font=font)
input_profile_name_label.grid(row=1, column=1, padx=10,)

# input_ID
input_profile_name = tkinter.Entry(width=20)
input_profile_name.grid(row=1, column=2)


# PASSWORD
input_password_label = tkinter.Label(text="PASS")
input_password_label.grid(row=2, column=1, padx=10,)

# PASWORD欄の作成
input_password = tkinter.Entry(show="*",width=20)
input_password.grid(row=2, column=2)


# フォロー解除人数
unfollow_nums_label = tkinter.Label(text="フォロー解除人数")
unfollow_nums_label.grid(row=3, column=1, padx=10,)

# フォロー解除人数欄の作成
unfollow_nums = tkinter.Entry(width=20)
unfollow_nums.grid(row=3, column=2)


# 揺らぎの間隔
time_interval_lavel = tkinter.Label(text="揺らぎの間隔(秒単位)")
time_interval_lavel.grid(row=4, column=1, padx=10,)

# 揺らぎの間隔欄の作成
time_interval = tkinter.Entry(width=20)
time_interval.grid(row=4, column=2)


#ボタンの作成
button = tkinter.Button(text="実行",command=button_click)
button.place(x=250, y=100)

#ウインドウの描画
root.mainloop()