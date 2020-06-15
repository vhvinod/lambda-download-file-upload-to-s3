from io import BytesIO
from zipfile import ZipFile
import urllib.request
import botocore.vendored.requests.packages.urllib3 as urllib3
import os
import boto3

def lambda_handler(event, context):
    
    url = '<internet_url>'   #provide internet url to extract the zip file
    s3Bucket = 's3-bucket'   #provide s3 bucket name
    fileName = 'sample.zip'
    s3=boto3.resource('s3')
    
    url = urllib.request.urlopen(url)
    
    with ZipFile(BytesIO(url.read())) as my_zip_file:
        for contained_file in my_zip_file.namelist():
            s3.meta.client.upload_fileobj(my_zip_file.open(contained_file), s3Bucket, fileName+contained_file,
                                        ExtraArgs={'ServerSideEncryption':'aws:kms','SSEKMSKeyId':'alias/<alias_name>'})
