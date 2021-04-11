from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
def show_entries():
    return render_template('entries/index.html')
    # entriesファイルにあるindex.html


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            # sessionを入れる
            session['logged_in'] = True
            flash('ログイン成功です！！')
            return redirect('/')
    return render_template('login.html')
# login.htmlで認証を行なっている


@app.route('/logout')
def logout():
    # ユーザー名とパスワードが合ってたときにセッション許可されたのを返却
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect('/')
