from flask import Flask, render_template, request
import os


app = Flask(__name__)


@app.route('/projects')
def projects():
  return render_template('projects.html')

@app.route('/resume')
def resume():
  return render_template('resume.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    return render_template('response.html', name=name, email=email, phone=phone, message=message)
  return render_template('index.html')



if (__name__ == "__main__"):
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
