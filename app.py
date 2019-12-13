from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1> Click to delete your existence! </h1>
    <button type="button" style="width:120px;height:60px;" onclick="alert('Your existence has been ended successfully.')">End Existence</button>
    <h3> Disclaimer: This button doesn't actually do anything </h3>
    '''

if(__name__=='__main__'):
    app.run(debug=False, host='0.0.0.0')