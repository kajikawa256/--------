import component.auto_operation
import component.get_oneway_love_follow_users as setup



filterd_list = setup()
print(filterd_list)

# 情報入力のためのwindow描画
# # 片思いフォロワーのユーザIDリスト取得

# # idとパスワードを指定して、片思いフォロー中のアカウントのフォローを外す
# component.auto_operation.unfolow_users(id, password, users_list)