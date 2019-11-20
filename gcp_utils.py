from google.cloud import storage
import os

def download_folder_from_bucket(bucket_name, folder_name, destination_folder_name, service_key_path):
    """Downloads a folder from the bucket."""
    storage_client = storage.Client.from_service_account_json(service_key_path)
    bucket = storage_client.get_bucket(bucket_name)
    files = bucket.list_blobs(prefix=folder_name)

    for file in files:
        if '.' in file.name:
            filename = file.name.split('/')[-1]
            # note that the dir should exist before downloading to that dir
            file.download_to_filename(destination_folder_name +"/"+filename)

def upload_files_into_bucket(bucket_name, bucketFolder, localFolder, service_key_path):
    """Upload files to GCP bucket."""
    storage_client = storage.Client.from_service_account_json(service_key_path)
    bucket = storage_client.get_bucket(bucket_name)
    local_files = [file for file in os.listdir(localFolder) if os.path.isfile(os.path.join(localFolder, file))]
    for file in local_files:
        localFile = localFolder + "/" + file
        blob = bucket.blob(bucketFolder + "/" + file)
        blob.upload_from_filename(localFile)

# download_folder_from_bucket("temp-bucket-for-lab", "input_images", "images_from_gcp", "/home/user/Downloads/balmy-flash-255917-08b1d111e645.json")
# upload_files_into_bucket("temp-bucket-for-lab", "input_images_2", "images_from_gcp", "/home/user/Downloads/balmy-flash-255917-08b1d111e645.json")