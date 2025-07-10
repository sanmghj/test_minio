import boto3
from botocore.config import Config

def hello_s3():
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon Simple Storage Service
    (Amazon S3) client and list the buckets in your account.
    This example uses the default settings specified in your shared credentials
    and config files.
    """

    # Create an S3 client.
    s3_client = boto3.client(
        "s3",
        endpoint_url="http://127.0.0.1:9000",
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin",
        config = Config(
            region_name="ap-northeast-2",
            signature_version="s3v4",
        )
    )

    print("Hello, Amazon S3! Let's list your buckets:")

    # Create a paginator for the list_buckets operation.
    paginator = s3_client.get_paginator("list_buckets")

    # Use the paginator to get a list of all buckets.
    response_iterator = paginator.paginate(
        PaginationConfig={
            "PageSize": 50,  # Adjust PageSize as needed.
            "StartingToken": None,
        }
    )

    # Iterate through the pages of the response.
    buckets_found = False
    for page in response_iterator:
        if "Buckets" in page and page["Buckets"]:
            buckets_found = True
            for bucket in page["Buckets"]:
                print(f"\t{bucket['Name']}")

    # upload a file to bucket
    if buckets_found:
        file_path = "test.json"

        # length = len(page["Buckets"])
        print(page["Buckets"])
        for bucket in page["Buckets"]:
            bucket_name = bucket["Name"]
            s3_client.upload_file(file_path, bucket_name, "test.json")
            print(f"File '{file_path}' uploaded to bucket '{bucket_name}'.")

    if not buckets_found:
        print("No buckets found!")


if __name__ == "__main__":
    hello_s3()
