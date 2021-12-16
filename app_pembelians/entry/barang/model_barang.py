from app_pembelians import db

class barang(db.Model):
    # __tablename__ = 'barang'
    id_barang = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_barang = db.Column(db.String(30))
    harga = db.Column(db.Float)
    id_suplier = db.Column(db.Integer)
    keterangan = db.Column(db.String(200))
    
    def __repr__(self):
      return '<barang {}>'.format(self.name)