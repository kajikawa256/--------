import instaloader

#
# 2024/05/02 時点で動作確認済み
# パスワードが簡単すぎると、instagram側でbotチェック作動がするのでエラーが起きる場合がある
# 【機能】idとパスワードを使ってinstagramにログインし、片思いフォローユーザのIDとフォロー中のユーザID数をリスト形式でreturnする
#

def get_unfollow_users(id, password):


  # インスタグラムにログイン
  loader = instaloader.Instaloader()
  try:
    loader.login(id, password)
  except:
    print("---------------------------")
    print("アカウント認証エラー")
    print("時間が経ってから再度お試しください")
    print("---------------------------")
    exit()

  # 指定したIDのprofileオブジェクトを作成
  profile = instaloader.Profile.from_username(loader.context,id)#id:フォロワーを取得したいアカウントのユーザーID

  # 指定したIDのフォロワーを全件取得
  followers = profile.get_followers()
  # 指定したIDのフォロー中を全件取得
  following = profile.get_followees()

  # リストに変換
  follower = [follower.username for follower in followers]   # フォロワー
  followed = [follower.username for follower in following]   # フォロー中

  # 片思いフォローユーザIDの取得 (フォロー中のユーザリストからフォロワーをフィルタリング)
  filterd_list =  [x for x in followed if x not in follower]

  return filterd_list,len(followed)
