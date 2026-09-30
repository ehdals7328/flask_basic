from flask import Blueprint, jsonify
from pybo.models import Question

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/questions')
def get_questions():
    question_list = Question.query.order_by(Question.create_date.desc()).all()
    return jsonify([q.to_dict() for q in question_list])