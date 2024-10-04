from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Multiplication Table</h1>
        <form action="/table" method="post">
            <label for="number">Enter a number:</label>
            <input type="number" name="number" id="number" required>
            <input type="submit" value="Generate Table">
        </form>
    '''

@app.route('/table', methods=['POST'])
def table():
    number = int(request.form['number'])
    table_html = "<h2>Table of {}</h2><ul>".format(number)
    
    for i in range(1, 11):
        table_html += f"<li>{number} x {i} = {number * i}</li>"
    
    table_html += "</ul><br><a href='/'>Back</a>"
    return table_html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
