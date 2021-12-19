from app_pembelians.entry.pembelian import app_pembelian, controller_pembelian
from flask import render_template

@app_pembelian.route('/pembelian-json')
def pembelian_json():
    return controller_pembelian.pembelianDataJson()
  
@app_pembelian.route('/pembelian-data', methods=['GET', 'POST'])
def pembelian_data():
  return controller_pembelian.pembelianData()


@app_pembelian.route('/pembelian')
def pembelian():
  data = controller_pembelian.pembelianData()
  return render_template('pembelian/pembelian.html', pembelian = data)