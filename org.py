from sys import argv
from pathlib import Path
import shutil
import os
import zipfile

#fileType indentifier function 
def get_dir(filename):
    ext=filename.suffix[1:]
    if os.path.getsize(filename)>1000000000:
        ext="lrg"
    return dirs.get(ext,"Others")



#extension dictionary here
dirs={
     # Images
    "jpeg": "Images",
    "png": "Images",
    "jpg": "Images",
    "tiff": "Images",
    "gif": "Images",

    # Videos
    "mp4": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "webm": "Videos",
    "flv": "Videos",

    # Music
    "mp3": "Music",
    "ogg": "Music",
    "wav": "Music",
    "flac": "Music",

    # Program Files
    "py": "Program Files",
    "js": "Program Files",
    "cpp": "Program Files",
    "html": "Program Files",
    "css": "Program Files",
    "c": "Program Files",
    "sh": "Program Files",

    # Documents
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "ppt": "Documents",
    "ods": "Documents",
    "csv": "Documents",
    
    #pre-compressed 
    "rar":"Precompressed",
    "zip":"Precompressed",
    
    #executables
    "exe":"Executables",
    
    #Large files
    "lrg":"Large Files"
    

 }

if len(argv) !=2: 
    #take working default working directory as default
    print(argv)
    print("="*35)
    print("[ERROR] Invalid number of arguments were provided")
    print("rerun script again with the following format:")
    print(f"[Usage]python {Path(__file__).name}< put your dir_path> (make sure the directory in absolute and in quotation")
    print("="*35)
    exit(1)
print("organizing...")
print("="*35)
#path to Organize
PATH=Path(argv[1])
for filename in PATH.iterdir():    
    # get absolute path of the file to be organized
    PathToFile=filename.absolute()
    if filename.is_file():
        #create destination file
        destination=PATH / get_dir(filename)
        if not destination.exists():
            destination.mkdir()
        PathToFile=filename.absolute()
        shutil.move(str(PathToFile),str(destination))
print("="*35)
print("Organization Done!")
        
           




