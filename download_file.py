import boto3

# הגדרת שם הבאקט (השתמש בשם הבאקט שיצרת בתרגיל 1)
bucket_name = 'student-maysabag-boto3-exercise1'

# הגדרת שם הקובץ להורדה מהבאקט
file_to_download = 'catphoto.jpeg'

# הגדרת שם הקובץ המקומי שבו יישמר הקובץ שהורד
local_file_name = 'downloaded_catphoto.jpeg'

# התחברות ל-S3 באמצעות boto3.client
s3 = boto3.client('s3')

# הורדת הקובץ מהבאקט
try:
    s3.download_file(bucket_name, file_to_download, local_file_name)
    print(f"File '{file_to_download}' downloaded successfully to '{local_file_name}'.")
except Exception as e:
    print(f"Error downloading file: {e}")