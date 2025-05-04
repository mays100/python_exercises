import boto3

# הגדרת שם הבאקט
bucket_name = 'student-maysabag-boto3-exercise1'

# הגדרת שם הקובץ למחיקה
file_to_delete = 'catphoto.jpeg'

# התחברות ל-S3 באמצעות boto3.client
s3 = boto3.client('s3')

# מחיקת הקובץ
try:
    s3.delete_object(Bucket=bucket_name, Key=file_to_delete)
    print(f"File '{file_to_delete}' deleted successfully from '{bucket_name}'.")
except Exception as e:
    print(f"Error deleting file: {e}")

# הצגת רשימת הקבצים בבאקט לאחר המחיקה (כדי לוודא שהקובץ נמחק)
print(f"\nFiles in bucket '{bucket_name}' after deletion:")
try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for item in response['Contents']:
            print(item['Key'])
    else:
        print("No files found in the bucket.")
except Exception as e:
    print(f"Error listing files after deletion: {e}")