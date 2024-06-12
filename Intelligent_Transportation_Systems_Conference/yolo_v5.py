import os
import csv
import cv2
import numpy as np
import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

exp = '14'  # Change the experiment number here
e = 14
# Define folders for different experiments

folders_old = [f'exp{exp}_wheelchair', f'exp{exp}_drone',
           f'exp{exp}_d_bright_0.3', f'exp{exp}_d_bright_0.5', f'exp{exp}_d_bright_0.7',
           f'exp{exp}_d_dark_0.3', f'exp{exp}_d_dark_0.5', f'exp{exp}_d_dark_0.7',
           f'exp{exp}_d_fog_0.3', f'exp{exp}_d_fog_0.5', f'exp{exp}_d_fog_0.7',
           f'exp{exp}_d_rain_drizzle', f'exp{exp}_d_rain_heavy', f'exp{exp}_d_rain_torrential',
           f'exp{exp}_w_bright_0.3', f'exp{exp}_w_bright_0.5', f'exp{exp}_w_bright_0.7',
           f'exp{exp}_w_dark_0.3', f'exp{exp}_w_dark_0.5', f'exp{exp}_w_dark_0.7',
           f'exp{exp}_w_fog_0.3', f'exp{exp}_w_fog_0.5', f'exp{exp}_w_fog_0.7',
           f'exp{exp}_w_rain_drizzle', f'exp{exp}_w_rain_heavy', f'exp{exp}_w_rain_torrential']

folders = [f'exp{exp}_d_bright_0.9', f'exp{exp}_w_bright_0.9',
           f'exp{exp}_d_dark_0.9', f'exp{exp}_w_dark_0.9']

# Iterate over experiment folders
for item in folders:
    images_folder = os.path.join(f'E://extreme/{e}', item)
    output_folder = f'exp{exp}_{item}-processed0.9'

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Path for CSV file
    csv_folder = f'csvs_exp{exp}'
    os.makedirs(csv_folder, exist_ok=True)
    name = item.replace('/', '-')
    csv_file = os.path.join(csv_folder, f'bbox_widths_{name}.csv')

    # Open a CSV file for writing
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['index', 'Bounding Box Width'])

        # Iterate over images in the folder
        for idx, image_name in enumerate(os.listdir(images_folder)):
            image_path = os.path.join(images_folder, image_name)
            image = cv2.imread(image_path)

            # Perform object detection
            results = model(image)

            # Process each detected object
            for detection in results.xyxy[0]:
                x1, y1, x2, y2, conf, class_id = detection
                
                if x2 < 50:
                    continue
                # Filter objects based on class ID
                if model.names[int(class_id)] == 'motorcycle':
                    # Calculate bounding box width
                    box_width = abs(x2 - x1)

                    # Draw bounding box on the image
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

                    # Write bounding box width to CSV
                    print(idx)
                    print(box_width.item())
                    writer.writerow([idx, box_width.item()])
            
            # Save the processed image with bounding boxes
            output_path = os.path.join(output_folder, f"processed_{image_name}")
            cv2.imwrite(output_path, image)
    
    print(f"Finished processing folder: {item}")
