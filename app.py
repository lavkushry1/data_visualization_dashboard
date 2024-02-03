from flask import Flask, jsonify, request
from models import db_session, Event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_session.init_app(app)

@app.route('/')
def index():
    return "Welcome to the Data Visualization Dashboard!"

@app.route('/api/events', methods=['GET'])
def get_events():
    start_year = request.args.get('start_year')
    end_year = request.args.get('end_year')
    country = request.args.get('country')
    city = request.args.get('city')
    topics = request.args.get('topics')
    region = request.args.get('region')
    sector = request.args.get('sector')
    pest = request.args.get('pest')
    source = request.args.get('source')
    swot = request.args.get('swot')
    query = "SELECT * FROM event WHERE "
    filters = []
    if start_year:
        filters.append(f"year >= {start_year}")
    if end_year:
        filters.append(f"year <= {end_year}")
    if country:
        filters.append(f"country = '{country}'")
    if city:
        filters.append(f"city = '{city}'")
    if topics:
        filters.append(f"topics LIKE '%{topics}%'")
    if region:
        filters.append(f"region = '{region}'")
    if sector:
        filters.append(f"sector = '{sector}'")
    if pest:
        filters.append(f"pest = '{pest}'")
    if source:
        filters.append(f"source = '{source}'")
    if swot:
        filters.append(f"swot = '{swot}'")
    if filters:
        query += " AND ".join(filters)
    else:
        query += "1=1"
    events = db_session.query(Event).filter(query).all()
    return jsonify([event.__dict__ for event in events])

if __name__ == '__main__':
    app.run(debug=True)