from app_pembelians import db

class suplier(db.Model):
    # __tablename__ = 'suplier'
    id_suplier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_suplier = db.Column(db.String(30))
    no_telp = db.Column(db.String(15))
    alamat = db.Column(db.String(100))
    
    def __repr__(self):
      return '<suplier {}>'.format(self.name)