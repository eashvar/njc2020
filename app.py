
from flask import *
import sqlite3
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")




@app.route('/find' , methods = ['POST'])
def Search():
    data = request.form
    schname = data["SchoolName"]
    deptname = data["Dept"]
    connection = sqlite3.connect("school.db")
    cursor = connection.execute("select School.Name, Staff.Name,Staff.Department, Staff.Contact, School.Address from School, Staff where School.Name like ? and Staff.Department = ?" ,(f"%{schname}%",deptname))
    cursor = cursor.fetchall()

    return render_template("search.html",cursor = cursor)

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
