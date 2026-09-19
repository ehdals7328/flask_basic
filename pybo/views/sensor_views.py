from flask import Blueprint

bp = Blueprint('sensor', __name__, url_prefix='/sensor')

@bp.route('/status')
def status():
    return "카메라 정상 작동 중"
