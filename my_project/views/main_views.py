from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/vision')
def vision():
    return render_template('vision.html')


@bp.route('/rag')
def rag():
    return render_template('rag.html')


@bp.route('/agent')
def agent():
    return render_template('agent.html')