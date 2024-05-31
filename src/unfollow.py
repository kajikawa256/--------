from selenium import webdriver
from time import sleep
import tkinter,tkinter.font
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from get_oneway_love_follow_users import get_unfollow_users
# 2024/05/28 追加
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# --------------login_process-----------------
def button_click():

    profile_name= input_profile_name.get()  # id
    password= input_password.get()          # password
    interval = int(time_interval.get())     # 揺らぎの間隔
    nums = int(unfollow_nums.get())         # フォロー解除人数
    operation_kind = mode_var.get()         # 半自動か全自動


    #----ログイン操作---
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")    # ウィンドウを最大化
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36") # User-Agentの設定
    # options.add_argument("--headless")         # ヘッドレスモードで実行


    driver = webdriver.Chrome(options=options) # オプションを設定し、インスタンス作成


    #instagramにアクセス
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(random.randint(3000,5000)/1000)
    #ログインID・PWを入力
    elem_search_word = driver.find_element(By.NAME,"username")
    elem_search_word.send_keys(profile_name)
    sleep(random.randint(4000,6000)/1000)
    ppassword= driver.find_element(By.NAME,'password')
    ppassword.send_keys(password)
    sleep(random.randint(3500,7000)/1000)
    ppassword.send_keys(Keys.ENTER)
    sleep(random.randint(3000,4200)/1000)


    #---フォロー解除処理---
    # 片思いフォロー中のユーザIDリスト(filterd_list)とフォロー中のユーザ数(following_num)を取得
    print("ユーザリスト取得中...")
    try:
        filterd_list,following_num = get_unfollow_users(profile_name,password)
    except:
        print("ユーザリスト取得エラー")
        print("しばらく時間をおいてから再度お試しください")
        sleep(10)
        # driverの開放
        driver.close()
        # tkinterの終了
        root.destroy()
        exit()
    print("取得完了")


    # プロフィール画面へ遷移
    driver.get(f"https://www.instagram.com/{profile_name}/")


    # 全自動と半自動で処理を分ける
    if operation_kind in "全自動":
        # 全自動
        # フォロー画面表示
        driver.get(f"https://www.instagram.com/{profile_name}/following/")
    else:
        # 半自動
        input("フォロー中の欄を開いてください、準備ができたらEnterキーを押してください...")


    # 自動スクロール
    scroll = following_num / 5 # スクロール数を自動で計算
    sleep(random.randint(5200,8020)/1000)
    try:
        li = driver.find_element(By.CLASS_NAME,"_aano")
        for i in range(int(scroll)): # スクロール数を入力 10スクロールで58人　100スクロールで580人　1000スクロールで5800人
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", li)
            sleep(random.randint(1000,10000)/1000) # 1~10秒のランダム秒数間隔でスクロール
    except:
        print("---------------------------")
        print("ユーザ読み込みエラー")
        print("半自動で再度お試しください")
        print("---------------------------")
        sleep(10)
        # driverの開放
        driver.close()
        # tkinterの終了
        root.destroy()
        exit()


    # フォローボタン一括取得
    following  = driver.find_element(By.CLASS_NAME,"_aano")
    followingbtns = following.find_elements(By.CLASS_NAME,"_acan._acap._acat")
    user_names = following.find_elements(By.CLASS_NAME,"_ap3a")


    # filterd_listと一致した行のフォロー中ボタンをクリックし、フォローを解除する
    index = 0
    unfollow_nums_count = 0 # フォロー解除した人数
    for name in user_names:
        if name.text in "フォロー中":
            continue
        if name.text in filterd_list:
            followingbtns[index].click()                             # フォロー中クリック
            sleep(random.randint(3000,10000)/1000)
            driver.find_element(By.CLASS_NAME,"_a9--._a9-_").click() # フォローをやめるクリック
            sleep(random.randint(3000,10000)/1000 + interval)
            unfollow_nums_count+=1  # フォロー解除した人数を+1

        index+=1

        # 解除した人数が指定した人数になればループ抜ける
        if nums == unfollow_nums_count:
            print(f"{unfollow_nums_count}人のユーザをフォロー解除しました")
            break


    # 終了処理
    print("エラーなし　処理を終了します。")
    sleep(10)
    # driverの開放
    driver.close()
    # tkinterの終了
    root.destroy()




#-----------------以下tkinter(画面描画)の処理-------------------#
# ウインドウの作成
root = tkinter.Tk()
root.title("インスタ自動フォロー解除ツール")
root.geometry("300x150")

font = tkinter.font.Font(
    root, size=10
)

# ID label
input_profile_name_label = tkinter.Label(text="ID", font=font)
input_profile_name_label.grid(row=1, column=1, padx=10)

# input_ID
input_profile_name = tkinter.Entry(width=20)
input_profile_name.grid(row=1, column=2)

# PASSWORD
input_password_label = tkinter.Label(text="PASS")
input_password_label.grid(row=2, column=1, padx=10)

# PASWORD欄の作成
input_password = tkinter.Entry(show="*", width=20)
input_password.grid(row=2, column=2)

# フォロー解除人数
unfollow_nums_label = tkinter.Label(text="フォロー解除人数")
unfollow_nums_label.grid(row=3, column=1, padx=10)

# フォロー解除人数欄の作成
unfollow_nums = tkinter.Entry(width=20)
unfollow_nums.grid(row=3, column=2)

# 揺らぎの間隔
time_interval_label = tkinter.Label(text="揺らぎの間隔(秒単位)")
time_interval_label.grid(row=4, column=1, padx=10)

# 揺らぎの間隔欄の作成
time_interval = tkinter.Entry(width=20)
time_interval.grid(row=4, column=2)

# ラジオボタンの状態を保持するための変数
mode_var = tkinter.StringVar(value="全自動")

# 全自動ラジオボタン
radio_auto = tkinter.Radiobutton(root, text="全自動", variable=mode_var, value="全自動")
radio_auto.grid(row=5, column=1, pady=10)

# 半自動ラジオボタン
radio_semi_auto = tkinter.Radiobutton(root, text="半自動", variable=mode_var, value="半自動")
radio_semi_auto.grid(row=5, column=2, pady=10)

#ボタンの作成
button = tkinter.Button(text="実行",command=button_click)
button.place(x=250, y=100)

# ウインドウの描画
root.mainloop()