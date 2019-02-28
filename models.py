from main import db

class ProjectModel(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(120),nullable=False,unique=True)
    description = db.Column(db.String(),nullable=True)
    startDate = db.Column(db.String(50),nullable=False)
    endDate = db.Column(db.String(50),nullable=False)
    cost = db.Column(db.Integer,nullable=False)
    status = db.Column(db.String(30))


    # CREATE
    def create_record(self):
        db.session.add(self)
        db.session.commit()


    # READ

    @classmethod
    def fetch_all(cls):
        records = ProjectModel.query.all()
        return records

    #UPDATE

    @classmethod
    def update_by_id(cls,id,newTitle,newDescription,newStartDate,newEndDate,newCost,newStatus):
        record = ProjectModel.query.filter_by(id=id).first()
        if record:
            record.title = newTitle
            record.description = newDescription
            record.startDate = newStartDate
            record.endDate = newEndDate
            record.cost = newCost
            record.status = newStatus
            db.session.commit()
            return True
        else:
            return False

    #DELETE
    @classmethod
    def delete_by_id(cls,id):
        record = ProjectModel.query.filter_by(id=id)
        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False













