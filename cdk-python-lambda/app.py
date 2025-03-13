#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_python_lambda.cdk_python_lambda_stack import CdkPythonLambdaStack

app = cdk.App()
CdkPythonLambdaStack(app, "CdkPythonLambdaStack")

app.synth()
