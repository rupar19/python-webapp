from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the application on a development server
    app.run(debug=True)
