from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

from common import get_tensor

from inference import get_type

@app.route('/')
def main():
    return render_template('index.html')



@app.route('/h', methods=['GET','POST'])

def h():
    if request.method=='GET':
        return render_template('upload.html', value="ddi")
    if request.method=='POST':
        if 'canbe anything' not in request.files:
            print("file not uploaded")
        file = request.files['canbe anything']
        image = file.read()
        
        
        category=get_type(image_bytes=image)        
    
        return render_template('result.html', resultr=category)


if __name__ == "__main__":
    #app.run(host='0.0.0.0' , debug=True)
    app.run(debug=True)
    #app.run(debug=True, port=os.getenv('PORT',5000))
