import boto3
import json
#import logging


class LambdaLauncher():
    def __init__(self):
        print("Started Lambda Launcher")
        #self.logger = logging.Logger() TODO: setup logger
        self.client = boto3.client('lambda')


    def register_function(self, function_name, runtime, role_arn, handler, zip_file_path):
        print(f"Registering function with name: {function_name}")
        with open(zip_file_path, 'rb') as f:
            zipped_code = f.read()

        # Register the Lambda function
        response = self.client.create_function(
            FunctionName=function_name,
            Runtime=runtime,
            Role=role_arn,
            Handler=handler,
            Code={
                'ZipFile': zipped_code,
            },
            Description='Your function description',
            Timeout=60,  # Timeout in seconds
            MemorySize=128,  # Memory size in MB
            Publish=True
        )
        print(f"Response: {response}")


    def invoke_masa_function(self):
        response = self.client.invoke(
            FunctionName='masa-function',
            InvocationType='RequestResponse',
            LogType='Tail'
        )
        response_payload = response['Payload'].read().decode('utf-8')
        print(response_payload)


    def update_function_code(self, function_name, zip_file_path):
        with open(zip_file_path, 'rb') as f:
            zipped_code = f.read()

        response = self.client.update_function_code(
            FunctionName=function_name,
            ZipFile=zipped_code,
        )
        print(response)