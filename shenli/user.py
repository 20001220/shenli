from config import *
from model import *


# 用来登录的
@app.route('/user_select', methods=['POST'])
def user_select():
    if request.method == 'POST':
        id = request.form.get('id')  # 获取form表单的数据
        password = request.form.get('password')  # 获取form表单的数据
        if not all([id, password]):  # 用来判空的
            return render_template('neirongbuquan.html')
        # 使用之前写的User类进行数据库查询
        # filter(User.id == id, User.password == password)：筛选条件
        # .first()：只显示第一个
        user = User.query.filter(User.id == id, User.password == password).first()
        if user:
            return render_template('index.html')
        else:
            return "密码错误！登录失败！"


@app.route('/zhuche')
def zhuche():
    return render_template("zhuche.html")


@app.route('/qudenglv')
def qudenglv():
    return render_template("forestdenglu.html")


# 用来注册的
@app.route('/user_insert', methods=['POST'])
def user_insert():
    uname = request.form.get('uname')  # 根据文本框的名字进行赋值
    upass = request.form.get('upass')
    user = User(id=uname, password=upass)  # 实例化一个User对象
    db.session.add(user)  # 添加一个User对象user
    db.session.commit()  # 事务提交 commit提交关键字
    return render_template("qudenglu.html")  # 界面跳转
