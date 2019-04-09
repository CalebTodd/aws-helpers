#!/usr/bin/env python3

# uses f-strings, so 3.6 or newer required
# reference: https://stackoverflow.com/questions/32106094

import argparse
from functions import whoami
import boto3
import botocore


def main():
    '''
    Purges delete markers from an S3 bucket
    Useful if versioning was not turned off before trying to delete a bucket
    '''
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-b', '--bucket_name',
                        required=True,
                        choices=[
                            'calebtodd-bucket-1',
                            'calebtodd-bucket-2'
                        ],
                        help="S3 Bucket to delete"
                        )
    args = parser.parse_args()
    whoami()
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(args.bucket_name)
    print(f'Working on {bucket.name}')
    versions = bucket.object_versions
    for version in versions.all():
        if is_delete_marker(version):
            version.delete()


def is_delete_marker(version):
    '''
    returns bool
    '''
    try:
        # note head() is faster than get()
        version.head()
        return False
    except botocore.exceptions.ClientError as e:
        if 'x-amz-delete-marker' in
        e.response['ResponseMetadata']['HTTPHeaders']:
            return True
        # an older version of the key but not a DeleteMarker
        elif '404' == e.response['Error']['Code']:
            return False


if __name__ == '__main__':
    main()
