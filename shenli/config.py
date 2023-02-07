from flask import *
from flask_sqlalchemy import *  # 引入了flask库和flask_sqlalchemy库
from sqlalchemy import func  # 这个库没用到

# flask基本配置信息：
app = Flask(__name__)
app.config.from_object('setting')    # 这个setting和setting.py是对应的
db = SQLAlchemy(app=app)
