from . import db


class Uid(db.Model):
    __table_name__ = "random-uid-data"
    id = db.Column(db.Integer, primary_key=True)

    data = db.Column(db.String(64), index=False, nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.data}"
