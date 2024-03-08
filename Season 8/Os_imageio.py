import os
import imageio

file_list = sorted(os.listdir("Season 8/images"))
IMAGES = []
for file_name in file_list:
    print(file_name)
    file_path = "Season 8/images/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)


imageio.mimsave("Season 8/my_output.gif", IMAGES)
