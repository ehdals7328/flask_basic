from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # question 속성은 Answer가 연결된 Question 객체를 가리킴.
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False) # DateTime 함수와 다르게 무조건 시간을 출력하는 기능이아님
    # 이 공간에는 시간을 적겠다 라는 테이블이므로, 이후 datetime.now()로 시간을 넣어야함
    # 그렇기 때문에 nullable=False를 적어주는 것.