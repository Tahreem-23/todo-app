from app import create,db
app=create()
with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)