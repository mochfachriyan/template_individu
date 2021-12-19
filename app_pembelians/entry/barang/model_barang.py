from app_pembelians import db
from app_pembelians.entry.suplier import model_suplier

class barang(db.Model):
    # __tablename__ = 'barang'
    id_barang = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_barang = db.Column(db.String(30))
    harga = db.Column(db.Float)
    id_suplier = db.Column(db.Integer, db.ForeignKey('suplier.id_suplier'))
    status = db.Column(db.String(10))
    
    def __init__(self, nama_barang, harga, id_suplier, status):
      self.nama_barang = nama_barang
      self.harga       = harga
      self.id_suplier  = id_suplier
      self.status  = status
      
    def __repr__(self):
      return '<barang {}>'.format(self.id_barang)
    
# suplier = model_suplier.suplier.id_suplier    
# results = db.session.query(barang, model_suplier.suplier).join(model_suplier.suplier).all()

# for barang, model_suplier.suplier in results:
#   print(barang.id_suplier, model_suplier.suplier.nama_suplier)
    
def joinBarangSUplier():
  results = db.session.query(barang, model_suplier.suplier).join(model_suplier.suplier).all()
  return results