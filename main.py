from flask import Flask,render_template,jsonify

app = Flask(__name__)

ITEMS = [
    {
        'item_code':1,
        'item_name':'تیرامیسو',
    },
    {
        'item_code':2,
        'item_name':'چیزکیک سن سباستین'
    }

]

WORKS = [
    'جابه جایی اقلام',
    'سفارش کیک',
    'سفارش شیر',
    'سفارش نان',
    'سفارش ساندویچ',
]

@app.route("/")
def hello_world():
    return render_template('home.html',items=ITEMS,works=WORKS)

@app.route("/api/items")
def items():
    return jsonify(ITEMS)
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)