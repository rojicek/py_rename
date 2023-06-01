# nic

import os
from datetime import datetime
import json
from PIL import Image, ExifTags
import shutil

dir_name = r'c:\Users\e675237\_moje_programy\py_rename\pics'
dir_name_new = r'c:\Users\e675237\_moje_programy\py_rename\pics_new'
dir_list = [os.path.join(dir_name, x) for x in os.listdir(dir_name)]
for full_name in dir_list:
    _, f = os.path.split(full_name)
    f1 = f[:f.rfind('.')]
    f_suffix = f[f.rfind('.') + 1:].lower()

    image_exif = Image.open(full_name)._getexif()

    if image_exif:
        # Make a map with tag names
        exif = {ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS and type(v) is not bytes}
        date_created = datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
        new_file_name = f'spejchar{date_created.year}-{str(date_created.month).zfill(2)}-{str(date_created.day).zfill(2)}.' + f_suffix
        full_new_name = os.path.join(dir_name_new, new_file_name)

        shutil.copyfile(full_name, full_new_name)

        # todo: plus modify timestamp jako jhead









# im = Image.open('path/to/image.jpg')
# exif = im.getexif()
# creation_time = exif.get(36867)
#
#
# folder_name = 'D:/Users/user/Desktop/Xiomi/100ANDRO/'
# dir_list = [os.path.join(folder_name, x) for x in os.listdir(folder_name)]
# #
# for file in dir_list:
#     filename, file_extension = os.path.splitext(file)
#     date = datetime.fromtimestamp(os.path.getctime(file)).strftime('%Y_%m_%d_%H_%M_%S')
#     os.rename(file, os.path.join(folder_name, date + file_extension))
#
#
# print(dir_list)
