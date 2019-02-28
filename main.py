from flask import Flask,render_template,request,redirect,url_for,flash
import pygal
from flask_sqlalchemy import SQLAlchemy

DB_URL = 'postgresql://postgres:123@127.0.0.1:5432/projectManagementSystem'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='some-secret-string'

db = SQLAlchemy(app)

from models import ProjectModel

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/',methods=['GET'])
def home():
    records = ProjectModel.fetch_all()
    status = [x.status for x in records]
    print(status)
    pie_chart = pygal.Pie()
    pie_chart.title = "Completed vs Pending projects"
    pie_chart.add("Pending projects",status.count("pending"))
    pie_chart.add("Completed projects",status.count("complete"))
    graph = pie_chart.render_data_uri()


    return render_template("index.html",records = records,graph=graph)

@app.route('/project/create',methods=['POST'])
def addNewProject():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        cost = request.form['cost']
        status = request.form['status']
        project = ProjectModel(title=title,description=description,startDate=startDate,
                                      endDate=endDate,cost=cost,status=status)

        project.create_record()

        flash("SUCCESS")
        return redirect(url_for('home'))

@app.route('/project/edit/<int:id>',methods=['POST'])
def editProject(id):
    newTitle = request.form['title']
    newDescription = request.form['description']
    newStartDate = request.form['startDate']
    newEndDate = request.form['endDate']
    newCost = request.form['cost']
    newStatus = request.form['status']
    updated = ProjectModel.update_by_id(id=id,newTitle=newTitle,newDescription=newDescription
                                        ,newStartDate=newStartDate,newEndDate=newEndDate,
                                        newCost=newCost,newStatus=newStatus)

    if updated:
        flash("Updated Successfully")
        return redirect(url_for('home'))
    else:
        flash("No record found")
        return redirect(url_for('home'))

@app.route('/project/delete/<int:id>',methods=['POST'])
def deleteRecord(id):
    deleted = ProjectModel.delete_by_id(id)
    if deleted:
        flash("Deleted Succesfully")
        return redirect(url_for('home'))
    else:
        flash("Record not found")
        return redirect(url_for('home'))



if __name__=='__main__':

    app.run(port=5001,debug=True)

# Bootstrap
# Flask
# SQL-Alchemy

# project management system
 # C- R - U - D


