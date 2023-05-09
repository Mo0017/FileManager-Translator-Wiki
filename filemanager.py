# Import required libraries 
# os for directory access, time for recursion, Observer to keep track, FileSystem for handling events
import os 
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Choose the target folder to track
trackedFolder = 'C:\\Users\\moham\\Documents\\Test'

# Choose where to place certain filetypes and the path to the targer folder
extFolders = {
    'jpg': 'C:\\Users\\moham\\Documents\\Test\\jpgFiles',
    'pdf': 'C:\\Users\\moham\\Documents\\Test\\pdfFiles',
    'docx': 'C:\\Users\\moham\\Documents\\Test\\docxFiles',
    'doc': 'C:\\Users\\moham\\Documents\\Test\\docFiles'
}


# class to track the folder and move when the folder is modified, 
class FileSorter(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(trackedFolder):
            ext = filename.split('.')[-1]
            if ext in extFolders.keys():
                src = trackedFolder + '/' + filename
                targetDestination = extFolders[ext]
                shutil.move(src, targetDestination)

# Instantiate functions
eventHandler = FileSorter()
observer = Observer()
observer.schedule(eventHandler, trackedFolder, recursive= True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()



