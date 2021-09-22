from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import (
    core,
    aws_lambda as _lambda
)


class SamplePythonCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        cdk_lambda = _lambda.Function(
            self, 'sample-python-lambda',
            runtime=_lambda.Runtime.PYTHON_3_7,
            description='Lambda function deployed using AWS CDK Python',
            code=_lambda.Code.asset('lambda'),
            handler='lambda_code.handler',
        )
