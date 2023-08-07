from flask import Flask
app = Flask(__name__)
@app.route('/')
def head():
    return 'Hello world Orhan'
@app.route('/second')
def second():
    return 'This is second page'
@app.route('/third')
def third():
    return 'This is third page'
@app.route('/fourth/<string:id>')
def fourth(id):
    return f'Id of this page is {id}'
if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
    # app.run(host= '0.0.0.0', port=80)
=======
    # app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)
>>>>>>> 0e1447dac1ea6adf8b306b5d9049bb5610fc574e
