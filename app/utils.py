import boto3 # type: ignore
from config import Config
from botocore.exceptions import NoCredentialsError # type: ignore

s3_client = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION
)

def upload_file_to_s3(file, filename):
    try:
        s3_client.upload_fileobj(file, Config.S3_BUCKET_NAME, filename)
        return True
    except NoCredentialsError:
        return False

def download_file_from_s3(filename):
    try:
        response = s3_client.get_object(Bucket=Config.S3_BUCKET_NAME, Key=filename)
        return response['Body']
    except NoCredentialsError:
        return None