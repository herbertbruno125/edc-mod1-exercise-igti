import boto3

if __name__ == '__main__':
    # s3_client = boto3.client('s3')
    # s3_client.download_file('datalake-herbertsantos-igti-edc', 'data/teste.csv', 'dimenssao_teste.csv')

    # s3_client.upload_file('teste_2.csv',
    #                       'datalake-herbertsantos-igti-edc',
    #                       'data/dimensao_teste_2.csv')

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('datalake-herbertsantos-igti-edc')
    for obj in bucket.objects.all():
        print(obj.key)
