import boto3
from dotenv import load_dotenv
import os

def upload_in_aws(name):
    load_dotenv('.env')
    aws_access_key_id = os.getenv("ACCES_ID")
    aws_secret_access_key = os.getenv("SECRET_ID")
    bucket_name = "proyecto2-archivos-202010770"
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3.upload_file(name, bucket_name, name)
    print("Archivo correctamente subido")