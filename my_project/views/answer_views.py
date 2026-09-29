# answer_views.py 수정 (Answer 클래스 import 추가 및 객체 생성 방식 변경)
from datetime import datetime
from flask import Blueprint, request, url_for
from my_project import db
from my_project.models import Question, Answer  # Answer import 추가
from werkzeug.utils import redirect

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']

    answer = Answer(content=content, create_date=datetime.now())
    question.answers_set.append(answer)

    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))