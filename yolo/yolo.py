from ultralytics import YOLO
from pathlib import Path
from PIL import Image
import json
import os 

def detect_objects(image_path):
    # YOLO model loading code
    model = YOLO('D:\Food Detection\weights26.pt')

    # Perform object detection and get the result image
    results = model.predict(image_path,imgsz=640)

    result_image_path = f'static/uploads/result_{Path(image_path).name}'

    objects = None

    # Show the results
    for r in results:
      
        r.names = {
            0: 'Indian Bread (85-448 cal per unit)',
            1: 'Rasgulla (106 cal per unit)',
            2: 'Biryani (187 cal per bowl)',
            3: 'Uttapam (227 cal per unit)',
            4: 'Paneer (225 cal per bowl)',
            5: 'Poha (137 cal per bowl)',
            6: 'Khichdi (125 cal per bowl)',
            7: 'Egg Omelette (127 cal per egg)',
            8: 'Rice (120 cal per bowl)',
            9: 'Dal Makhani (278 cal per serving)',
            10: 'Rajma Tadka (121 cal per bowl)',
            11: 'Puri (134 cal per unit)',
            12: 'Chole (173 cal per bowl)',
            13: 'Dal Fry (127 cal per bowl)',
            14: 'Sambar (114 cal per bowl)',
            15: 'Papad (29 cal per unit)',
            16: 'Gulab Jamun (175 cal per unit)',
            17: 'Idli (73 cal per unit)',
            18: 'Vada (155 cal per unit)',
            19: 'Dosa (147 cal per unit)',
            20: 'Fries (365 cal per serving)',
            21: 'Burger (391 cal per unit)',
            22: 'chai (62 cal per cup)',
            23: 'samosa (262 cal per unit)',
            24: 'Noodles (300 cal per serving)',
            25: 'Dumplings (71.8 cal per unit)'
        }
    
        j = r.tojson()
        j_dict = json.loads(j)
        obj_dict = dict()
        for i in j_dict:
            if i['name'] not in obj_dict.keys():
                obj_dict[i['name']] = 1
            else:
                obj_dict[i['name']] += 1
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save(result_image_path)  # save image

    # Return the result image path
    return result_image_path, obj_dict