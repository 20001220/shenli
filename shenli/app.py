from config import *
from forest import *
from user import *
from conflagration import *  # 这4行引入了该项目其他几个文件


@app.route('/')
def helloflask():
    return render_template('forestdenglu.html')  # 启动时跳入到该模板


# trees.sql可以用来生成这个项目的数据库
# forestdenglu.html

if __name__ == '__main__':  # 整个项目的入口
    app.run(host='127.0.1.4', port=5500, debug=True)  # 可以设置ip和端口号等等
