from project import db
 
 
subs=db.Table('subs',
    db.Column('author_id',db.Integer,db.ForeignKey('author.author_id'),primary_key=True),
    db.Column('book_id',db.Integer,db.ForeignKey('book.book_id'),primary_key=True),extend_existing=True,
)

class Author(db.Model):

    author_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

    books = db.relationship('Book',secondary=subs,back_populates='books')

class Book(db.Model):

    book_id=db.Column(db.Integer,primary_key=True)
    book_name=db.Column(db.String(50)) 

    authors = db.relationship('Author',secondary=subs,back_populates='authors')   