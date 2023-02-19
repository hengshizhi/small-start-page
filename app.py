from sanic import Sanic 
from sanic.response import text,html,json,file,raw,file_stream,redirect,empty 

app = Sanic("qishiye")

def get_or_post(request:object,key): #如果没有GET参数就用post
    if(request.args.get(key) != None):
        return request.args.get(key)
    elif(request.form.get(key) != None):
        return request.form.get(key)
    return False

async def index(request):
    return await file('./index.html')

async def favicon(request):
    '''favicon.ico图标'''
    return text('OK!')

async def write(request):
    data = get_or_post(request,'data')
    if(data):
        with open('./data.txt', 'w' ,encoding='utf-8') as f :
            f.write(data)
        return text('OK!')
    return text('False')

async def read(request):
    with open('data.txt','r' ,encoding='utf-8') as f:
        ret = f.read()
    return text(ret)

app.add_route(favicon, "/favicon.ico",methods=["GET"]) # favicon.ico
app.add_route(index,f'/',methods=['GET','POST']) 
app.add_route(write,f'/write',methods=['GET','POST']) 
app.add_route(read,f'/read',methods=['GET','POST']) 

if __name__ == "__main__":
    app.run(port=80,debug=True,dev=True)