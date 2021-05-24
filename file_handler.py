import os,sys,shutil

def get_images(folder):
    '''
    find image files in test data path
    :return: list of files found
    '''
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print('Find {} images'.format(len(files)))
    return files



if __name__=='__main__':

    source_dir  = '/home/amr62/turin_file_system/copied_files/'
    dest_dir    = '/home/amr62/turin_file_system/demo_images/'
    pat_folders = [os.path.join(source_dir,f) for f in os.listdir(source_dir)]

    filtered_files=[]
    for pat_folder in pat_folders:
        filtered_files += [os.path.join(pat_folder,f) for f in os.listdir(pat_folder) if 'hands' in f or 'feet' in f]

    # for f in filtered_files:
    f = filtered_files[0]
    dest_files=[]
    for f in filtered_files:
        im_file = os.path.join(os.path.basename(os.path.split(f)[-2]),os.path.split(f)[-1])
        if not os.path.isdir(os.path.join(dest_dir,os.path.split(im_file)[-2])):
            os.makedirs(os.path.join(dest_dir,os.path.split(im_file)[-2]))
        dest_f = os.path.join(dest_dir,im_file)
        dest_files += [dest_f]
        shutil.copy2(f,dest_f)







