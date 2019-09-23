from __future__ import print_function
from crhelper import CfnResource
import logging
import boto3
import json

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource()

try:
    ## Init code goes here
    pass
except Exception as e:
    helper.init_failure(e)

@helper.update
@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    logger.info("Do nothing")

@helper.create
def create(event, context):
    logger.info("Got Create")
    try:
        sourcebucket = event['ResourceProperties']['SourceBucketName']
        bucketprefix = event['ResourceProperties']['SourceBucketPrefix']
        bucketkey = bucketprefix+'scripts/model-ll.tar.gz'
        destbucket = event['ResourceProperties']['DestBucketName']
        logger.info(sourcebucket)
        logger.info(bucketkey)
        logger.info(destbucket)
        if event['RequestType'] == 'Create':
            s3 = boto3.client('s3')
            copy_source = {'Bucket':sourcebucket, 'Key':bucketkey}
            logger.info('copying lambda zip')
            s3.copy_object(Bucket=destbucket, Key=bucketkey, CopySource=copy_source)
            logger.info('copied lambda zip')
    except Exception as e:
        print(e)

def lambda_handler(event, context):
    logger.info("calling helper")
    helper(event, context)
    logger.info("done helper")