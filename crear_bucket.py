import boto3

def lambda_handler(event, context):
    bucket_name = event['body']['bucket_name']
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    
    return {
        'statusCode': 200,
        'message': f'Bucket {bucket_name} creado exitosamente.'
    }
