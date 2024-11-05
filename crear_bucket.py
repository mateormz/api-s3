import boto3

def lambda_handler(event, context):
    bucket_name = event['body']['bucket_name']
    region = 'us-east-1'  # Cambia la región aquí si deseas otra diferente
    s3 = boto3.client('s3', region_name=region)  # Establece la región explícitamente

    # Verifica si la región es us-east-1 (sin LocationConstraint)
    if region == 'us-east-1':
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    
    return {
        'statusCode': 200,
        'message': f'Bucket {bucket_name} creado exitosamente en la región {region}.'
    }
