from flask import Flask, render_template
import pymysql

app = Flask(__name__,
        static_url_path='/content', #this can be empty string if we want "images/title.png" directly
        static_folder='static', #map the static folder to serve files directly
        template_folder='templates' #map the templates folder so that flask picks up templates from here
        )


class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = 'mysql'
        db = "fridaynight"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    def list_beers(self):
        self.cur.execute("SELECT name,brewer,alcohol  FROM beers LIMIT 50")
        result = self.cur.fetchall()
        return result

@app.route('/')

def home(): #this function gets executed for the above route
    uiResult=None
    def db_query():
        db = Database()
        results = db.list_beers()
        return results
    res = db_query()
    print(res)
    #return render_template('fridaynight.html', result=res, content_type='application/json')
    if res is None:
       #something wrong in fetching rows
       return  "Some Error"
    else:
       return render_template('fridaynight.html', beers=res) 
