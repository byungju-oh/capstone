
from common import get_tensor,get_body

import json


model = get_body()

def get_type(image_bytes):
    tensor = get_tensor(image_bytes)
    outputs = model.forward(tensor)
    
    _,prediction= outputs.max(1)
    category = prediction.item() 
    
    
    if category ==0:
        ty='마른남자'
    elif category ==1:
        ty='남자비만'
    elif category ==2:
        ty='정상남자'
    elif category ==3:
        ty='마른여자'
    elif category == 4:
        ty='여자비만'
    else:
        ty='정상여자'


   
    return ty
    
