import numpy as np
import sys
from PIL import Image

def convert_image_to_ascii(img, interval):
    img_data = downsize_image(np.asarray(img), interval)
    ascii_data = []
    ascii_chars = '@$#*!=;:~-,. '

    for row in img_data:
        ascii_row = []
        for rgb in row:
            bw = greyscale(rgb)
            ascii_char = ascii_chars[int(bw / 256 * len(ascii_chars))]
            ascii_row.append(ascii_char)
        ascii_data.append(ascii_row)

    return ascii_data

def downsize_image(img_data, interval):
    old_h = img_data.shape[0]
    old_w = img_data.shape[1]

    new_img_data = np.zeros((old_h // interval, old_w // interval, 3))

    for newy, y in enumerate(range(0, old_h - interval, interval)):
        for newx, x in enumerate(range(0, old_w - interval, interval)):
            color_sum = np.array([0, 0, 0])
            for yi in range(interval):
                for xi in range(interval):
                    color_sum = np.add(color_sum, img_data[y + yi][x + xi][:3])
            color_avg = np.divide(color_sum, interval * interval)

            new_img_data[newy][newx] = color_avg

    return new_img_data

def greyscale(rgb):
    return 0.3 * rgb[0] + 0.59 * rgb[1] + 0.11 * rgb[2]

    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Provide the single image file you would like to convert to ascii.')
    else:
        try:
            filename = sys.argv[1]
            supported_types = ['.jpg', '.png', '.jpeg']

            if not any(x for x in supported_types if filename.endswith(x)):
                print(f'Only the following filetypes are supported: {supported_types}.')
            else:
                with open(filename, 'r') as img_file:
                    interval = int(input('Interval: '))

                    if interval < 1:
                        print('Interval must be at least 1.')
                    else:
                        img = Image.open(sys.argv[1])
                        ascii_data = convert_image_to_ascii(img, interval)

                        with open('output.txt', 'w') as output_file:
                            for row in ascii_data:
                                for ascii_char in row:
                                    output_file.write(ascii_char)
                                output_file.write('\n')
        except FileNotFoundError:
            print(f"No image file '{arg}' exists.")
