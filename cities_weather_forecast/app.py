import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/weatherForecast', methods=['GET'])
def index():
    try:
        if request.method == 'GET':
            if request.args.get('cityName'): 

                ## get list of cities
                ##https://search.reservamos.mx/api/v2/places?q=mon

                print(request.args.get('cityName'))
                ## set the url of the service
                _url = 'https://search.reservamos.mx/api/v2/places?q='+request.args.get('cityName')
                print(_url)
                ## generate the get call
                _response = requests.get(_url)
                
                print(_response)
                ## returns the json as response
                return _response.json(), 200


                ##return jsonify({"status": "success"})
            else: 
                return '', 400
        else:
            return '', 405
        ##return "Welcome to Cities Weather Forecast!"
    except Exception as e: 
        ## In case of error.
        return jsonify({"status":"Error", "code": 500, "reason": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True) 