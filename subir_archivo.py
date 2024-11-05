import base64
import boto3

def lambda_handler(event, context):
    bucket_name = event['body']['bucket_name']
    file_name = event['body']['file_name']
    directory_name = event['body']['directory_name']
    base64_content = event['body']['file_content']
    
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=bucket_name,
        Key=f"{directory_name}/{file_name}",
        Body=base64.b64decode(base64_content)
    )
    
    return {
        'statusCode': 200,
        'message': f'Archivo {file_name} subido en el directorio {directory_name} del bucket {bucket_name}.'
    }