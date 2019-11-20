# Google-cloud-storage-utilities
Some basic utilities to manipulate google cloud storage using python

### Prerequisites
You need to have google-cloud-storage installed. You can install it through pip

```
pip install google-cloud-storage
```

### Examples

To download files from a folder called images which is inside a bucket named test-bucket into a folder called local_images which is in your local machine:
```
python gcp_utils.py -d --bucket_name=test-bucket --bucket_folder=images --local_folder=local_images --service_account=/home/user/Downloads/balmy-flash-255917-08b1d111e665.json
```
Note that the service account needs to have storage admin privileges and local_images folder should have been already created in your local machine

To upload files from a folder called local_images which is in your local machine to a folder called images inside a bucket named test-bucket:
```
python gcp_utils.py -u --bucket_name=test-bucket --bucket_folder=images --local_folder=local_images --service_account=/home/user/Downloads/balmy-flash-255917-08b1d111e645.json
```
Note that the service account needs to have storage admin privileges and images folder should have been already created in the test-bucket

### References
* https://hackersandslackers.com/manage-files-in-google-cloud-storage-with-python/
* google cloud documentation
