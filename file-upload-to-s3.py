import urllib
import boto3
import botocore.vendored.requests.packages.urllib3 as urllib3
import logging
import http.client

def lambda_handler(event, context):

    s3Bucket = 's3-bucket'  #provide s3 bucket name
    url = '<internet_url>'  #provide internet url to download the file  

    s3=boto3.resource('s3')
    http=urllib3.PoolManager()
            
    file=url.rsplit('/',1)[1]
    urllib.request.urlopen(url)
    s3.meta.client.upload_fileobj(http.request('GET', url,preload_content=False), s3Bucket, file, 
    ExtraArgs={'ServerSideEncryption':'aws:kms','SSEKMSKeyId':'alias/<alias_name>'})
    print('Download completed : ' +file)
