from app_pembelians.entry.suplier import app_suplier, controller_suplier
from flask import render_template, redirect, url_for
  
@app_suplier.route('/suplier-json', methods=['GET', 'POST'])
def suplierJson():
  return controller_suplier.suplierData()

@app_suplier.route('/suplier-json/<id_suplier>', methods=['GET'])
def suplierJsonDetails(id_suplier):
  return controller_suplier.suplierDataDetail(id_suplier)  # --- DETAIL SUPLIER --- #




# -----------------------------FRONTEND--------------------------------# 

@app_suplier.route('/')
def index():
    return redirect(url_for('suplier.home'))

@app_suplier.route('/home')
def home():
    return render_template('dashboard.html')
  
@app_suplier.route('/suplier')
def suplier():
    data = controller_suplier.suplierData()
    return render_template('suplier/suplier.html', suplier = data)
  


   


# @app_suplier.route('/suplier')
# def suplier():
#     return render_template('suplier/suplier.html')
  