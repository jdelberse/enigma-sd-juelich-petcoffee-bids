import os
import sys
import pandas as pd

# %%
# path of the dataset
save_path = '/data/project/sleep_ENIGMA_Cognition/dataladstore/PETcoffee_BIDS/'
reformat_path = '/data/project/sleep_ENIGMA_Cognition/dataladstore/PETcoffee_BIDS/'

# %%
def get_folder_lists(save_path):
    # get the list of the folders
    folders = os.listdir(save_path)
    # only keep the real folders
    folders = [f for f in folders if os.path.isdir(os.path.join(save_path, f))]
    # remove the . start folders
    folders = [f for f in folders if not f.startswith('.')]
    # order the folders
    folders.sort()

    return folders

# %%
"""
Get subject lists from all sessions, and compare the subject lists for different sessions and make a list includes all subjects
"""
# get the list of subjects folders
sess_folders = get_folder_lists(save_path)

# get all subjects inside all sessions, remove the duplicates and sort the list
def get_all_subjects(sess_folders):
    all_subjects = []
    for sess in sess_folders:
        sess_path = os.path.join(save_path, sess)
        subjects = get_folder_lists(sess_path)
        all_subjects.extend(subjects)
    all_subjects = list(set(all_subjects))
    all_subjects.sort()

    return all_subjects

all_sub_list = get_all_subjects(sess_folders)
# for the elements in the list, like 'sub-105006003', remove the last 3 digits, remove the duplicates and sort the list
all_sub_list = [sub[:-3] for sub in all_sub_list]
all_sub_list = list(set(all_sub_list))
all_sub_list.sort()

# %%
# compare the all_sub_list with the subjects in each session, and get each session missing subjects
def get_missing_subjects(sess_folders, all_sub_list):
    missing_sub_list = []
    for sess in sess_folders:
        sess_path = os.path.join(save_path, sess)
        subjects = get_folder_lists(sess_path)
        subjects = [sub[:-3] for sub in subjects]
        subjects.sort()
        missing_sub = list(set(all_sub_list) - set(subjects))
        missing_sub.sort()
        missing_sub_list.append(missing_sub)

    return missing_sub_list

missing_sub_list = get_missing_subjects(sess_folders, all_sub_list)

# %%
"""
Based on sub_list, reformat the data
"""
# create subject folders
for sub in all_sub_list:
    if not os.path.exists(reformat_path + sub):
        os.makedirs(reformat_path + sub)

# %%
# create session folders in each subject folder
for sub in all_sub_list:
    for sess in sess_folders:
        # check if this subject exists in this session
        if sub in missing_sub_list[sess_folders.index(sess)]:
            # print missing subjects and jump to the next session
            print('Subject ' + sub + ' is missing in session ' + sess)
            continue
        else:
            # create session folder
            if not os.path.exists(reformat_path + sub + '/' + 'ses-' + sess):
                os.makedirs(reformat_path + sub + '/' + 'ses-' + sess)
            # create the file type folders in each session folder
            if not os.path.exists(reformat_path + sub + '/' + 'ses-' + sess + '/anat'):
                os.makedirs(reformat_path + sub + '/' + 'ses-' + sess + '/' + 'anat')
            if not os.path.exists(reformat_path + sub + '/' + 'ses-' + sess + '/func'):
                os.makedirs(reformat_path + sub + '/' + 'ses-' + sess + '/' + 'func')
            if not os.path.exists(reformat_path + sub + '/' + 'ses-' + sess + '/fmap'):
                os.makedirs(reformat_path + sub + '/' + 'ses-' + sess + '/' + 'fmap')

# %%
"""
Move files
"""
for sess in sess_folders:
    sub_folders = get_folder_lists(save_path + sess)
    for sub in sub_folders:
        # get the list of the file types
        file_types = get_folder_lists(save_path + sess + '/' + sub)
        # print(file_types)
        for f_type in file_types:
            # get the list of the files
            files = os.listdir(save_path + sess + '/' + sub + '/' + f_type)
            # print(files)
            for file in files:
                print(file)
                # sub remove the last 3 digits
                sub_re = sub[:-3]
                # file name, remove the digits before the first '_'
                file_name = file[file.find('_'):]
                # rename the file
                re_file_name = sub_re + '_' + 'ses-' + sess + file_name
                # if the file is already in the folder, skip it
                if os.path.exists(reformat_path + sub_re + '/' + 'ses-' + sess + '/' + f_type + '/' + re_file_name):
                    print('File already exists, skip it')
                    continue
                # os.rename(save_path + sess + '/' + sub + '/' + f_type + '/' + file,
                #           reformat_path + sub_re + '/' + 'ses-' + sess + '/' + f_type + '/' + re_file_name)
                command = 'mv ' + save_path + sess + '/' + sub + '/' + f_type + '/' + file + ' ' + reformat_path + sub_re + '/' + 'ses-' + sess + '/' + f_type + '/' + re_file_name
                os.system(command)

# %%
# remove the former session folders
for sess in sess_folders:
    command = 'rm -rf ' + save_path + sess
    os.system(command)