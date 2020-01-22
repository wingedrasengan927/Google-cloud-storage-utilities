from google.cloud import storage
import argparse
import os

def download_folder_from_bucket(bucket_name, folder_name, local_folder_name, service_key_path):
    """Downloads a folder from the bucket."""
    storage_client = storage.Client.from_service_account_json(service_key_path)
    bucket = storage_client.get_bucket(bucket_name)
    files = bucket.list_blobs(prefix=folder_name)

    for file in files:
        if '.' in file.name:
            filename = file.name.split('/')[-1]
            # note that the dir should exist before downloading to that dir
            file.download_to_filename(local_folder_name +"/"+filename)

def upload_files_into_bucket(bucket_name, bucketFolder, localFolder, service_key_path):
    """Upload files to GCP bucket."""
    storage_client = storage.Client.from_service_account_json(service_key_path)
    bucket = storage_client.get_bucket(bucket_name)
    local_files = [file for file in os.listdir(localFolder) if os.path.isfile(os.path.join(localFolder, file))]
    for file in local_files:
        localFile = localFolder + "/" + file
        blob = bucket.blob(bucketFolder + "/" + file)
        blob.upload_from_filename(localFile)
        
def delete_folder_from_bucket(bucket_name, bucketFolder, service_key_path):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client.from_service_account_json(service_key_path)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(bucketFolder)
    blob.delete()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="store_true", default=False, help="download files from a folder in a google cloud bucket")
    parser.add_argument("--service_account", default=None, type=str, help="path to the service account json file")
    parser.add_argument("--bucket_name", default=None, type=str, help="name of the google storage bucket")
    parser.add_argument("--bucket_folder", default=None, type=str, help="name of the folder inside the bucket whose files you want to download")
    parser.add_argument("--local_folder", default=None, type=str, help="the folder in your machine you want to download or upload the files")
    parser.add_argument("-u", action="store_true", default=False, help="upload files into a folder inside a bucker")
    parser.add_argument("-d", action="store_true", default=False, help="delete a folder from a bucket")

    args = parser.parse_args()

    if args.d:
        download_folder_from_bucket(args.bucket_name, args.bucket_folder, args.local_folder, args.service_account)
    elif args.u:
        upload_files_into_bucket(args.bucket_name, args.bucket_folder, args.local_folder, args.service_account)
    elif args.d:
        delete_folder_from_bucket(args.bucket_name, args.bucket_folder, args.service_account)

if __name__ == "__main__":
    main()
