from flask import Flask, request, jsonify, url_for
import os
import random
import json

app = Flask(__name__)
#set static path
app.static_folder = 'static'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/dog_img')
def dog_img():
    imgs = os.listdir('static/dog')
    img = random.choice(imgs)
    baseurl = request.base_url
    sendurl = baseurl.replace('dog_img', 'static/dog/'+img)
    return jsonify({'img': sendurl})

@app.route('/cat_img')
def cat_img():
    imgs = os.listdir('static/cat')
    img = random.choice(imgs)
    baseurl = request.base_url
    sendurl = baseurl.replace('cat_img', 'static/cat/'+img)
    return jsonify({'img': sendurl})

@app.route('/dog_fact')
def dog_fact():
    facts = json.load(open('static/dog_fact.json'))
    fact = random.choice(facts)
    return jsonify({'fact': fact})

@app.route('/cat_fact')
def cat_fact():
    facts = json.load(open('static/cat_fact.json'))
    fact = random.choice(facts)
    return jsonify({'fact': fact})




if __name__ == '__main__':
    app.run(debug=True,port=4000)