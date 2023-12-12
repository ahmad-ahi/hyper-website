from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



c = CurrencyRates()

@app.route('/fun', methods=['POST', 'GET'])
def fun():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"
        
        return f"Result: {result}"
    else:
        return render_template('fun.html')

@app.route('/schedule1', methods=['POST', 'GET'])
def schedule1():
    if request.method == 'POST':
        amount = int(request.form['amount'])
        currency = request.form['currency']

        latest_rates = c.get_rates('USD') 
        if currency in latest_rates:
            exchange_rate = latest_rates[currency]
            converted_amount = amount * exchange_rate

            return f"The converted amount is {converted_amount:.2f} {currency}"
        else:
            return "rates not available"
    else:
        return render_template('schedule1.html')

if __name__ == '__main__':
    app.run(debug=True)
