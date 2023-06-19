from PIL import Image
import os

if __name__ == '__main__':
    # Create skins directory if it doesn't exist
    if not os.path.exists('skins'):
        os.makedirs('skins')

    # Set base skin
    skin_image = Image.open('skin.png').convert('RGBA')
    rect = Image.new('RGBA', (8,8), (255, 255, 255, 0)) # Remove outer-layer face
    skin_image.paste(rect, (40,8))
    input_image = Image.open('map.png')

    # Main loop
    x_position = 0
    y_position = 0
    i = 0
    for face_y in range(3):
        for face_x in range(9):
            if i != 0: # Skip first
                # Calculate the coordinates of the current face
                x1 = face_x * 8
                y1 = face_y * 8
                x2 = x1 + 8
                y2 = y1 + 8

                # Crop the input image to the current face
                face_image = input_image.crop((x1, y1, x2, y2))

                # Create a new image with the same dimensions as the face
                output_image = Image.new('RGBA', (8, 8))

                # Paste the face image onto the output image
                output_image.paste(face_image)

                # Calculate the position to paste the face onto the background image
                paste_x = x_position + face_x * 8
                paste_y = y_position + face_y * 8

                # Paste the face onto the background image
                skin_image.paste(output_image, (8,8), output_image)
                file_name = f'skins/skin_{i}.png'
                skin_image.save(file_name)
            i += 1
