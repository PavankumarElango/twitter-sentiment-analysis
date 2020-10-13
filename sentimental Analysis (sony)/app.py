# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:26:35 2020

@author: pavan
"""
from flask import Flask,render_template,request
import pickle 
#summarise
from gensim.summarization import summarize
app = Flask(__name__)  
     
with open('tweet.pkl','rb') as f:
    data = pickle.load(f) 

@app.route('/')  
def message():
    return render_template('home.html')  


@app.route('/sentiment',methods = ['POST','GET'])
def sentiment():
	if request.method == 'POST':
		message = request.form['message']
		# Machine learning analysiser
		pred = data.predict([message])
		return render_template('home.html', prediction=pred)



# summarize
@app.route('/nlpsummarize')
def summarize_nlp():
	return render_template('summarize.html')

# spam classification
@app.route('/summarize',methods= ['POST','GET'])
def sum_route():
	if request.method == 'POST':
		message = request.form['message']
		sum_message = summarize(message)
		return render_template('summarize.html',original = message, prediction=sum_message)


if __name__ == '__main__':
    app.run(debug = True)      
    
    
    