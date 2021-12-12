from flask import Flask, redirect, url_for
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request, make_response
from RedditApp import RedditApp
from flask import render_template
import os
app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://crypTalkAdmin:cryptoScraper@cluster0.8rffs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('crypTalk')
user_collection = pymongo.collection.Collection(db, 'coin_names')

coinList = RedditApp()


@app.route('/addcoin', methods=['POST'])
def post_coin():
    _json = request.json
    name = _json['Name']

    if name and request.method == 'POST':
        id = db.coin_names.insert_one({'Name':name})
        resp = jsonify("Coins updated successfully")
        resp.status_code = 200
    else:
        return not_found()

    return resp

@app.route('/addcoins', methods=['POST'])
def post_coins():
    _json = request.json
    for coin in _json:
        name = coin['Name']

        if name and request.method == 'POST':
            id = db.coin_names.insert_one({'Name':name})
            resp = jsonify("Coins updated successfully")
            resp.status_code = 200
        else:
            return not_found()

    return resp

@app.route('/getcoin', methods=['GET'])
def get_coin():
    id = request.args.get('id')
    print("Id:",id)
    if len(id) != 24:
        messsage = {
            'status': 404,
            'message:': 'The requested ID must be a 24 character hex'
        }
        resp = jsonify(messsage)
        resp.status_code = 404
        return resp
    coin = db.coin_names.find_one({'_id':ObjectId(id)})
    if coin is None:
        message = {
            'status': 404,
            'message': 'The requested coin \'s ID was not found'}
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    resp = dumps(coin)
    return resp

@app.route('/getcoins', methods=['GET'])
def get_coins():
    resp = coinList.getCoinScores()
    print(resp)
    return dumps(resp)

@app.route('/updatecoin', methods=['PUT'])
def update_coin():
    id = request.args.get('id')
    toUpdate = request.json
    if len(id) != 24:
        messsage = {
            'status': 404,
            'message:': 'The requested ID must be a 24 character hex'
        }
        resp = jsonify(messsage)
        resp.status_code = 404
        return resp
    coin = db.coin_names.find_one({'_id':ObjectId(id)})
    if coin is None:
        message = {
            'status': 404,
            'message': 'The requested coin \'s ID was not found'}
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    db.coin_names.update({'_id': ObjectId(id)},
                             {'$set': {list(toUpdate.keys())[0] : list(toUpdate.values())[0] }})

    resp = jsonify("Coin updated successfully")

    resp.status_code = 200

    return resp

@app.route('/deletecoin', methods=['DELETE'])
def delete_coin():
    id = request.args.get('id')
    if len(id) != 24:
        messsage = {
            'status': 404,
            'message:': 'The requested ID must be a 24 character hex'
        }
        resp = jsonify(messsage)
        resp.status_code = 404
        return resp
    coin = db.coin_names.find_one({'_id':ObjectId(id)})
    if coin is None:
        message = {
            'status': 404,
            'message': 'The requested coin \'s ID was not found'}
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    db.coin_names.delete_one({'_id':ObjectId(id)})
    resp = jsonify("Coin deleted successfully")

    resp.status_code = 200

    return resp

@app.errorhandler(404)
def not_found(error=None):
    messsage = {
        'status': 404,
        'message:': 'Request not found' + request.url
    }
    resp = jsonify(messsage)
    resp.status_code = 404
    return resp