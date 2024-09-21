from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load member data from store_data.json
with open('store_data.json', 'r') as json_file:
    members_data = json.load(json_file).get('pragicts', {}).get('member', [])

# Route for the root URL
@app.route('/')
def index():
    return render_template('index.html', members=members_data)

# Profile route with verification ID parameter
@app.route('/profile/<verification_id>')
def profile(verification_id):
    # Find the member with the given verification_id
    member = next((emp for emp in members_data if emp.get('verification_id') == verification_id), None)
    if member:
        return render_template('profile.html', member=member)
    else:
        return render_template('404.html'), 404

# Staff verification route
@app.route('/member-verification.py')
def staff_verification():
    verification_id = request.args.get('verification-id')
    # Find the member with the given verification_id
    member = next((emp for emp in members_data if emp.get('verification_id') == verification_id), None)
    if member:
        return render_template('profile.html', member=member)
    else:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
