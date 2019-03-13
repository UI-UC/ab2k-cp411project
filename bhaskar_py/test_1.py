#from flask import Flask
#app = Flask(__name__)
#
#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

#from flask import Flask
#app = Flask(__name__)
#
#@app.route("/") #define "root" (or home) route (using "route" decorator)
#def home(): #this function gets executed for the above route
#    return ( #just a multi-line string, for now
#        "<html>"
#        "   <body>"
#        "       <h2>"
#        "           Hello! this is Web Page2!"
#        "       </h2>"
#        "   </body>"
#        "</html>")
#
##if __name__ == "__main__":
##        app.run(host="0.0.0.0", port=8080)

from flask import Flask
import dbaccess as db
app = Flask(__name__)

@app.route("/") #define "root" (or home) route (using "route" decorator)
def home(): #this function gets executed for the above route
    return ( #just a multi-line string, for now
        f'''<html>
                <body>
                        <h2>
                        List of Beers
                        </h2>
                        {getBeerTable()}
                </body>
                </html>''')

def getBeerTable():
        dbResult = db.executeQuery("SELECT * FROM fridaynight.beers") #fetch rows
        uiResult = None

        if dbResult is None:
                #something wrong in fetching rows
                uiResult = "Some Error"
        else:
                #frame HTML table from fetched rows
                ui = "<table width='50%'>"
                ui += "<thead><td>name</td><td>Brewer</td><td>Alcohol</td></thead>"
                for r in dbResult:
                        ui += "<tr>"
                        ui += f"<td>{r['name']}</td>"
                        ui += f"<td>{r['brewer']}</td>"
                        ui += f"<td>{r['alcohol']}</td>"
                        ui += "</tr>"
                ui += "</table>"
                uiResult = ui

        return uiResult

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
