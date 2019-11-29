from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from app import app

from app import login
db = SQLAlchemy(app)


db.Model.metadata.reflect(bind=db.engine, schema='coursework_db')
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return Therapists.query.get(int(id))




class Therapists(UserMixin, db.Model):
    '''deal with an existing table'''
    __table__ = db.Model.metadata.tables['coursework_db.therapists']
    

    def __str__(self):
        return str({"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "title": self.title, "username": self.username, "password": self.password})

    def __repr__(self):
        return str({"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "title": self.title, "username": self.username, "password": self.password})
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if self.password_hash == None:
            self.set_password(password)
            db.session.commit()
        return check_password_hash(self.password_hash, password)

class Patients(db.Model):
    __table__ = db.Model.metadata.tables["coursework_db.patient_info"]

    def __str__(self):
        return str({"pid": self.pid, "last_name": self.last_name, "first_name": self.first_name, "ssn": self.ssn, "gender": self.gender, "age": self.age, "therapist_id": self.therapist_id})

    def __repr__(self):
        return str({"pid": self.pid, "last_name": self.last_name, "first_name": self.first_name, "ssn": self.ssn, "gender": self.gender, "age": self.age, "therapist_id": self.therapist_id})


class Images(db.Model):
    __table__ = db.Model.metadata.tables["coursework_db.images"]

    def __str__(self):
        return str({"image_id": self.image_id, "patient_id": self.patient_id, "datetime": self.datetime, "im_type": self.im_type, "image": self.image})

    def __repr__(self):
        return str({"image_id": self.image_id, "patient_id": self.patient_id, "datetime": self.datetime, "im_type": self.im_type, "image": self.image})


class ImageAnalysis(db.Model):
    __table__ = db.Model.metadata.tables["coursework_db.image_analysis"]

    def __str__(self):
        return str({"image_id": self.image_id, "segment": self.segment, "tumor": self.tumor, "diagnosis": self.diagnosis, "recommendations": self.recommendations, "confidence": self.confidence, "datetime": self.dt, "verified": self.verified})

    def __repr__(self):
        return str({"image_id": self.image_id, "segment": self.segment, "tumor": self.tumor, "diagnosis": self.diagnosis, "recommendations": self.recommendations, "confidence": self.confidence, "datetime": self.dt, "verified": self.verified})


class ImageTypes(db.Model):
    __table__ = db.Model.metadata.tables["coursework_db.image_types"]

    def __str__(self):
        return str({"id": self.id, "name": self.name})

    def __repr__(self):
        return str({"id": self.id, "name": self.name})


class TumorTypes(db.Model):
    __table__ = db.Model.metadata.tables["coursework_db.tumor_types"]

    def __str__(self):
        return str({"id": self.id, "name": self.name, "descr": self.descr})

    def __repr__(self):
        return str({"id": self.id, "name": self.name, "descr": self.descr})
