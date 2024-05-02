# tkintertのインポート
import tkinter as tk
from tkinter import ttk


root = tk.Tk() # tkinterのメインウィンドウの作成
root.title("事前情報入力")    # タイトル
root.geometry("640x360")  # 初期画面サイズ(width x height)
root.maxsize(650, 370)    # 画面最大サイズ(width, height)
root.minsize(650, 370)    # 最小画面サイズ(width, height)


# ウィジェットと説明の情報をリストで定義
widgets_info = [
    ("Button", "クリック可能なボタンです。"),
    ("Label", "テキストや画像を表示するためのウィジェットです。"),
    ("Entry", "1行のテキスト入力フィールドです。"),
    ("Checkbutton", "チェックボックスです。"),
    ("Menubutton", "ボタンを押すと選択肢が表示されます。"),
    ("Radiobutton", "ラジオボタンです。"),
    ("Scale", "スライダーバーです。"),
    ("Scrollbar", "スクロールバーです。"),
    ("Spinbox", "スピンボックスです。数値を入力するためのボックスです。")
]





###  Frameはdivみたいな感じ?  ###
# 見出し用フレーム
head_frame = tk.Frame(root)
head_frame.pack()

# メインフレーム
main_frame = tk.Frame(root)
main_frame.pack()

# pack() に引数を記述しない場合は、中央配置・パディング（隙間）無しで配置されます。
head_frame.pack(side="top", padx=10, pady=10)

tk.Label(head_frame, text="ヘッダー", font=("", 18, "")).pack()
head_frame.pack()


# ウィジェットを配置
tk.Button(main_frame, text="Button").grid(row=0, column=1, padx=5, pady=5, sticky="w")
tk.Label(main_frame, text="Label").grid(row=1, column=1, padx=5, pady=5, sticky="w")
tk.Entry(main_frame).grid(row=2, column=1, padx=5, pady=5, sticky="w")
tk.Checkbutton(main_frame).grid(row=3, column=1, padx=5, pady=5, sticky="w")
ttk.Menubutton(main_frame, text="Menubutton").grid(row=4, column=1, padx=5, pady=5, sticky="w")
ttk.Radiobutton(main_frame).grid(row=5, column=1, padx=5, pady=5, sticky="w")
ttk.Scale(main_frame).grid(row=6, column=1, padx=5, pady=5, sticky="w")
ttk.Scrollbar(main_frame).grid(row=7, column=1, padx=5, pady=5, sticky="w")
ttk.Spinbox(main_frame).grid(row=8, column=1, padx=5, pady=5, sticky="w")

# 説明を配置
for i, (_, description) in enumerate(widgets_info):
    tk.Label(main_frame, text=description, wraplength=300, justify="left").grid(row=i, column=2, padx=5, pady=5, sticky="w")

root.mainloop()

root.mainloop() # メインループの作成