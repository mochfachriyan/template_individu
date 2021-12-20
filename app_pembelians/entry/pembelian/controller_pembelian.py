from app_pembelians.entry import pembelian
from app_pembelians.entry.pembelian import model_pembelian
from flask import jsonify, request, redirect, url_for, flash
from app_pembelians import db
import os

def pembelianDataJson(): # deff adalah function
  # select * FROM
  pembelian = model_pembelian.pembelian.query.all() # ini kalau di Oracle macem Select * from suplier
  data = formatArray(pembelian) #
  return jsonify(data) # ngereturn dari response.py kelas succes
  
# --------------------------------- DATA USER ------------------------------------------#
def userDataJson(): 
  user = model_pembelian.user.query.all()
  dataUser = user
  return jsonify(dataUser) 

def userData(): 
  user = model_pembelian.user.query.all()
  return user
    
# -------------------------------- MENAMPILKAN SEMUA DATA PEMBELIAN --------------------------------#
def pembelianData(): 
  pembelian = model_pembelian.joinPembelian()
  return pembelian   

# -------------------------------- TAMBAH DATA PEMBELIAN --------------------------------#
def tambahPembelian():
  id_user = request.form['id_user']
  id_barang = request.form['id_barang']
  
  pembelian = model_pembelian.pembelian(id_user, id_barang, '', '')
  db.session.add(pembelian)
  db.session.commit()   
  flash('You have successfully created a new Pembelian')
  return redirect(url_for('pembelian.pembelian'))

# -------------------------------- EDIT DATA PEMBELIAN --------------------------------#
def editPembelian():
  barang = model_pembelian.pembelian.query.get(request.form.get('id_pembelian'))
  barang.id_user = request.form['id_user']
  barang.id_barang  = request.form['id_barang']

  db.session.commit()
  flash("barang Updated Successfully")
  return redirect(url_for('pembelian.pembelian'))

# -------------------------------- HAPUS DATA PEMBELIAN --------------------------------#
def hapusPembelian(id_pembelian):
  pembelian = model_pembelian.pembelian.query.get(id_pembelian)
  db.session.delete(pembelian)
  db.session.commit()
  flash("pembelian Deleted Successfully")
  return redirect(url_for('pembelian.pembelian'))
    













# function untuk format array nya Dosen
def formatArray(datas):
  array = []
  for i in datas:
    array.append(singleObject(i)) # INGAT pelajaran di w3school tentang Lists, Tuples, Sets, DIctionaries ? nah ini method yang ada di Lists
  # menambahkan di arraynya
  # membuat Function singleDosen dulu
  return array


# function format untuk menampilkan Dosen
def singleObject(data):
  data={
  'id_pembelian':data.id_pembelian,
  'id_user':data.id_user,
  'id_barang':data.id_barang,
  'tanggal':data.tanggal,
  'keterangan':data.keterangan
  }
  return data