import os
import shutil
import xml.etree.ElementTree as ET

# path to xml-file
train_xml_path = "dl_project-1/svt1/test.xml"

image_folder_path = "dl_project-1/svt1/img"
# output folder for the train/test images
output_folder_path = "dl_project-1/svt1/test"


if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)


tree = ET.parse(train_xml_path)
root = tree.getroot()

# loop over the images in the xml file
for image in root.findall('image'):

    image_name = image.find('imageName').text.split('/')[-1]
    image_path = os.path.join(image_folder_path, image_name)
    

    """
    image_folder = os.path.join(output_folder_path, image_name.split('.')[0])
    os.makedirs(image_folder, exist_ok=True)
    """
    image_folder = output_folder_path
    os.makedirs(image_folder,exist_ok=True)

    shutil.copy(image_path, image_folder)
    
    # bounding box information to a text file in the image folder
    bbox_file = os.path.join(image_folder, 'bbox.txt')
    with open(bbox_file, 'w') as f:
        for rect in image.findall('.//taggedRectangle'):
            x = rect.get('x')
            y = rect.get('y')
            width = rect.get('width')
            height = rect.get('height')
            tag = rect.find('tag').text
            f.write(f'{tag} {x} {y} {width} {height}\n')