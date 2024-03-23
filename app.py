from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from googlesearch import search

app = Flask(__name__)

def check_college_name(college_name):
    # Perform some validation or check if the college name exists
    # For simplicity, we'll just check if the length of the college name is greater than 0
    return len(college_name) > 0

def check_event_name(event_name):
    # Perform some validation or check if the event name exists
    # For simplicity, we'll just check if the length of the event name is greater than 0
    return len(event_name) > 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search_event():
    college_name = request.args.get('college')
    event_name = request.args.get('event')

    if not check_college_name(college_name):
        return jsonify({'error': 'Invalid College'})
    
    if not check_event_name(event_name):
        return jsonify({'error': 'Invalid Event'})

    # Construct the search query
    search_query = college_name + " " + event_name

    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()

    try:
        # Perform a Google search and visit the first result
        for url in search(search_query, num=1, stop=1):
            # Quit the webdriver
            driver.quit()
            return jsonify({'college': college_name, 'eventUrl': url, 'message': 'Original Event'})
    except Exception as e:
        # Quit the webdriver
        driver.quit()
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
