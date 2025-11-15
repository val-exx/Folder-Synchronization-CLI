from pathlib import Path
import shutil
from datetime import datetime
import filecmp
from filecmp import dircmp
import os

def sync_folders(source, dest, delete = False):
    source_path = Path(source)
    dest_path = Path(dest)

    #IF SOURCE FOLDER DOES NOT EXIST, STOP THE PROGRAM
    if not source_path.exists():
        print(f"Source folder {source} does not exist!")
        return
    
    #ID DESTINATION FOLDER/BACKUP DOES NOT EXISTS, CREATE DEFAULT BACKUPFOLDER IN THE SAME PARENT DIRECTORY OF SOURCE FOLDER
    if not dest_path.exists():
        print(f"Destination folder {dest} does not exists.. creating")
        dest_path = Path(source).parent / "backup"
        print(f"Default backup folder {dest_path} created!")
        dest_path.mkdir()

    FileUpdated = list()
    FileCopied = list ()
    FileDeleted = list ()

    #COPY OR UPDATE FILE FROM SOURCE TO DESTINATION
    for item in source_path.iterdir():
        if item.is_file():
            item_to_search = dest_path / item.name #file to search in destination
            
            if item_to_search.exists(): #the file exists in destination folder
                if not filecmp.cmp(item, item_to_search,shallow=False): #if files are not the same, update it
                    print(f"{item.name} updating in destination folder..")
                    FileUpdated.append(str(item.name+"\n"))
                    shutil.copy2(item,item_to_search)
            
            else: #the file does not exist in destination folder
                print(f"{item.name} does not exist in destination folder.. copying")
                FileCopied.append(str(item.name+"\n"))
                shutil.copy2(item,item_to_search)

    #now consider that in source folder, some files do not exists anymore, but still present in backup folder
    #remove "obsolete files"
    if delete == True:
        obsolete_files = dircmp(source_path,dest_path).right_only
        for file in obsolete_files:
            FileDeleted.append(str(file+"\n"))
            os.remove(Path(dest+"\\"+file))


    #Update report log file
    str_time_stamp = datetime.now().strftime("\n%Y_%m_%d_%H_%M_%S\n")
    with open("report.txt","a", encoding="utf-8") as f:
        f.write(str_time_stamp)

        number_updated = len(FileUpdated)
        number_copied = len(FileCopied)
        number_removed = len(FileDeleted)

        if number_updated == 0:
            f.write(f"NO FILES UPDATED.\n")
        else:
            f.write(f"UPDATED FILES: {number_updated}\n")
            f.writelines(FileUpdated)

        if number_copied == 0:
            f.write(f"NO FILES COPIED.\n")
        else:
            f.write(f"COPIED FILES: {number_copied}\n")
            f.writelines(FileCopied)

        if number_removed == 0:
            f.write(f"NO FILES REMOVED.\n")
        else:
            f.write(f"DELETED FILES: {number_removed}\n")
            f.writelines(FileDeleted)
        
        
        
     



