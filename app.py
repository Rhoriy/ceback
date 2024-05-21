from flask import Flask, render_template
from tasks import hello

# Url botão Heroku Deploy
#https://dashboard.heroku.com/new-app?button-url=https%3A%2F%2Fgithub.com%2FRhoriy%2Fceback

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
    
