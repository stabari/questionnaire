from flask import Flask, request, json, Response, jsonify
import pickle

from flask_cors import CORS, cross_origin
import pandas as pd
# initialized the Flask APP
app = Flask(__name__)
CORS(app, support_credentials=True)

min = [-4.52364,-4.53089,	-4.83648,	-1.24421,	0.0000717008,	0.12051,	-0.05765,	0.0001,	0.0163,	-0.1124,	-0.0365,	0.0032,	-0.0975,	-0.01915]
max= [-2.59793,	-2.58566,	-1.77495,	1.37953,	0.070945104,	1.20653,	0.05116,	0.163,	0.1482,	0.1523,	0.0455,	0.0338,	0.0737,	0.05882
]

# Fetchs the model file for prediction
model1 = pickle.load(open('./backend/model.pkl','rb'))

def normalize_input(input):
    """
    Normalizes the given input values min/max.
    """
    r = []
    i=0;
    for x in input:
        t = 0 # modify code here
        r.append(t)
        i=i+1
    return r;

# Achieving CRUD through API - '/crudapi'
@app.route('/predict', methods=['POST'])
def read_data():
    """
    Takes in a list of values from the user and normalizes it and makes prediction with it.
    """

    data = request.json
    read_obj = normalize_input(data)
    print([read_obj])
    print(model1.predict([read_obj]))
    
    return json.dumps(model1.predict([read_obj]).tolist())
   
@app.route('/', methods=['GET'])
def api():
    """
    Tests whether the API is active.
    """
    return "API is active"

@app.route('/data', methods=['GET'])
def data():
    live_df = pd.read_excel('data/SPX_live0.xlsx')
    print(live_df)
    return live_df.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)