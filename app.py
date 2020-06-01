from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

from common import get_tensor

from inference import get_type

# @app.route('/')
# def main():
#     return render_template('index.html')

@app.route('/')
def main():
    return render_template('base.html')


@app.route('/eff')
def mn():
    

    return render_template('ext.html')
@app.route('/s')
def s():
    

    return render_template('s.html')



@app.route('/h', methods=['GET','POST'])

def h():
    if request.method=='GET':
        return render_template('up.html', value="ddi")
    if request.method=='POST':
        if 'canbe anything' not in request.files:
            print("file not uploaded")
        file = request.files['canbe anything']
        image = file.read()
        
        
        category=get_type(image_bytes=image)
        if category=='마른남자':        
    
            return render_template('result.html', result=category)
        
        elif category=='남자비만':
            return render_template('result1.html', result=category)
        
        elif category=='정상남자':
            return render_template('result2.html', result=category)
       
        elif category=='마른여자':
            return render_template('result3.html', result=category)
        
        elif category=='여자비만':
            return render_template('result4.html', result=category)
        
        elif category=='정상여자':
            return render_template('result5.html', result=category)

@app.route('/ex')
def ex():
    

    return render_template('ex.html')


if __name__ == "__main__":
    #app.run(host='0.0.0.0' , debug=True)
    app.run(debug=True)
    #app.run(debug=True, port=os.getenv('PORT',5000))
