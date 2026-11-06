from app import create_app 

app=create_app()

@app.route('/welcome',methods=["GET"])
def index():
    
    return {"message":"Welcome to Camping-fun API"},200