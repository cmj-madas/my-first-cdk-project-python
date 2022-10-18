from distutils import core
from aws_cdk import (
    aws_s3 as _s3,
    Stack
    # Duration,
    # aws_sqs as sqs,
)
from constructs import Construct

class MyFirstCdkProjectPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "mybucketId",
            bucket_name="myfirstcdkproject101020203900",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )

        # example resource
        # queue = sqs.Queue(
        #     self, "MyFirstCdkProjectPythonQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
