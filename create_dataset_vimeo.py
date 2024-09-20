import os
from PIL import Image

def copy_images(source_folder, destination_folder):
    """
    Copies images from the source folder to the destination folder.

    Args:
        source_folder (str): The path to the source folder.
        destination_folder (str): The path to the destination folder.
    """

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    trainlist = []
    dir = sorted(os.listdir(source_folder))
    
    for i,filename in enumerate(dir):
      
      if i == len(dir) -2:
        break
      
      
      for j in range(i,i+3):
        source_path = os.path.join(source_folder, dir[j])
        print(source_path)
        cur_path = f"{destination_folder}/{i}"
        
        if not os.path.exists(cur_path):
          os.makedirs(cur_path)
        
        destination_path = os.path.join(cur_path,f"im{j-i+1}.png")
        img = Image.open(source_path)
        img.save(destination_path)
      trainlist.append(f"{destination_folder}/{i}")

    with open("tri_trainlist.txt", "w") as f:
      f.write("\n".join(trainlist))

# Example usage:
source_folder = "satImages"
destination_folder = "sequences"

copy_images(source_folder, destination_folder)