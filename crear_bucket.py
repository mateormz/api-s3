import boto3

def lambda_handler(event, context):
    bucket_name = event['body']['bucket_name']
    s3 = boto3.client('s3')
    
    # Crear el bucket en us-east-1 sin especificar LocationConstraint
    s3.create_bucket(Bucket=bucket_name)
    
    return {
        'statusCode': 200,
        'message': f'Bucket {bucket_name} creado exitosamente en la región us-east-1.'
    }
