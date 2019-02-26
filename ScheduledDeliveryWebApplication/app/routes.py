from app import app


@app.route('/search')
def search():
    return "Search"


@app.route('/catalog')
def catalog():
    return "Catalogo"


@app.route('/login')
def login():
    return "Login"


@app.route('/checkout')
def checkout():
    return "Checkout"
