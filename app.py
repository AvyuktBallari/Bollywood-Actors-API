import json
import random
from datetime import datetime
from flask import Flask, request, jsonify
from difflib import get_close_matches

app = Flask(__name__)

with open('data.json', 'r') as f:
    actors = json.load(f)

def find_actor_by_name(name):
    names = [actor['name'] for actor in actors]
    closest = get_close_matches(name, names, n=1, cutoff=0.6)
    if closest:
        return next((actor for actor in actors if actor['name'] == closest[0]), None)
    return None

@app.route('/api/actors', methods=['GET'])
def get_all_actors():
    """Get the entire list of actors."""
    return jsonify(actors), 200

@app.route('/api/actors/random/<int:num>', methods=['GET'])
def get_random_actors(num):
    """Get a specified number of random actors."""
    if num <= 0:
        abort(400, description="Number must be greater than 0")
    return jsonify(random.sample(actors, min(num, len(actors)))), 200

@app.route('/api/actors/<string:name>', methods=['GET'])
def get_actor_by_name(name):
    """Get actor by exact or fuzzy name match."""
    actor = find_actor_by_name(name)
    if actor:
        return jsonify(actor), 200
    abort(404, description="Actor not found")

@app.route('/api/actors/search', methods=['GET'])
def search_actors():
    """Search actors by name, gender, birth date, or birth month."""
    name_query = request.args.get('name', '').lower()
    gender_query = request.args.get('gender', '').lower()
    birth_date_query = request.args.get('birth_date', '').lower()
    birth_month_query = request.args.get('month', '').lower()

    results = actors

    # Filter by name
    if name_query:
        results = [actor for actor in results if name_query in actor['name'].lower()]
    
    # Filter by gender
    if gender_query:
        results = [actor for actor in results if actor['gender'].lower() == gender_query]
    
    # Filter by exact birth date
    if birth_date_query:
        results = [actor for actor in results if actor['birth_date'] == birth_date_query]

    # Filter by birth month
    if birth_month_query:
        try:
            month_number = datetime.strptime(birth_month_query, "%B").month
            results = [
                actor for actor in results
                if datetime.strptime(actor['birth_date'], "%d %B %Y").month == month_number
            ]
        except ValueError:
            abort(400, description="Invalid month format. Use full month names (e.g., 'March').")

    if not results:
        abort(404, description="No actors found matching the criteria")
    
    return jsonify(results), 200


if __name__ == '__main__':
    app.run()
