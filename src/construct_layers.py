import aws_cdk as cdk

from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3_deployment
from constructs import Construct


class ConstructLayersStack(cdk.Stack):
    """Demonstrates construct layers"""

    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        # Layer 1 (L1) Construct
        s3.CfnBucket(
            scope=self,
            id="L1Bucket",
            bucket_encryption=s3.CfnBucket.BucketEncryptionProperty(
                server_side_encryption_configuration=[
                    s3.CfnBucket.ServerSideEncryptionRuleProperty(
                        server_side_encryption_by_default=s3.CfnBucket.ServerSideEncryptionByDefaultProperty(
                            sse_algorithm="AES256",
                        ),
                    ),
                ],
            ),
        )

        # Layer 2 (L2) Construct
        l2_bucket = s3.Bucket(
            scope=self,
            id="L2Bucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
        )

        # Layer 3 (L3) Construct
        s3_deployment.BucketDeployment(
            scope=self,
            id="L3BucketDeployment",
            destination_bucket=l2_bucket,
            sources=[
                s3_deployment.Source.asset(
                    path="code/ch-infrastructure-as-code/src",
                ),
            ],
        )
