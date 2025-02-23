from flask import Flask, request, jsonify

app = Flask(__name__)
seed = 0  # default seed value

@app.route('/', methods=['GET'])
def get_seed():
    # Return the current seed value as a string
    #return jsonify({'num': seed})
    return str(seed)

@app.route('/', methods=['POST'])
def update_seed():
    global seed
    data = request.get_json()
    if data and 'num' in data:
        seed = int(data['num'])
        print("Seed updated to:", seed, "type =", type(seed))
        #return jsonify({"status": "success", "seed": seed})
        return jsonify({"message": f'Seed value set to {seed}'})
    else:
        return jsonify({"status": "error", "message": "No 'num' provided"}), 400
    #seed = data.get('num', '')

if __name__ == '__main__':
    # Run the app on all interfaces on port 5000
