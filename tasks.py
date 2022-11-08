from celery import Celery
import os

app = Celery()
app.config_from_object("celery_settings")

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
            CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
@app.task
def hello():
     print('hello_test')

     import boto3
     import pandas as pd

     s3 = boto3.client('s3')

     s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='AKIAX7IW42VWFZVUAYUP',
        aws_secret_access_key='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'
     )

     # Print out bucket names
     for bucket in s3.buckets.all():
        print(bucket.name)

     import os
     os.environ["AWS_DEFAULT_REGION"] = 'us-east-1'
     os.environ["AWS_ACCESS_KEY_ID"] = 'AKIAX7IW42VWFZVUAYUP'
     os.environ["AWS_SECRET_ACCESS_KEY"] = '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'

     import pandas as pd

     # Make dataframes
     foo = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
     bar = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})
     foo1 = pd.DataFrame({'title': ['Natura Homem NEO'], 'url': ['https://www.youtube.com/watch?v=aq7GZxmtzK4']})

     # list of strings
     lst = ['Novo Luna Coragem', 'https://www.youtube.com/watch?v=-EWjS3XgUIM']

     # Calling DataFrame constructor on list
     foo4 = pd.DataFrame(lst)


     # Save to csv
     #foo1.to_csv('foo1.csv')
     #bar.to_csv('bar.csv')

     foo4.to_csv('foo4.csv')

     # Upload files to S3 bucket
     #s3.Bucket('rhoriycelery').upload_file(Filename='foo1.csv', Key='foo1.csv')
     #s3.Bucket('rhoriycelery').upload_file(Filename='bar.csv', Key='bar.csv')

     # Upload files to S3 bucket foo2
     s3.Bucket('rhoriycelery').upload_file(Filename='foo4.csv', Key='foo1.csv')
     #s3.Bucket('rhoriycelery').upload_file(Filename='bar.csv', Key='bar.csv')

     #for obj in s3.Bucket('rhoriycelery').objects.all():
        #print(obj)

     # Load csv file directly into python foo
     obj = s3.Bucket('rhoriycelery').Object('foo4.csv').get()
     foo4 = pd.read_csv(obj['Body'], index_col=0)

     #print(obj)

     #print(type(foo2))

     print(foo4)
