"""
This module serves as a basic entry point for web requests.
"""
from . import app
from .models.log import Log
from .models.check import Check
from .config import MAX_RESULTS, SCORED_CHECKS
from flask import request, jsonify, render_template
from threading import Thread, Event
from engine.engine import Engine

threads = []
event = Event()

frozen = True


@app.route('/')
@app.route('/home')
@app.route('/scoreboard')
def home():
    return render_template("scoreboard.html")


@app.route('/api/start')
def start_threads():
    global frozen
    if not frozen:
        return 'Already running'
    frozen = False

    for i in range(1):
        e = Engine(event=event, tid=i)
        e.start()
        threads.append(e)
    return 'Started'

@app.route('/api/stop')
def stop_threads():
    global frozen
    if frozen:
        return 'Not running'
    event.set()
    for t in threads:
        t.join()
    frozen = True

    return 'Stopped'

@app.route('/api/logs', methods=['POST', 'GET'])
def api_logs():
    # Retrieve data from request
    data = { }
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            data = request.form
    index = data.get('index', 0)
    limit = data.get('limit', MAX_RESULTS)

    # Sanity Checks
    if type(index) != int or type(limit) != int:
        return jsonify({
            'status': 400,
            'description': 'Invalid parameter type. \'limit\' and \'index\' must be integers, or not included.'
        })
    if index < 0:
        index = 0
    if limit > MAX_RESULTS or limit < 0:
        limit = MAX_RESULTS
    
    # Get data
    end = index+limit
    logs = Log.objects[index:end]
    resp = {
        'status': 200,
        'logs': logs,
        'count': len(logs) 
    }
    return jsonify(resp)

@app.route('/api/checks', methods=['POST', 'GET'])
def api_checks():
    # Retrieve data from request
    data = { }
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            data = request.form
    index = data.get('index', 0)
    limit = data.get('limit', MAX_RESULTS)

    # Sanity Checks
    if type(index) != int or type(limit) != int:
        return jsonify({
            'status': 400,
            'description': 'Invalid parameter type. \'limit\' and \'index\' must be integers, or not included.'
        })
    if index < 0:
        index = 0
    if limit > MAX_RESULTS or limit < 0:
        limit = MAX_RESULTS
    
    # Get data
    end = index+limit
    checks = Check.objects[index:end]
    resp = {
        'status': 200,
        'checks': checks,
        'count': len(checks) 
    }
    return jsonify(resp)

@app.route('/api/round/')
def api_round():
    global frozen

    checks = []
    for check in SCORED_CHECKS:
        last_round = Check.objects(check_type=check).order_by('-id').first()
        if last_round is None or frozen:
            checks.append(
                {
                    'check_type': check,
                    'passed': False,
                    'check_status': 'Frozen',
                    'frozen': True
                })
        else:
            checks.append(last_round.get_document())
    resp = {
        'status': 200,
        'checks': checks,
        'count': len(checks)
    }
    return jsonify(resp)
