from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017) # 몽고디비 아이디 패스워드 입력해서 올리기
# client = MongoClient('localhost', 27017) #기존의 몽고디비 연결
db = client.dbhomework
## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')
# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문 완료!'})
# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)