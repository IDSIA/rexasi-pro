import os
import csv
from ultralytics import YOLO
import cv2
import numpy as np

exp = ['8']
for e in exp:
    folders = [f'{e}/exp0{e}_wheelchair', f'{e}/exp0{e}_drone',
               f'{e}/exp0{e}_d_bright_0.3', f'{e}/exp0{e}_d_bright_0.5', f'{e}/exp0{e}_d_bright_0.7',
               f'{e}/exp0{e}_d_dark_0.3', f'{e}/exp0{e}_d_dark_0.5', f'{e}/exp0{e}_d_dark_0.7',
               f'{e}/exp0{e}_d_fog_0.3', f'{e}/exp0{e}_d_fog_0.5', f'{e}/exp0{e}_d_fog_0.7',
               f'{e}/exp0{e}_d_rain_drizzle', f'{e}/exp0{e}_d_rain_heavy', f'{e}/exp0{e}_d_rain_torrential',
               f'{e}/exp0{e}_w_bright_0.3', f'{e}/exp0{e}_w_bright_0.5', f'{e}/exp0{e}_w_bright_0.7',
               f'{e}/exp0{e}_w_dark_0.3', f'{e}/exp0{e}_w_dark_0.5', f'{e}/exp0{e}_w_dark_0.7',
               f'{e}/exp0{e}_w_fog_0.3', f'{e}/exp0{e}_w_fog_0.5', f'{e}/exp0{e}_w_fog_0.7',
               f'{e}/exp0{e}_w_rain_drizzle', f'{e}/exp0{e}_w_rain_heavy', f'{e}/exp0{e}_w_rain_torrential']

    for item in folders:
        images_folder = f'{item}'
        output_folder = f'exp{item}-processed'


        model_path = os.path.join('.', 'runs', 'detect', 'train13', 'weights', 'best.pt')
        threshold = 0.01
        model = YOLO(model_path)

        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(f'csvs_{e}', exist_ok=True)

        # Open a CSV file for writing
        name = item.replace('/', '-')

        with open(f'csvs_{e}_bis/bbox_widths_{name}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['index', 'Bounding Box Width'])

            for idx, image_name in enumerate(os.listdir(images_folder)):
                image_path = os.path.join(images_folder, image_name)
                image = cv2.imread(image_path)
                results = model(image)[0]
                #if y1<30:
                    #if len(model(image))>1:
                        #results = model(image)[1]
                    #else:
                        #results = np.nan
                box_width = np.nan

                
                if results is not np.nan:# Iterate over detected objects
                    for result in results.boxes.data.tolist():
                        
                        x1, y1, x2, y2, score, class_id = result
                        if y2 < 280:
                            continue

                        if score > threshold:
                            # Calculate bounding box width
                            box_width = abs(x2 - x1)
                            #height, width, _ = image.shape
                            # Draw bounding box on the image
                            #cv2.line(image, (0, 280), (width - 1, 280), (0, 0, 255), thickness=2)
                            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)


                writer.writerow([idx, box_width])  # Uncommented this line

                # Save the processed image with bounding boxes
                output_path = os.path.join(output_folder, f"processed_{image_name}")
                cv2.imwrite(output_path, image)