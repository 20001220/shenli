from config import *  # 引入config文件


# 本文件用来存放类的，写了两种类

# 第一种 用来操作数据库的数据，一个类对应一个表
class User(db.Model):  # 类名要和数据库的表名一致，首字母要大写
    id = db.Column(db.Integer, primary_key=True)  # 这下面每一行要和表中的列对应上
    password = db.Column(db.String(50))  # 例如：id是列名，db.Integer说明这是一个整形，primary_key=True说明这列是主键
# db.String(50)说明这是一个长度为50的字符串，数据库里对应的类型是VARCHAR，但是通过实际使用发现
# 类型的对应并没有那么严格。很多时候python里的类型写错了也一样能用,但是能对应上还是对应上吧

class Conflagration(db.Model):
    year = db.Column(db.Integer, primary_key=True)
    commonly = db.Column(db.Float(50))
    more = db.Column(db.Float(50))
    major = db.Column(db.Float(50))
    significant = db.Column(db.Float(50))


class Forest(db.Model):
    year = db.Column(db.Integer, primary_key=True)
    forestrylandarea = db.Column(db.Float(50))
    forestcoverage = db.Column(db.Float(50))
    plantationarea = db.Column(db.Float(50))
    forest = db.Column(db.Float(50))
    livingtree = db.Column(db.Float(50))
    standingtree = db.Column(db.Float(50))


# 第二种
# 用来存放一些数据，在后面的文件会用到，
# 大概就是给这个类传入 year, forestrylandarea, forestcoverage,等等对应的数据（有顺序的），
# 然后这个类实例化的对象就含有了这些数据
class Snfo:
    def __init__(self, year, forestrylandarea, forestcoverage, plantationarea, forest, livingtree, standingtree):
        self.year = year
        self.forestrylandarea = forestrylandarea
        self.forestcoverage = forestcoverage
        self.plantationarea = plantationarea
        self.forest = forest
        self.livingtree = livingtree
        self.standingtree = standingtree


class Cunzhi:
    def __init__(self, year, count):
        self.year = year
        self.count = count


class EchartsA:
    def __init__(self, company, count):
        self.company = company
        self.count = count


class Cnfo:
    def __init__(self, year, commonly, more, major, significant):
        self.year = year
        self.commonly = commonly
        self.more = more
        self.major = major
        self.significant = significant
