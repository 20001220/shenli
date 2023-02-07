from config import *
from model import *


@app.route('/huo')
def huo():
    return render_template('conflagration.html')



@app.route('/xianshia')
def xianshia():
    return render_template('conflagrationtubiao.html')

@app.route('/shujubiao')
def shujubiao():
    return render_template('conflagration.html')

@app.route('/conflagration_select',methods=['POST','GET'])
def conflagration_select():
    year = request.form.get('year')
    list = []
    if year != None and year != '':
        list.append(Conflagration.year == year)

    # order_by(User.id.desc()).offset(0).limit(3)
    conflagrations = Conflagration.query.filter(*list).order_by(Conflagration.year.asc()).all()
    cnfos=[]
    for f in conflagrations:
        cnfos.append(Cnfo(str(f.year),f.commonly,f.more,f.major,f.significant).__dict__)
    return json.dumps(cnfos)
