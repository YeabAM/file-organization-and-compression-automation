from sys import argv
from pathlib import Path
import shutil
import os
import zipfile

#fileType indentifier function 
def get_dir(filename):
    ext=filename.suffix[1:]
    return dirs.get(ext,"Others")
#compressor function
def com_file(filename,path):
    dir=get_dir(filename)
    Finalname=filename
    if not dir=="Pcompressed" and os.path.getsize(filename)>300000000:
    
        Zipname=os.path.basename(filename).split(".")
        Zipname=Zipname[0]
        Zipname=Zipname + ".zip"
        print("compressing...")
    
        newZip=zipfile.ZipFile(Zipname,'w')
        newZip.write(filename,compress_type=zipfile.ZIP_DEFLATED)
        newZip.close
        Finalname=Zipname
        shutil.move(str(os.path.abspath(Finalname)),str(path))
    return Finalname


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
    "rar":"Pcompressed",
    "zip":"Pcompressed",
    
    #executables
    "exe":"Executables"
    

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
    #get absolute path of the file to be organized
    # PathToFile=filename.absolute()
    if filename.is_file():
        filepath=com_file(filename,PATH)
        filepath=Path(filepath)
        print("file path:",os.path.abspath(filepath))
        #create destination file
        # destination=PATH / get_dir(filename)
        # if not destination.exists():
        #     destination.mkdir()
        # filename=Path(com_file(filename))
        # PathToFile=filename.absolute()
        # print("path to file:",PathToFile)
        # shutil.move(str(PathToFile),str(destination))
print("="*35)
print("Organization Done!")
        
           




