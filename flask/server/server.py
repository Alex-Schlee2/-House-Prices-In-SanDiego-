from flask import Flask, request, jsonify

import util


app=Flask(__name__)

#http endpoint
@app.route('/get_feature_names', methods=['GET', 'POST', 'DELETE'])

def get_feature_names():
    response=jsonify({'features': util.get_feature_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/predict_home_price', methods=[ 'GET','POST'])
def predict_home_price():
    sqft=float(request.form['sqft'])
    baths = float(request.form['baths'])
    beds = float(request.form['beds'])


    response=jsonify({'estimated_price': util.get_estimated_price(sqft,baths,beds)})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#run application in a specific port
if __name__ == '__main__':
    print('Starting San Diego price prediction')
    util.load_saved_artifacts()
    app.run()