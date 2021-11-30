"""
This file is to check if the folder that the student is trying to submit
is of this exact structure (with exact naming):
| student.py
| tothemoon.png


This code is inspired by the submission zip file created by Professor
James Tompkin (james_topkin@brown.edu) for CSCI 1430 - Brown University.

Adapted by Nam Do (nam_do@brown.edu) - Summer 2021.
"""

import sys
import os, zipfile

########################################## HELPER FUNCTIONS ##########################################

# Function from https://stackoverflow.com/questions/1724693/find-a-file-in-python
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


# Function adapted from https://www.geeksforgeeks.org/working-zip-files-python/
def get_all_file_paths(directory, ext):
    # Initializing empty file paths list
    file_paths = []

    # Crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory):
        for filename in files:
            if filename.endswith(ext):
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
    
    # returning all file paths
    return file_paths

########################################## MAIN ZIP LOGIC ##########################################
def main():
    # First, check what directory that we're running this from
    curdir = os.getcwd()
    failed = False
    # If the current directory doesn't contain this script, we'll exit and
    # tell the student to chdir to the right directory
    if find('zip_assignment.py', curdir) == None:
        # We haven't found this file, and so we will print out a message and sys exit
        print("We cannot find the file zip_assignment.py in the directory that you are")
        print("executing this script from. Please use command 'cd <path>' to change to the right")
        print("directory that contains zip_assignment.py and execute this script again.")
        sys.exit()
    # Check if there is the right files
    student_code_path, student_successful_plot_path = "student.py", "tothemoon.png"
    for p in [student_code_path, student_successful_plot_path]:
        if not os.path.exists(p):
            failed = True
            print(f"Issue: This directory does not contain '{p}'.")
            if p == student_successful_plot_path:
                print(f"Please make sure that the stencil graph plotting function is executed properly so the file {p} is written to your directory")

            print(f"Please make sure that the file '{p}' is in the same directory as 'zip_assignment.py'.")
            print("\n\n")


    if failed:
        print("Please fix all your issues for zipping code to proceed.")
        sys.exit()

    print("Writting into zip file...")
    zip_path = "getting-started-submission-1951A.zip"
    with zipfile.ZipFile(zip_path, "w") as zip:
        # Write the code file
        if os.path.exists(student_code_path):
            zip.write(student_code_path)

        # Write the image file to make sure that the student produced the thing successfully
        if os.path.exists(student_successful_plot_path):
            zip.write(student_successful_plot_path)


    print("Done! Wrote the submission zip to {}".format(zip_path))

    

        


if __name__ == "__main__":
    main()