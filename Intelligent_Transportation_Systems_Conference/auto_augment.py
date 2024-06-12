import Automold as am
import Helpers as hp
import numpy as np
from PIL import Image
import os

if __name__ == "__main__":
    #radius = [250, 300, 350]
    intensity = ['drizzle', 'heavy', 'torrential']
    coeff = [0.3, 0.5, 0.7, 0.9]

    #folder_names = ["exp{:02d}".format(i) for i in range(1)]
    folder_names = ["00"]
    for folder in folder_names:

        output_folders = [f'fog_{coeff[0]}',
                          f'fog_{coeff[1]}',
                          f'fog_{coeff[2]}',
                          f'bright_{coeff[0]}',
                          f'bright_{coeff[1]}',
                          f'bright_{coeff[2]}',
                          f'bright_{coeff[3]}',
                          f'dark_{coeff[0]}',
                          f'dark_{coeff[1]}',
                          f'dark_{coeff[2]}',
                          f'dark_{coeff[3]}',
                          f'rain_{intensity[0]}',
                          f'rain_{intensity[1]}',
                          f'rain_{intensity[2]}'
                          ]
        for f in output_folders:
            out_path = os.path.join('correct_images', f'exp{folder}')
            if not os.path.exists(out_path + '_w_' + f):
                os.makedirs(out_path + '_w_' + f)
            if not os.path.exists(out_path + '_d_' + f):
                os.makedirs(out_path + '_d_' + f)

        print(out_path)
        wheelchair_path = os.path.join(out_path, 'wheelchair')
        for filename in os.listdir(wheelchair_path):
            print(filename)
            if filename.endswith('.png'):
                image_path = os.path.join(wheelchair_path, filename)
                image = Image.open(image_path)

                for item in coeff:
                    output_folder = os.path.join('correct_images', f'exp{folder}_w_bright_{item}')
                    bright_image = am.brighten(np.array(image), brightness_coeff=item)
                    bright_image_pil = Image.fromarray(bright_image)
                    output_filename = os.path.splitext(filename)[0] + '_bright_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    bright_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")

                for item in coeff:
                    output_folder = os.path.join('correct_images', f'exp{folder}_w_dark_{item}')
                    dark_image = am.darken(np.array(image), darkness_coeff=item)
                    dark_image_pil = Image.fromarray(dark_image)
                    output_filename = os.path.splitext(filename)[0] + '_dark_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    dark_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")

                for item in coeff[:-1]:
                    output_folder = os.path.join('correct_images', f'exp{folder}_w_fog_{item}')
                    fog_image = am.add_fog(np.array(image), fog_coeff=item)
                    fog_image_pil = Image.fromarray(fog_image)
                    output_filename = os.path.splitext(filename)[0] + '_fog_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    fog_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")
                
                for item in intensity:
                    output_folder = os.path.join('correct_images', f'exp{folder}_w_rain_{item}')
                    rain_image = am.add_rain(np.array(image), rain_type=item)
                    rain_image_pil = Image.fromarray(rain_image)
                    output_filename = os.path.splitext(filename)[0] + '_rain_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    rain_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")
                
        drone_path = os.path.join(out_path, 'drone')
        for filename in os.listdir(drone_path):
            if filename.endswith('.png'):
                image_path = os.path.join(drone_path, filename)
                image = Image.open(image_path)

                for item in coeff:
                    output_folder = os.path.join('correct_images', f'exp{folder}_d_bright_{item}')
                    bright_image = am.brighten(np.array(image), brightness_coeff=item)
                    bright_image_pil = Image.fromarray(bright_image)
                    output_filename = os.path.splitext(filename)[0] + '_bright_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    bright_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")

                for item in coeff:
                    output_folder = os.path.join('correct_images', f'exp{folder}_d_dark_{item}')
                    dark_image = am.darken(np.array(image), darkness_coeff=item)
                    dark_image_pil = Image.fromarray(dark_image)
                    output_filename = os.path.splitext(filename)[0] + '_dark_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    dark_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")

                for item in coeff[:-1]:
                    output_folder = os.path.join('correct_images', f'exp{folder}_d_fog_{item}')
                    fog_image = am.add_fog(np.array(image), fog_coeff=item)
                    fog_image_pil = Image.fromarray(fog_image)
                    output_filename = os.path.splitext(filename)[0] + '_fog_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    fog_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")
                
                for item in intensity:
                    output_folder = os.path.join('correct_images', f'exp{folder}_d_rain_{item}')
                    rain_image = am.add_rain(np.array(image), rain_type=item)
                    rain_image_pil = Image.fromarray(rain_image)
                    output_filename = os.path.splitext(filename)[0] + '_rain_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    rain_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")

                
"""
                for item in radius:
                    output_folder = os.path.join('automatic_augmentation', f'{folder}_w_sun_{item}')
                    sun_image = am.add_sun_flare(np.array(image), src_radius=item, flare_center = (280,100), angle=2)
                    sun_image_pil = Image.fromarray(sun_image)
                    output_filename = os.path.splitext(filename)[0] + '_sun_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    sun_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")
        
                
                for item in coeff:
                    output_folder = os.path.join('automatic_augmentation', f'{folder}_w_dark_{item}')
                    dark_image = am.darken(np.array(image), darkness_coeff=item)
                    dark_image_pil = Image.fromarray(dark_image)
                    output_filename = os.path.splitext(filename)[0] + '_dark_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    dark_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")

                for item in coeff:
                    output_folder = os.path.join('automatic_augmentation', f'{folder}_w_bright_{item}')
                    bright_image = am.brighten(np.array(image), brightness_coeff=item)
                    bright_image_pil = Image.fromarray(bright_image)
                    output_filename = os.path.splitext(filename)[0] + '_bright_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    bright_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")



        

                for item in coeff:
                    output_folder = os.path.join('automatic_augmentation', f'{folder}_d_dark_{item}')
                    dark_image = am.darken(np.array(image), darkness_coeff=item)
                    dark_image_pil = Image.fromarray(dark_image)
                    output_filename = os.path.splitext(filename)[0] + '_dark_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    dark_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")

                for item in coeff:
                    output_folder = os.path.join('automatic_augmentation', f'{folder}_d_bright_{item}')
                    bright_image = am.brighten(np.array(image), brightness_coeff=item)
                    bright_image_pil = Image.fromarray(bright_image)
                    output_filename = os.path.splitext(filename)[0] + '_bright_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    bright_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")




                


                for item in intensity:
                    output_folder = os.path.join('automatic_augmentation', f'{folder}_w_rain_{item}')
                    rain_image = am.add_rain(np.array(image), rain_type=item)
                    rain_image_pil = Image.fromarray(rain_image)
                    output_filename = os.path.splitext(filename)[0] + '_rain_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    rain_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")


                for item in radius:
                    output_folder = os.path.join('automatic_augmentation', f'{folder}_d_sun_{item}')
                    sun_image = am.add_sun_flare(np.array(image), src_radius=item)
                    sun_image_pil = Image.fromarray(sun_image)
                    output_filename = os.path.splitext(filename)[0] + '_sun_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    sun_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")


                for item in intensity:
                    output_folder = os.path.join('automatic_augmentation', f'{folder}_d_rain_{item}')
                    rain_image = am.add_rain(np.array(image), rain_type=item)
                    rain_image_pil = Image.fromarray(rain_image)
                    output_filename = os.path.splitext(filename)[0] + '_rain_' + str(item) + '.png'
                    output_path = os.path.join(output_folder, output_filename)
                    rain_image_pil.save(output_path)
                    print(f"Processed image '{filename}' and saved as '{output_filename}' in '{output_folder}'")
"""