#!/usr/bin/env python3

# uses f-strings, so 3.6 or newer required

import boto3
import botocore
import textwrap


def set_default_aws_session(aws_profile=None, region_name='us-east-2'):
    '''
    sets AWS Boto3 default session
    '''
    try:
        if aws_profile:
            boto3.setup_default_session(
                profile_name=aws_profile,
                region_name=region_name
            )
        else:
            # using default provider chain w/ region argument
            boto3.setup_default_session(region_name=region_name)

    except botocore.exceptions.ProfileNotFound:
        boto3.setup_default_session(region_name=region_name)

    whoami()


def whoami():
    '''
    prints information about the current default session
    '''
    client = boto3.client('sts')
    response = client.get_caller_identity()
    output = f"""
        Arn: {response['Arn']}
        UserId: {response['UserId']}
    """
    print(textwrap.dedent(output))
