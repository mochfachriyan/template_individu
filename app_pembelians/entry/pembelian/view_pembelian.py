from app_pembelians.entry.pembelian import app_pembelian, controller_pembelian
from app_pembelians.entry.suplier import controller_suplier 
from app_pembelians.entry.barang import controller_barang 
from flask import render_template

@app_pembelian.route('/pembelian-json')
def pembelian_json():
    return controller_pembelian.pembelianDataJson()
  
@app_pembelian.route('/pembelian-data', methods=['GET', 'POST'])
def pembelian_data():
  return controller_pembelian.pembelianData()

# READ PEMBELIAN
@app_pembelian.route('/pembelian')
def pembelian():
  pembelian = controller_pembelian.pembelianData()
  user = controller_pembelian.userData()
  barang = controller_barang.barangData()
  return render_template('pembelian/pembelian.html', pembelian = pembelian, user = user, barang = barang)

# TAMBAH PEMBELIAN
@app_pembelian.route('/tambah-pembelian', methods=['GET', 'POST'])
def tambah_pembelian():
  return controller_pembelian.tambahPembelian()

# EDIT PEMBELIAN  
@app_pembelian.route('/edit-pembelian/', methods=['GET', 'POST'])
def edit_pembelian():
  return controller_pembelian.editPembelian()

# HAPUS PEMBELIAN  
@app_pembelian.route('/hapus-pembelian/<id_pembelian>', methods=['GET', 'POST'])
def hapus_pembelian(id_pembelian):
  return controller_pembelian.hapusPembelian(id_pembelian)