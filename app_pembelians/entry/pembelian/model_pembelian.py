from app_pembelians import db

class pembelian(db.Model):
    # __tablename__ = 'pembelian'
    id_pembelian = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    id_barang = db.Column(db.Integer)
    tanggal = db.Column(db.DateTime)
    keterangan = db.Column(db.String(200))
   
    def __init__(self, id_user, id_barang, tanggal, keterangan):
      self.id_user       = id_user
      self.id_barang  = id_barang
      self.tanggal  = tanggal
      self.keterangan  = keterangan
    
    def __repr__(self):
      return '<pembelian {}>'.format(self.id_pembelian)
    
    
class user(db.Model):
    # __tablename__ = 'user'  
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(25))
    username = db.Column(db.String(25))
    password = db.Column(db.String(25))
    email = db.Column(db.String(25))
    
    def __init__(self, nama, username, password, email):
      self.nama       = nama
      self.username  = username
      self.password  = password
      self.email  = email
    
    def __repr__(self):
      return '<user {}>'.format(self.id_user)
    

# tes = db.session.query(pembelian, user).join(user).all()

# def joinPembelianUSer():
#   results = db.session.query(pembelian, user).join(user).all()
#   data = results
#   return data

# for pembelian, user in tes:
#   print(pembelian.id_user, user.nama)