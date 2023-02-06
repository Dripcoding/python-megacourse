import zipfile


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir) # extract contents of zip file to dest_dir
    

if __name__ == '__main__':
    extract_archive('/home/juiced/python-mega-course/todosApp/bonus/compressed.zip', 
                    '/home/juiced/python-mega-course/todosApp/files')