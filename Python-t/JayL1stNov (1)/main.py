from flask import Flask, render_template

###  Always Needed
app = Flask(__name__)




@app.route('/')
def index():
  stats = ['Alex']
  if len(stats) == 2:
    return render_template('index.html', data=stats)
    
  else:
    return render_template('index.html', data=['N/A'] * 2)


@app.route('/runpage')
def runs():
    return render_template('run_page.html')



#### Always needed
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=(8080))
    #app.run() 