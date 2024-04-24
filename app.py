from flask import Flask, render_template, request,redirect,url_for
import pandas as pd
#clsimport chromadb

app = Flask(__name__, static_url_path='/static')

# Load the CSV file
df = pd.read_csv('subtitles.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get user keyword from form
    user_keyword = request.form['keyword']

    # Search for the user keyword in the CSV file
    matched_rows = df[df['file_content'].str.contains(user_keyword, case=False)].head(10)

    # Render the search results template
    return render_template('results.html', keyword=user_keyword, matches=matched_rows)

if __name__ == '__main__':
    app.run(debug=True)
