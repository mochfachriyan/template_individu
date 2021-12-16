from app_pembelians import db
from flask import flash

class suplier(db.Model):
    # __tablename__ = 'suplier'
    id_suplier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_suplier = db.Column(db.String(30))
    no_telp = db.Column(db.String(15))
    alamat = db.Column(db.String(100))
    
    def __init__(self, nama_suplier, no_telp, alamat):
      self.nama_suplier  = nama_suplier
      self.no_telp       = no_telp
      self.alamat        = alamat
    
    def __repr__(self):
      return '<suplier {}>'.format(self.name)
    
def tambahSuplier(nama, no_tlp, alamat):
    new_suplier = suplier(nama, no_tlp, alamat)
    try:
        # Actually add this dessert to the database
        db.session.add(new_suplier)

        # Save all pending changes to the database
        db.session.commit()
        flash('You have successfully created a new suplier')
        return new_suplier
    except:
        return 'There was an issue adding suplier'