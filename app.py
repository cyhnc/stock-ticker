from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)


@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
  ticker = request.form['text']
  pticker = ticker.upper()
  api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % pticker
  session = requests.Session()
  session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
  raw_data = session.get(api_url)
  
  plot = figure(tools=TOOLS,
              title='Data from Quandle WIKI set',
              x_axis_label='date',
              x_axis_type='datetime')

  script,div = components(plot)
  return render_template('graph.html', script=script, div=div)
  


if __name__ == '__main__':
  app.run(port=33507)
