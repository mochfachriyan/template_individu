from app_pembelians.entry.barang import app_barang, controller_barang
from app_pembelians.entry.suplier import controller_suplier
from flask import render_template, url_for, redirect
  
@app_barang.route('/barang-json', methods=['GET'])
def barang_data():
  return controller_barang.barangDataJson()

@app_barang.route('/barang-json/<id_suplier>', methods=['GET'])
def barang_data_detail(id_suplier):
  return controller_barang.barangDataDetail(id_suplier)  # --- DETAIL BARANG --- #
  

# -----------------------------FRONTEND--------------------------------# 

# ---- BARANG TAMPILAN STATUS ---- #
status=[{'status' : 'Tersedia'},
        {'status' : 'Habis'}]

# READ BARANG
@app_barang.route('/barang')
def barang():
  barang = controller_barang.barangData()
  suplier = controller_suplier.suplierData()
  return render_template('barang/barang.html', barang=barang, suplier=suplier, status=status)

# TAMBAH SUPLIER  
@app_barang.route('/tambah-barang', methods=['GET', 'POST'])
def tambah_barang():
  return controller_barang.tambahBarang()

# EDIT SUPLIER  
@app_barang.route('/edit-barang/', methods=['GET', 'POST'])
def edit_barang():
  return controller_barang.editBarang()

# HAPUS SUPLIER  
@app_barang.route('/hapus-barang/<id_barang>', methods=['GET', 'POST'])
def hapus_barang(id_barang):
  return controller_barang.hapusBarang(id_barang)