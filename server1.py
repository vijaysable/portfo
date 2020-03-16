from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


# from html - templating lang - jinja {{}} means flask knows inside this is python expression which it has to evaluate
@app.route('/<string:page_name>')
def index(page_name=None):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_file(data)
        write_csv_file(data)
        return redirect('./thankyou.html')
    else:
        return 'something went wrong'


def write_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        text = data['text']
        file = database.write(f'\n {email} - {subject} - {text}')


# def write_csv_file(data):
#     with open('data.csv', mode='a', newline='') as csvfile:
#         email = data['email']
#         subject = data['subject']
#         text = data['text']
#         writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow([email,subject,text])


def write_csv_file(data):
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['email', 'subject', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'email': data['email'], 'subject': data['subject'], 'text': data['text']})

#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')