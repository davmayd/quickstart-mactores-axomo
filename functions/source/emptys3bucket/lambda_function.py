from __future__ import print_function
from crhelper import CfnResource
import logging
import boto3

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource()

try:
    ## Init code goes here
    pass
except Exception as e:
    helper.init_failure(e)

@helper.create
@helper.update
def create(event, context):
    logger.info("Got Create")
    bucket = event['ResourceProperties']['BucketName']
    logger.info(bucket)
    logger.info("Above bucket created")

@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    try:
        bucket = event['ResourceProperties']['BucketName']
        logger.info(bucket)
        logger.info("Above bucket will be emptied")
        if event['RequestType'] == 'Delete':
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(bucket)
            for obj in bucket.objects.filter():
                s3.Object(bucket.name, obj.key).delete()
    except Exception as e:
        print(e)
    # Delete never returns anything. Should not fail if the underlying resources are already deleted. Desired state.

def lambda_handler(event, context):
    logger.info("calling helper")
    helper(event, context)
    logger.info("done helper")