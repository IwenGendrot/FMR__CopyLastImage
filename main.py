import glob
import os
from shutil import copyfile


def confirmation(in_folder, out_folder, file_to_copy, student_login):
    user_command = input("Copy " + file_to_copy + " to " + out_folder
                         + student_login + ".jpg ? y/c to enter file manually \n")
    if user_command == "y":
        copyfile(file_to_copy, out_folder + student_login + ".jpg")  # copy image from in folder to out folder
        print("File renamed")
    elif user_command == "c":
        file_to_copy = in_folder + input("Correct file to copy in input folder : \n")
        if os._exists(file_to_copy):
            confirmation(in_folder, out_folder, file_to_copy, student_login)
        else:
            print("File do not exist")
    else:
        print("File note renamed")


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
    confirmation(input_folder, output_folder, max(list_of_files, key=os.path.getctime), student_login)
