from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://dbpertama:sparta@cluster0.8pjjzub.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    # link github = https://github.com/ffmdn13/fanbook-project.git
    return render_template('index.html')

@app.route('/homework', methods = ['POST'])
def homework_post():
    fan_receive = request.form['fan_data']
    comment_receive = request.form['comment_data']

    doc = {
        'name': fan_receive,
        'comment': comment_receive
    }

    db.fanbook.insert_one(doc)
    return jsonify({'msg': 'Post posted!'})

@app.route('/homework', methods = ['GET'])
def homewrk_get():
    message_list  = list(db.fanbook.find({}, {'_id':False}))
    return jsonify({'msg': message_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)