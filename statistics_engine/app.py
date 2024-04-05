# dependencies -------->
from flask import Flask, jsonify
from requests import get
from flask_cors import CORS

# program variables -------->
app = Flask(__name__)
# enable CORS
CORS(app)

# endpoints -------->
@app.route('/statistics', methods=['GET'])
def get_packages_statistics():
    status_tags = {}
    status_statistics = {}
    response = get('http://0.0.0.0:5000/packages').json()
    package_count = len(response)
    # count how many times each status repeats
    for it in response:
        if it['status'] not in status_tags:
            status_tags[it['status']] = 1
        else:
            status_tags[it['status']] = status_tags[it['status']] + 1

    # obtain the percentage of each status
    for key, value in status_tags.items():
        status_statistics[key] = f"{round((value / package_count) * 100, 2)}%"

    return jsonify({'count' : status_tags, 'statistics' : status_statistics})

# program execution -------->
if __name__ == '__main__':
    app.run(debug=True, port=9000)
