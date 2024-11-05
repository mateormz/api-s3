import boto3
import os

def lambda_handler(event, context):
    bucket_name = event['body']['bucket_name']
    s3 = boto3.client('s3')
    
    region = 'us-east-1'

    # Parámetros adicionales para evitar el error
    s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    
    return {
        'statusCode': 200,
        'message': f'Bucket {bucket_name} creado exitosamente en la región {region}.'
    }
