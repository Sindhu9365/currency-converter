from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Static currency rates
rates = {
    'USD': 1.0,
    'EUR': 0.93,
    'INR': 83.0,
    'JPY': 155.0
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']

            converted_amount = (amount / rates[from_currency]) * rates[to_currency]
            result = f"{amount} {from_currency} = {round(converted_amount, 2)} {to_currency}"
        except Exception as e:
            result = f"Error: {e}"
    
    return render_template('index.html', result=result, rates=rates.keys())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets this automatically
    app.run(host='0.0.0.0', port=port)
