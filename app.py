import aws_cdk as cdk

from src.cdk_stack import MyStack


app = cdk.App()
MyStack(app, "MyStack")
app.synth()
