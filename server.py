from flask_blog import app

if __name__ == '__main__':
  app.run(debug=True)


#サーバーそのものだと思って良い
#ここを起動させることによって、アプリケーションの変数を持ってきて、そのアプリケーションを動かす。
#__name__とアプリケーションが等しい時に実行する
