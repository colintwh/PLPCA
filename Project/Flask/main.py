#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:11:26 2020

@author: mj
"""

# import the Flask class from the flask module
from flask import Flask, render_template, request
import ployTest as poly
import Transcript_pyfinal as py3
import os
#import logging

# create the application object 
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

flag = False

ROOT_PATH = os.path.dirname(os.path.abspath('__file__'))
#ROOT_PATH = str(os.chdir(r"C:\Users\MJ\dev\Flask"))

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template("error.html", content=["Oops Something Wrong...!!!"]), 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return render_template("error.html", content=["Oops Something Wrong...!!!"]), 500

# inbuilt function which takes error as parameter 
@app.errorhandler(404)
def not_found(e): 
  return render_template("error.html", content=["Oops Something Wrong...!!!"]), 404

@app.route('/Upload', methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def Upload():
    print("inside home...")
    cwd = os.getcwd()
    print("cwd - ", cwd)
    print("ROOT_PATH - ", ROOT_PATH)
    print("request.method - ", request.method)
    if request.method == 'POST':
        return render_template("error.html", content=["Oops Something Wrong...!!!"])
    return render_template("home.html", content=["Upload the Transcript file for Sentiment Analysis"])

@app.route("/upload", methods=['POST'])
def upload():
    print("inside upload")
    file = request.files['file']
    #name = request.values['name']
    folderLocation = ROOT_PATH.replace('Flask', 'data')
    file.save(os.path.join(folderLocation,"input.txt"))
    filenameWithLocation = "".join((folderLocation, "\\", "input.txt"))
    print("File name with folderLocation - ", filenameWithLocation)
    if os.path.isfile(filenameWithLocation):
        print("File exist...")
        global flag
        flag = False
        if flag == False :
            print("filenameWithLocation - ", filenameWithLocation)
            py3.getcsv(filenameWithLocation)
            flag = poly.plotAllAspects(folderLocation) 
            print(flag)
            return render_template("sales.html", content=["Transcript's Sentiment Analysis for Aspect - Sales"])
    else:
        render_template("error.html", content=["Oops Something Wrong...!!!"])

@app.route('/OpCost')
def OpCost():
    return render_template('opCost.html', content=["Transcript's Sentiment Analysis for Aspect - Operational Cost"]) 

@app.route('/Sales')
def Sales():
    return render_template('sales.html', content=["Transcript's Sentiment Analysis for Aspect - Sales"]) 

@app.route('/ProductServices')
def ProductServices():
    return render_template('productServices.html', content=["Transcript's Sentiment Analysis for Aspect - Product Services"]) 

@app.route('/Debt')
def Debt():
    return render_template('debt.html', content=["Transcript's Sentiment Analysis for Aspect - Debt"]) 

@app.route('/Earnings')
def Earnings():
    return render_template('earnings.html', content=["Transcript's Sentiment Analysis for Aspect - Earnings"]) 

@app.route('/Acquisitions')
def Acquisitions():
    return render_template('acquisitions.html', content=["Transcript's Sentiment Analysis for Aspect - Acquisitions"]) 

@app.route('/Competition')
def Competition():
    return render_template('competition.html', content=["Transcript's Sentiment Analysis for Aspect - Competition"]) 

@app.route('/OpRisks')
def OpRisks():
    return render_template('opRisks.html', content=["Transcript's Sentiment Analysis for Aspect - Operational Risks"])  

@app.route("/About")
def About():
    return render_template("about.html", content=["About Transcript's Sentiment Analysis and its Team !!!"])

# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 7777)
    #TEMPLATES_AUTO_RELOAD = True
    app.secret_key = 'super_secret_key'