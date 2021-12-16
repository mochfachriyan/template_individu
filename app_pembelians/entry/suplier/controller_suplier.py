from app_pembelians.entry import suplier
from app_pembelians import response
from app_pembelians.entry.barang import controller_barang, model_barang
from app_pembelians.entry.suplier import model_suplier
from flask import jsonify, request, redirect, url_for


# -------------------------------- MENAMPILKAN SEMUA DATA SUPLIER --------------------------------#
def suplierData(): # deff adalah function
  # select * FROM
  suplier = model_suplier.suplier.query.all() # ini kalau di Oracle macem Select * from suplier
  return suplier # ngereturn dari response.py kelas succes
 
# -------------------------------- MENAMPILKAN DETAIL DATA SUPLIER --------------------------------#
def suplierDataDetail(id_suplier):
  suplier = model_suplier.suplier.query.filter_by(id_suplier=id_suplier)
  data = formatArray(suplier) #
  return jsonify(data) # ngereturn dari response.py kelas succes

# -------------------------------- TAMBAH DATA SUPLIER --------------------------------#
def tambahSuplier():
  if request.method == 'POST':
    # Create variables for easy access
    nama_suplier = request.form['nama']
    no_telp = request.form['no_tlp']
    alamat = request.form['alamat']
    
    model_suplier.tambahSuplier(nama_suplier, no_telp, alamat)
    return redirect(url_for('suplier.suplier'))
  else:
    # memakai modal di halaman yang sama
    return redirect(url_for('suplier.suplier'))



# function format array
def formatArray(datas):
  array = []
  for i in datas:
    array.append(singleObject(i)) # INGAT pelajaran di w3school tentang Lists, Tuples, Sets, DIctionaries ? nah ini method yang ada di Lists
  # menambahkan di arraynya
  # membuat Function singleDosen dulu
  return array

# function format suplier
def singleObject(data):
  data={
    'id_suplier':data.id_suplier,
    'nama_suplier':data.nama_suplier,
    'no_telp':data.no_telp,
    'alamat':data.alamat
  }
  return data
