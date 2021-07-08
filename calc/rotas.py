from flask import current_app as app, render_template, request
import math

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'GET':
        return render_template('soma.html')

    elif request.method == 'POST':
        p1 = request.form['p1']
        p2 = request.form['p2']

        op = "soma"
        res = float(p1) + float(p2)

        return render_template('resposta.html', op=op, res=res, p1=p1, p2=p2)

@app.route('/subtrair', methods=['POST', 'GET'])
def subtrair():
    if request.method == 'GET' :
        return render_template('subtração.html')
    
    elif request.method == 'POST':
        min = request.form['min']
        sub = request.form['sub']

        op = "subtração"
        res = float(min) - float(sub)

        return render_template('resposta.html', op=op, min=min, sub=sub, res=res)

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if  request.method == 'GET' :
        return render_template('multiplicação.html')

    elif request.method == 'POST' :
        multn = request.form['multn']
        multr = request.form['multr']

        op = "multiplicação"
        res = float(multn) * float(multr)

        return render_template('resposta.html', op=op, multn=multn, multr=multr, res=res)

@app.route('/dividir', methods=['POST', 'GET'])
def dividir():
    if request.method == 'GET':
        return render_template('divisão.html')
    
    elif request.method == 'POST':
        divs = request.form['divs']
        divd = request.form['divd']

        op = "divisão"
        quo = float(divd)/float(divs)

        return render_template('resposta.html', op=op, divs=divs, divd=divd, quo=quo)

@app.route('/grau', methods=['GET', 'POST'])
def grau():
    if request.method == 'GET':
        return render_template('2grau.html')

    elif request.method == 'POST':
        va = request.form['a']
        vb = request.form['b']
        vc = request.form['c']

        op = "2grau"
        delta = float(vb)**2 - (4*float(va)*float(vc))
        x1 = (-float(vb) + math.pow(delta, 1/2))/(2*float(va))
        x2 = (-float(vb) - math.pow(delta, 1/2))/(2*float(va))

        return render_template('resposta.html', op=op, delta=delta, x1=x1, x2=x2)



