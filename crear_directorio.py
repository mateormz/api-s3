import boto3

def lambda_handler(event, context):
    bucket_name = event['body']['bucket_name']
    directory_name = event['body']['directory_name']
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=(directory_name + '/'))
    
    return {
        'statusCode': 200,
        'message': f'Directorio {directory_name} creado en el bucket {bucket_name}.'
    }
