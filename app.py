from flask import Flask, render_template
from tasks import hello

app = Flask(__name__)

@app.route('/')
def index():
    hello.delay()
    return 'OK'

@app.route('/result_ce')
def resultce():
    print('Cheguei CE')
    
    import boto3
    import pandas as pd

    s3 = boto3.client('s3')

    '''

    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id='',
        aws_secret_access_key=''
    )

    '''

    print('Cheguei CE')
    # Load csv file directly into python foo
    #obj = s3.Bucket('rhoriycelery').Object('foo1.csv').get()
    #foo1 = pd.read_csv(obj['Body'], index_col=0)

    obj = s3.Bucket('rhoriycelery').Object('foo4.csv').get()
    foo4 = pd.read_csv(obj['Body'], index_col=0)

    print('ffo4:', foo4)

    #title = foo2[0]
    url = foo4.loc[1].item()
    title = foo4.loc[0].item()


    #print('title:', title)
    #print('url:', url)

    #print(obj)

    #print(type(foo1))

    #print('foo1:', foo1)

    return render_template('result.html', title=title, url=url)
    
  
    #return 'OK CE'

if __name__ == "__main__":
    app.run()
    
