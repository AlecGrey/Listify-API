from run import app

@app.route('/', methods=['GET'])
def home():
    return "<h1>Listify API</h1>"
    # RENDER A VIEW!