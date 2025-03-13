from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct
import os

class CdkPythonLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_function = _lambda.Function(
            self, 'TestingLambda',
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler='testing-lambda.handler',
            code=_lambda.Code.from_asset(os.path.join(os.getcwd(), 'lambda'))
        )
