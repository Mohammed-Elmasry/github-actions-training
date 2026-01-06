from flask import Flask, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return {"message": f"Hello, {name}!"}

if __name__ == '__main__':
    # We host on 0.0.0.0 so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000)