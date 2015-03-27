from app import db
from models import BlogPost

# Create sqlite database in filesystem
db.create_all()

# Add first few posts
db.session.add(BlogPost("Well", "I am well!"))
db.session.add(BlogPost("Good", "I am good!"))
db.session.commit()
