from flask import Flask, render_template

app = Flask(__name__)

# 定义主页路由
@app.route('/')
def index():
    return render_template('index.html')

# 定义播放页面路由
@app.route('/play')
def play():
    return render_template('play.html')

# 运行Flask应用程序
if __name__ == '__main__':
    app.run(debug=True)
