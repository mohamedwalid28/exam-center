from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
import uuid


app = Flask(__name__, template_folder='../EXAM Center Enhanced/templates', static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@WALIDSPC/Eexam_center?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)


class Doctor(db.Model):
    __tablename__ = 'Doctors'
    __table_args__ = {'extend_existing': False}

    DoctorID = db.Column(db.Integer, primary_key=True)  #,default=lambda: str(uuid.uuid4())
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(50), nullable=False)

    # def __init__(self, Username, Name, Password):
    #     self.DoctorID = str(uuid.uuid4())  # Generate UUID for DoctorID
    #     self.Username = Username
    #     self.Name = Name
    #     self.Password = Password
        
class Student(db.Model):
    __tablename__ = 'Students'
    __table_args__ = {'extend_existing': False}

    StudentID = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    Email = db.Column(db.String(255), unique=True, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(50), nullable=False)

class Exam(db.Model):
    __tablename__ = 'Exams'
    __table_args__ = {'extend_existing': False}

    ExamID = db.Column(db.String, primary_key=True, server_default=str(func.newid()))
    DoctorID = db.Column(db.String, db.ForeignKey('Doctors.DoctorID'), nullable=False)
    ExamName = db.Column(db.String(255), nullable=False)
    Questions = db.Column(db.String, nullable=False)
    Answers = db.Column(db.String, nullable=False)
    TotalScore = db.Column(db.Integer, nullable=False)

    # Define the relationship to the Doctor model
    doctor = db.relationship('Doctor', backref='exams', foreign_keys=[DoctorID])


class AnsweredExam(db.Model):
    __tablename__ = 'AnsweredExams'
    __table_args__ = {'extend_existing': False}

    ExamID = db.Column(db.String, db.ForeignKey('exam.ExamID'), primary_key=True)
    DoctorID = db.Column(db.String, db.ForeignKey('doctor.DoctorID'), primary_key=True)
    StudentID = db.Column(db.String, db.ForeignKey('student.StudentID'), primary_key=True)
    ModelAnswer = db.Column(db.String, nullable=False)
    StudentAnswers = db.Column(db.String, nullable=False)
    FinalScore = db.Column(db.Integer, nullable=False)

class ExamReport(db.Model):
    __tablename__ = 'ExamReports'
    __table_args__ = {'extend_existing': False}

    DoctorID = db.Column(db.String, db.ForeignKey('Doctors.DoctorID'), primary_key=True)
    StudentID = db.Column(db.String, db.ForeignKey('Students.StudentID'), primary_key=True)
    ExamID = db.Column(db.String, db.ForeignKey('Exams.ExamID'), primary_key=True)
    FinalScore = db.Column(db.Integer, nullable=False)
    Percentage = db.Column(db.Float, nullable=False)

    # Define a relationship to the Exam model
    exam = db.relationship('Exam', backref='exam_reports', primaryjoin='ExamReport.ExamID == Exam.ExamID')

global doctor_name
doctor_name = None
#test cases to check that inserting works well
def insert_initial_values():
    # Check if there are any doctors in the database
# Insert initial values
        doctor = Doctor.query.first()

        if doctor:
            doctor_id = doctor.DoctorID
            global doctor_name
            doctor_name = doctor.Name
        else:
            doctor_id = None



       # doctor_id =  Doctor.query.with_entities(Doctor.DoctorID).order_by(func.newid()).limit(1).scalar()
        initialExams = [
           Exam(
                # DoctorID=doctor_id,
                ExamName='Data Science',
                Questions='Dr. John Smith',
                Answers='passwords123',
                TotalScore=202
                ),
            Exam(
                # DoctorID=doctor_id,
                ExamName='Data Analysis',
                Questions='Dr. John Smith',
                Answers='passwords123',
                TotalScore=202
                )
        ]

        # Add doctors to the session and commit changes to the database
        db.session.add_all(initialExams)
        db.session.commit()
        print("insertion Done")

def insert_initial_valuesdoc():
    # Check if there are any doctors in the database
    if not Doctor.query.first():
        # Insert initial values
        # doctor_id =  Doctor.query.with_entities(Doctor.DoctorID).order_by(func.newid()).limit(1).scalar()

        new_doctor = Doctor(
        # DoctorID = Doctor.query.with_entities(Doctor.DoctorID).order_by(func.newid()).limit(1).scalar(),
        Username='john_doe',
        Name='John Doe',
        Password='secure_password'
        )

# Add the new doctor to the session
        db.session.add(new_doctor)
# Commit the changes to the database
        db.session.commit()
        print("insertion Done")

def insert_exam_qeustions(docusername,):
    if Exam.query.first():
        pass
        

global docusername  
docusername = ""

global studentusername
studentusername = ""

@app.route('/')
@app.route('/index')
def index():
    doctors = Doctor.query.all()
    insert_initial_valuesdoc()
    return render_template('index.html', doctors=doctors)
    return render_template('index.html')

@app.route('/Dlogin')
def Dlogin():
    return render_template('Dlogin.html')

@app.route('/Slogin')
def Slogin():
    insert_initial_values()
    return render_template('Slogin.html')

@app.route('/DExam')
def DExam():
    return render_template('DExam.html')

@app.route('/doccreateexam')
def doccreateexam():
    return render_template('doccreateexam.html')

@app.route('/docinsertexams')
def docinsertexams():
    return render_template('docinsertexams.html')

@app.route('/SExam')
def SExam():
    Examss = Exam.query.all()
    print(Examss)
    return render_template('SExam.html', exam_data = Examss, docname = doctor_name)

@app.route('/Sign')
def Sign():
    return render_template('Sign.html')

@app.route('/managexams')
def managexams():
    return render_template('manageexams.html')

if __name__ == '__main__':
    app.run(debug=True)
