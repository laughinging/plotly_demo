from flask import Flask, render_template, request
from plots import generate_plot

app = Flask(__name__)

@app.route('/change')
def fixed_plot():
    bar = generate_plot()
    return render_template('static.html', plot=bar)

@app.route('/', methods=['GET', 'POST'])    
def select_feature():
    #render_template('dynamic.html', plot=generate_plot())
    selected_group = request.args['selected']
    print(selected_group)
    bar = generate_plot(group=selected_group)
    return render_template('static.html', plot=bar)
    

if __name__ == '__main__':
    app.run(debug=True)