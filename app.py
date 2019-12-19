from flask import Flask, render_template, request
from plots import generate_plot
import os

app = Flask(__name__)

@app.route('/')
def fixed_plot():
    bar = generate_plot()
    return render_template('index.html', plot=bar)

@app.route('/change', methods=['GET', 'POST'])    
def select_feature():
    print(request.data)
    
    selected_group = request.args['selected']
    print(selected_group)
    bar = generate_plot(group=selected_group)
    return bar

if __name__ == '__main__':
    app.run()