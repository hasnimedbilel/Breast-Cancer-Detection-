import base64
import io
import sys
from PIL import Image
from flask import request
from flask import jsonify
from flask import Flask


app = Flask(__name__)

print "hahahahaha"
@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    image.save("./received.jpg")
    sys.argv[1] = "./received.jpg"
    import label_image
    
    response = {
        'prediction' : {
            'tumor' : str(label_image.predictions[0][0]),
            
            'normal' : str(label_image.predictions[0][1])
            
        }
    }
    
    return jsonify(response)
    
