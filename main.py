import glob
import os
from shutil import copyfile

input_folder = input("Enter path to input folder \n")
output_folder = input("Enter path to output folder \n")
if not (os.path.isdir(output_folder)):
    os.makedirs(output_folder)  # Make sure directory exists before starting
if not (output_folder.endswith("/") or output_folder.endswith("\\")):  # To be sure our paths are correct
    output_folder += "/"
if not (input_folder.endswith("/") or input_folder.endswith("\\")):
    input_folder += "/"
while True:
    student_login = input("Enter student login \n")
    list_of_files = glob.iglob(input_folder + "*.jpg")  # select all images from folder
    file_to_copy = max(list_of_files, key=os.path.getctime)
    copyfile(file_to_copy, out_folder + student_login + ".jpg")
    print("Copied " + file_to_copy + " to " +  out_folder + student_login + ".jpg")
