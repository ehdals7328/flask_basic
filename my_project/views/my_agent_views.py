# views/agent_views.py
from flask import Blueprint, render_template, request, jsonify, session
from my_project.my_agent import ConversationManager  # my_project/agent.py 에서 로드

bp = Blueprint('my_agent', __name__, url_prefix='/my_agent')

# 멀티 세션 지원용 인스턴스 딕셔너리
user_managers = {}

def get_or_create_manager(session_key: str) -> ConversationManager:
    if session_key not in user_managers:
        user_managers[session_key] = ConversationManager()
    return user_managers[session_key]

@bp.route('/')
def index():
    """agent.html 렌더링"""
    return render_template('my_agent.html')

@bp.route('/chat', methods=['POST'])
def chat():
    """웹 대화창 요청 수신 API"""
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'status': 'error', 'error': '메시지가 없습니다.'}), 400

    # 브라우저 세션 키 활용 (없으면 디폴트 키)
    session_key = session.get('user_id', 'default_user_session')

    try:
        manager = get_or_create_manager(session_key)
        answer, log = manager.process_message(user_message)

        return jsonify({
            'status': 'success',
            'answer': answer,
            'log': log
        })
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500