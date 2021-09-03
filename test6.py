from flask import Flask,render_template
app = Flask(__name__,template_folder='templates')
  
@app.route('/')
def home():
    return render_template("template2.html")
if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(debug=True)
