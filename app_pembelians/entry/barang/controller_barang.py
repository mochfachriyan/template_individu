from werkzeug.wrappers import request
from app_pembelians import response
from app_pembelians.entry import barang
from app_pembelians.entry.barang import model_barang
from app_pembelians.entry.suplier import controller_suplier, model_suplier
from flask import jsonify, request, flash, redirect, url_for
from app_pembelians import db


# ---------------------------MENAMPILKAN SEMUA DATA BARANG--------------------------------#
def barangDataJson(): 
  barang = model_barang.barang.query.all() # ini kalau di Oracle seperti Select * from barang
  data = formatArray(barang) 
  return response.success(data, "success")


def barangData(): 
  query = model_barang.joinBarangSUplier()
  return query

# -------------------------------- TAMBAH DATA BARANG --------------------------------#
def tambahBarang():
  nama_barang = request.form['nama']
  harga = request.form['harga']
  id_suplier = request.form['id_suplier']
  status = request.form['status']
  
  barang = model_barang.barang(nama_barang,harga,id_suplier,status)
  db.session.add(barang)
  db.session.commit()   
  flash('You have successfully created a new Barang')
  return redirect(url_for('barang.barang'))

# -------------------------------- EDIT DATA SUPLIER --------------------------------#
def editBarang():
  barang = model_barang.barang.query.get(request.form.get('id_barang'))
  barang.nama_barang = request.form['nama']
  barang.harga  = request.form['harga']
  barang.id_suplier = request.form['id_suplier']
  barang.status = request.form['status']

  db.session.commit()
  flash("barang Updated Successfully")
  return redirect(url_for('barang.barang'))

# -------------------------------- HAPUS DATA SUPLIER --------------------------------#
def hapusBarang(id_barang):
  barang = model_barang.barang.query.get(id_barang)
  db.session.delete(barang)
  db.session.commit()
  flash("Barang Deleted Successfully")
  return redirect(url_for('barang.barang'))
   

# ---------------------------MENAMPILKAN DETAIL DATA BARANG--------------------------------#    
# def barangDataDetail(id): 
#   try:
#     suplier = model_suplier.suplier.query.filter_by(id_suplier=id) # ini kalau di Oracle seperti Select * from barang
#     data = formatArray(suplier)  
    
#     if not barang: 
#       return response.badRequest([], 'Data Barang tidak ada !!')
    
#     # suplier = controller_suplier.suplierDataDetail(id_suplier)
#     return response.success(data, "success")
#   except Exception as e: 
#     print(e)
    





# function untuk format array nya data barang
def formatArray(datas):
  array = []
  for i in datas:
    array.append(singleObject(i)) # INGAT pelajaran di w3school tentang Lists, Tuples, Sets, DIctionaries ? nah ini method yang ada di Lists
  # menambahkan di arraynya
  # membuat Function singleObject dulu
  return array

# function format untuk menampilkan semua data siplier
def singleObject(data):
  data={
    'id_barang':data.id_barang,
    'nama_barang':data.nama_barang,
    'harga':data.harga,
    'id_suplier':data.id_suplier,
    'status':data.status
  }
  return data




        
