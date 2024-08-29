from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests


def get_currency(in_cur,out_cur):
    url = f"https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate=soup.find('span',class_='ccOutputRslt').get_text()
    rate=float(rate[:-4])

    return rate


app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate</h1> <p>Example URL: /api/v1/usd-inr </p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur,out_cur):
    rate=get_currency(in_cur, out_cur)
    result_dicty={'input_currency':in_cur, 'output_currency':out_cur, 'rate':rate}
    return jsonify(result_dicty)

if __name__ == '__main__':
    app.run(debug=True)
