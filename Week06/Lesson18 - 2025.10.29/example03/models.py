from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    kitaplar = db.relationship("Kitap", backref="user", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Kategori {self.ad}>"


class Kategori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(100), nullable=False, unique=True)
    kitaplar = db.relationship("Kitap", backref="kategori", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Kategori {self.ad}>"


class Kitap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    baslik = db.Column(db.String(200), nullable=False)
    yazar = db.Column(db.String(100), nullable=False)
    kategori_id = db.Column(db.Integer, db.ForeignKey("kategori.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, default=1)

    def __repr__(self):
        return f"<Kitap {self.baslik}>"
