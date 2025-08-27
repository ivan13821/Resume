import os





def get_start_patch():
    this_file = os.path.abspath(__file__).split('/')
    path_to_start_project = '/'.join(this_file[0:this_file.index("ResumeBackEnd")])+"/"

    return path_to_start_project

