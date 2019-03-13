from flask import Flask, render_template
import pymysql
app = Flask(__name__)
class Database:
    def __init__(self):
        #host = "localhost"
        #user = "root"
        #password = 'mysql'
        #db = "fridaynight"
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
    return ( #just a multi-line string, for now
        f'''<html>
                <body>
                        <h2>
                        List of Beers
                        </h2>
                        {beers()}
                </body>
                </html>''')
def beers():
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
       uiResult = "Some Error"
    else:
       #frame HTML table from fetched rows
       ui = "<table width='50%'>"
       ui += "<thead><td>BeerName</td><td>Brewer Name</td><td>Alcohol</td></thead>"
       for r in res:
               ui += "<tr>"
               ui += f"<td>{r['name']}</td>"
               ui += f"<td>{r['brewer']}</td>"
               ui += f"<td>{r['alcohol']}</td>"
               ui += "</tr>"
       ui += "</table>"
       uiResult = ui

    return uiResult
