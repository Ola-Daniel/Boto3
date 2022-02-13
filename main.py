import boto3
import uuid

"""
# Create a bucket with boto3
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 char long
    return ''.join([bucket_prefix, str(uuid.uuid4())])
"""


def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response


# dynamically creating and naming files in s3 buckets
def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name


first_file_name = create_temp_file(300, 'firstfile.txt', 'f')
# Creating Bucket and Object instances
first_bucket = s3_resourse.Bucket(name=first_bucket_name)
first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name
)


#Uploading a file with the following, Object,bucket, or client instance
# Object
s3_resource.Object(first_bucket_name, first_file_name).upload_file(
    Filename=first_file_name
)

#Bucket
s3_resource.Bucket(first_bucket_name).upload_file(
    Filename=first_file_name, Key=first_file_name
)

#Client
s3_resource.meta.client.upload_file(
    Filename=first_file_name, Bucket=first_bucket_name,
    Key=first_file_name
)

# Downloading a file from s3
s3_resource.Object(first_bucket_name, first_file_name).download_file(
    f'/tmp/{first_file_name}')


# Copying objects between buckets
def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)

copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name)

