from flask import Flask, request
import stripe

stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXXX"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = 'ok'
        stripe.Customer.create(
            email=request.form['stripeEmail'],
            source=request.form['stripeToken'])

    return res


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4567)