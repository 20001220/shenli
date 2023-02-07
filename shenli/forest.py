from config import *  # 引入config文件
from model import *  # 引入model文件


@app.route('/denglu')
def denglu():
    return render_template('forestdenglu.html')  # 用来跳转界面的


@app.route('/fanhuione')
def fanhuione():
    return render_template('index.html')  # 用来跳转界面的


@app.route('/tubiao')
def tubiao():
    return render_template('forestubiao.html')  # 用来跳转界面的


@app.route('/chuntubiao')  # 用来跳转界面的，根据get到的数值选择跳到哪个界面
def chuntubiao():
    opt = int(request.args.get('opt'))
    if opt == 0:
        return render_template('tubiao.html')
    elif opt == 1:
        return render_template('tubiao1.html')
    elif opt == 2:
        return render_template('tubiao2.html')
    elif opt == 3:
        return render_template('tubiao3.html')
    elif opt == 4:
        return render_template('tubiao4.html')
    else:
        return render_template('tubiao5.html')


@app.route('/forest_select', methods=['POST', 'GET'])  # 设置路由的请求接收方式
def forest_select():
    year = request.form.get('year')  # 获取form表单的数据
    list = []
    if year != None and year != '':
        list.append(Forest.year == year)

    # order_by(User.id.desc()).offset(0).limit(3)
    # order_by():用来排序，通过里面的参数进行排序
    forests = Forest.query.filter(*list).order_by(Forest.year.asc()).all()  # 返回一个列表，里面是筛选到的数据库的数据
    snfos = []
    for f in forests:  # 通过Snfo类以及.__dict__把forests里面的数据转化为字典并存入snfos列表
        snfos.append(Snfo(f.year, f.forestrylandarea, f.forestcoverage, f.plantationarea,
                          f.forest, f.livingtree, f.standingtree).__dict__)
    return json.dumps(snfos)  # 返回一个json串
