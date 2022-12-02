from main import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    likes = db.Column(db.Integer, default=0)
    reason = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "likes": self.likes,
            "reason": self.reason
        }
