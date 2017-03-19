# -*- coding:utf-8 *-*

from flask import Flask, render_template, request, flash
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
#app.config.from_object("config")
app.config['MONGODB_DB'] = 'woop_test_DB'
db = MongoEngine(app)

class User(db.Document):
    id = db.IntField(primary_key=True)
    email = db.EmailField(required=True)
    name = db.StringField(max_length=42)
    passwd = db.StringField(required=True)

class WOOP(db.Document):
    user = db.ReferenceField(User)
    save_time = db.DateTimeField(required=True)
    due_time = db.DateTimeField(required=True)
    wish = db.StringField(required=True)
    outcome = db.StringField(required=True)
    obstacle = db.StringField(required=True)
    plan = db.ListField(db.StringField(), required=True)

'''user = User(email='stonemask@noreply.users.github.com', name='stonemask',
            id=10000, passwd='s1k34567')
user.save()
user1 = User(email='martin@email.com', name='martin',
            id=10001, passwd='ma345425')
user1.save()
v = WOOP(wish='心愿a wish', outcome='结果a outcome', save_time=datetime.now(),
            obstacle='困难many obstacles', plan=['如果', '纳闷', '若', '则'],
            due_time='2017-03-16 13:56', user=10000)
v.save()

for a in range(0, len(v.plan), 2):
    print(v.plan[a], v.plan[a+1])
'''
@app.route('/woop', methods=['GET', 'POST'])
def mainpage():
    if request.method == 'POST':
        print(request.form)
        '''print(request.form['wish'])
        print(request.form['due_time'])
        print(request.form['outcome'])
        print(request.form['obs0'])
        print(request.form['obs1'])
        print(request.form['if0'])
        print(request.form['then0'])
        #print(request.form['wish'].encode(encoding="utf-8"))'''
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(debug=True)
