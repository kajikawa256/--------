# DEMO

https://github.com/kajikawa256/Instagram_Auto_Operation/assets/87938576/5cddaac2-d0ad-476c-9c8b-75661439234a


 
# Features
 
「Instagram_Auto_Operation」は片思いフォロー中のユーザのフォローを自動で解除するツールです。
片思いフォローとは、自身はフォローしているが相手からフォローバックされていない状態の事を指します。
各動作の間に乱数で生成した秒数分待機時間を作ることで、BOTチェックに引っかからないよう工夫しています。
 
# Requirement
* Python 3.11.1
* selenium 4.20.0

 
# Installation
 
seleniumのインストール方法
 
```bash
pip install selenium
```
 
# Usage
 

 
```bash
git clone https://github.com/kajikawa256/Instagram_Auto_Operation
python src/unfollow.py
```
 
# Note

 * インスタグラムアカウントのパスワードが短いと、安全性（bot）チェックが入るのでうまく動作しない場合がある。
 * 2段階認証をオフにしないとうまく動作しない場合がある。
 * プログラム起動時、別Windowを開くとうまく動作しない場合があるのでプログラムが動作したらPCを触らない。
 * 10回ほど時間を空けず連続で起動すると認証エラーが発生する場合があるので注意。
 * フォロー解除人数が多すぎるとスパムアカウント扱いされて、アカウントの停止になる恐れがあるので20人程度を推奨。
 * 環境によってはうまく動作しない可能性もある。
 * バージョンアップにより使用できなくなるおそれあり。
 * いかなる不具合や不利益が被った場合でも、一切の責任を負わない。

# Author
 
作成情報を列挙する
 
* Shousei Kajikawa
* 2003/06/19
 
# License
著作権フリー
