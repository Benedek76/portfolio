from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

# Adding URL parametars
# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data): # Need the csv module of Python
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# Setup csv DB
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
      except:
        return 'did not save to database'
    else:
        return 'Something went wrong. Try again!'

# Settings for display messages on the screen
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'Something went wrong. Try again!'


# Begening settings
# @app.route("/works.html")
# def works():
#     return render_template('works.html')
#
# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


# Test Pages
# @app.route("/blog")
# def blog():
#     return "<p>Hello, Lilcoka from blog!</p>"
#
# @app.route("/blog/2020/dogs")
# def blog2():
#     return "<p>Hello, dog - Mogyika!</p>"
#
# @app.route("/about")
# def about():
#     return render_template('about.html')