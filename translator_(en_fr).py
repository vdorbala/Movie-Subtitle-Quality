# To get the id part of the file
import xlrd
import pdb
# Authenticate and create the PyDrive client
# auth.authenticate_user()
# gauth = GoogleAuth()
# gauth.credentials = GoogleCredentials.get_application_default()
# drive = GoogleDrive(gauth)

# from google.colab import drive
# drive.mount('/content/drive/')



import os
from tqdm import tqdm
path = "./subs/en/"
tar="./subs/en-fr"
dir_list = sorted(os.listdir(path))
present_list = os.listdir(tar)
present_list = [item.strip(".txt") for item in present_list]
print(present_list)
  
print("Files and directories in '", path, "' :") 
  
# print the list
print(dir_list)

from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr", device=0)

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Movie NLP Project/subs/en
for filename in tqdm(dir_list):
  try:
    if filename.strip(".en") in present_list:
      print("Skipping {}",format(filename))
      continue

    if not filename.endswith('.en'):
      continue
    t_path = os.path.join("./subs/en-fr/",os.path.splitext(filename)[0]+".txt")
    file = open(path + filename, mode='r')
    text = file.readlines()
    numlines = len(text)

    print("Movie is {}".format(filename))

    with open(t_path,'w+') as f:
      for linenum in tqdm(range(numlines)):
        t = translator(text[linenum])
        # print(linenum)
        f.write(t[0].get('translation_text')+'\n')
    f.close()

  except KeyboardInterrupt as e:
    pdb.set_trace()