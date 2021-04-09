#########################################################################################
##   Python function to zip many files/directories and split in n smaller zip files    ##
##   Author: Gunther Bacellar                                                          ##
##   Email: gcbacel@hotmail.com                                                        ##
#########################################################################################

# Zip all files and subdirectories into a single file
import os
import pathlib
import shutil
from zipfile import ZipFile
def zip_all_files(source, target_filename):
    directory = source   
    file_paths = []    
    for root, directories, files in os.walk(directory):   
        for filename in files: 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
    with ZipFile(target_filename,'w') as zip:     
        for file in file_paths:          
            zip.write(file) 
        print('All files zipped successfully!')

source = pathlib.Path().absolute()   # change to the directory you want to zip files and sub-directories
target_zipname = 'Myfile.zip'       
zip_all_files(source, target_zipname)


# Stage 1: Breakdown a single file in multiple files
outfile = 'filename'    # change here to the name of file you want to breakdown
packet_size = int(80_000_000)   # Specify the number of bytes each part will have
with open(outfile, "rb") as output:
    filecount = 0
    while True:
        data = output.read(packet_size)
        print(len(data))
        if not data:
            break   # we're done
        with open("{}{:03}".format(outfile, filecount), "wb") as packet:
            packet.write(data)
        filecount += 1


# Stage 2: Merge the multiple file parts in a single zip file
packet_size = int(80_000_000)   # Specify the number of bytes each part has. It must be the same as defined in stage 1
file_name = 'filename'  # change here to the name of file you want to breakdown. Don't need to be the same as stage 1
number_parts = 6    # define the number of parts you are merging. It must contain all parts in order to create file
file_list = [file_name +'00'+str(x) for x in range(number_parts)]
output_file = 'HW4-mina.zip'
packet_size = int(100_741_824) 
with open(output_file, 'wb') as output:
    for file in file_list:
        with open(file, "rb") as input:
            data = input.read(packet_size)
            output.write(data)