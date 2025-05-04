import boto3

# הגדרת שם הבאקט (החלף את 'yourname' בשמך)
bucket_name = 'student-maysabag-boto3-exercise1'.lower() # שמות באקטים חייבים להיות באותיות קטנות

# הגדרת שם הקובץ להעלאה (ודא שקובץ 'catphoto.jpeg' נמצא באותה תיקייה כמו הסקריפט)
file_to_upload = 'catphoto.jpeg'

# התחברות ל-S3 באמצעות boto3.client
s3 = boto3.client('s3')

# יצירת הבאקט
try:
    s3.create_bucket(Bucket=bucket_name,
                    CreateBucketConfiguration={
                        'LocationConstraint': 'us-west-2'  # כאן מגדירים את אזור הבאקט ל-us-west-2
                    })
    print(f"Bucket '{bucket_name}' created successfully in us-west-2.")
except Exception as e:
    # אם הבאקט כבר קיים, נקבל שגיאה, ואפשר להתעלם ממנה לצורך התרגיל
    if 'BucketAlreadyOwnedByYou' in str(e):
        print(f"Bucket '{bucket_name}' already exists.")
    else:
        print(f"Error creating bucket: {e}")

# העלאת הקובץ
try:
    s3.upload_file(file_to_upload, bucket_name, file_to_upload)
    print(f"File '{file_to_upload}' uploaded successfully to '{bucket_name}'.")
except Exception as e:
    print(f"Error uploading file: {e}")

# הצגת רשימת הקבצים בבאקט
print(f"\nFiles in bucket '{bucket_name}':")
try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for item in response['Contents']:
            print(item['Key'])
    else:
        print("No files found in the bucket.")
except Exception as e:
    print(f"Error listing files: {e}")