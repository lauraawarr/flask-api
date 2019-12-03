from flask import Flask, request, jsonify, abort, make_response
from application import application
from application import db
from application.models import TodoList

# Elastic Beanstalk initalization
application.debug=False
application.secret_key = 'AKIAYKPGJGQ5ZMQXHZC7'

@application.route('/todos', methods=['GET'])
def get_todos():
    todos = []
    try:
        query_db = TodoList.query.order_by(TodoList.id.desc())
        for q in query_db:
            todos.append(q.json())
        db.session.close()
        return jsonify({ 'todos': todos })
    except:
        db.session.rollback()
        return abort(500)

@application.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or not 'title' in request.json:
        abort(400)
    try:
        data_entered = TodoList(title=request.json['title'], notes=request.json.get('notes', ''))
        db.session.add(data_entered)
        db.session.expunge_all()
        db.session.commit()  
        db.session.close()
        return jsonify({ 'task': data_entered.json() }), 201
    except:
        db.session.rollback()
        return abort(500)

@application.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 404)

@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@application.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error': 'Internal server error'}), 500)

if __name__ == '__main__':
    application.run(host='0.0.0.0')