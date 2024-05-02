import instaloader


id = ""
password = ""

#インスタグラムにログイン
loader = instaloader.Instaloader()
loader.login(id, password)

#指定したIDのprofileオブジェクトを作成
profile = instaloader.Profile.from_username(loader.context,id)#id:フォロワーを取得したいアカウントのユーザーID

#指定したIDのフォロワーを全件取得
followers = profile.get_followers()
# 指定したIDのフォロー中を全件取得
following = profile.get_followees()

# リストに変換
follow = [follower.username for follower in followers]   # フォロワー
followed = [follower.username for follower in following] # フォロー中

print(len(follow))
print(len(followed))

