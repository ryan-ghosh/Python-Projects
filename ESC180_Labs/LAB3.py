import utilities

def rotate_90_degrees(image_array, direction = 1):
    #1 for clock_wise. -1 for anticlockwise
    output_array = []
    row = []
    if direction == 1:
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[len(image_array) - 1 - j][i])
            output_array.append(row)
            row = []
    elif direction == -1:
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[j][len(image_array) - 1 - i])
            output_array.append(row)
            row = []
    return output_array

def flip_image(image_array, axis = 0):
    #axis = -1 (along x = y), 0 along y, 1 along x
    row = []
    output_array = []
    if axis == 0:
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[i][len(image_array) - 1 - j])
            output_array.append(row)
            row = []
    elif axis == 1:
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[len(image_array) - 1 - i][j])
            output_array.append(row)
            row = []
    elif axis == -1:
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[len(image_array) - 1 - j][len(image_array) - 1 - i])
            output_array.append(row)
            row = []
    return output_array

def invert_greyscale(image_array):
    output_array = []
    row = []
    for i in range(len(image_array)):
        for j in range(len(image_array[i])):
            row.append(255 - image_array[i][j])
        output_array.append(row)
        row = []
    return output_array

def crop(image_array, direction, n_pixels):
    output_array = []
    row = []
    if direction == 'left':
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[i][len(image_array) - 1 - n_pixels])
            output_array.append(row)
            row = []
    elif direction == 'right':
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[i][j + n_pixels])
            output_array.append(row)
            row = []
    elif direction == 'up':
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[len(image_array) - 1 - n_pixels][j])
            output_array.append(row)
            row = []
    elif direction == 'down':
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                row.append(image_array[i + n_pixels][j])
            output_array.append(row)
            row = []
    return output_array

def rgb_to_grayscale(rgb_image_array):
    output_array = []
    row = []
    for i in range(len(rgb_image_array)):
        for j in range(len(rgb_image_array)):
            row.append(rgb_image_array[i][0.2989 * r + 0.5870 * g + 0.1140 * b]
    output_array.append(row)
    row = []
    return output_array

def invert_rgb(image_array):
    element = []
    row = []
    output_array = []
    for i in range(len(image_array)):
        for j in range(len(image_array[i])):
            for k in range(3):
                element.append(255 - image_array[i][j][k])
            row.append(element)
            element = []
        output_array.append(row)
        row = []

    return output_array

if (__name__ == "__main__"):
    file = 'robot.png'
    utilities.write_image(rgb_to_grayscale(utilities.image_to_list(file)), 'gray.png')

