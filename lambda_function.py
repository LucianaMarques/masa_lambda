# lambda_function.py
import boto3
from datetime import date, datetime
import logging
import os
import subprocess


def lambda_handler(event, context):
    log_file_name = f"masa_function_output-{date.year}-{date.month}-{datetime.hour}-{datetime.minute}-{datetime.second}.log"
    logging.basicConfig(filename=log_file_name, level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    os.chdir("./")
    command = "/var/task/MASA-OpenMP/masa-openmp-1.0.1.1024/masa-openmp /var/task/sequence.fasta /var/task/sequence2.fasta"
    r = subprocess.run(command.split(), capture_output=True)
    logger.info(f'Executed run with return code: {r.returncode}')
    s3 = boto3.client('s3')
    s3.put_object(Body=log_file_name, Bucket='spot-pricing-research', Key=log_file_name)
    return {
        'statusCode': r.returncode,
        'stdout': r.stdout,
        'stderr': r.stderr,
    }
