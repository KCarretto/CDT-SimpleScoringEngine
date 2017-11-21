"""
This module serves as a basic entry point for web requests.
"""
from . import app
from .models.log import Log
from .models.check import Check
from .config import MAX_RESULTS, SCORED_CHECKS
from flask import request, jsonify, render_template

@app.route('/')
@app.route('/home')
@app.route('/scoreboard')
def home():
    return render_template("scoreboard.html")

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
    checks = []
    for check in SCORED_CHECKS:
        last_round = Check.objects(check_type=check).order_by('-id').first()
        if last_round is None:
            checks.append({'status': 'unchecked'})
        else:
            checks.append(last_round.get_document())

    resp = {
        'status': 200,
        'checks': checks,
        'count': len(checks)
    }
    return jsonify(resp)
