import pathlib

import dropbox

from constants_.base import DROPBOX_ACCESS_TOKEN
from dropbox.exceptions import AuthError


def dropbox_connection():
    """
    Function to create a connection to Dropbox
    :return:
    """
    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print("Error connect to Dropbox with current access token: ", str(e))

    return dbx


def dropbox_upload_file(contents, file_name):
    """
    Function to upload file to Dropbox
    :return:
    """
    dbx = dropbox_connection()
    try:
        dbx.files_upload(contents, f'/testcase_folder/{file_name}', mode=dropbox.files.WriteMode("overwrite"))
        return True
    except Exception as e:
        return False


def dropbox_download_file(file_name):
    """
    Function to download file from Dropbox
    :return:
    """
    dbx = dropbox_connection()

    metadata, result = dbx.files_download(path=f'/testcase_folder/{file_name}')
    local_path = f'temp_/{file_name}'

    with open(local_path, 'wb') as f:
        f.write(result.content)
        f.close()

    return local_path
