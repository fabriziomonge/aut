# app.py

import pandas as pd
data = pd.read_excel('cred.xlsx')
data = data.set_index('Name',1)


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)
    psw = request.args.get("psw", None)
    
    # For debugging
    print(f"got name {name}")
    print(f"got psw {psw}")
    response = {}
    
    name = str(name)
    psw = str(psw)
    
    try:
        # Check if user sent a name at all
        if not name:
            response["ERROR"] = "no name found, please send a name."
        # Check if the user entered a number not a name
        elif str(name).isdigit():
            response["ERROR"] = "name can't be numeric."
        # Now the user entered a valid name

        elif data['PSW'][name]  == psw:
            response["MESSAGE"] = "logged"
        # Now the user entered a valid name

        else:
            response["MESSAGE"] = f"NOT LOGGED"
    except:
        response["MESSAGE"] = f"NOT LOGGED"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
