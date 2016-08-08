from flask import Flask
from listener import Listener

app = Flask(__name__)

host = "127.0.0.1"
port = 5001

# define Listener that manages the communication with the remote datagenerator service
generator_domain = "http://127.0.0.1:5000"
listener = Listener(generator_domain)

# you define a callback that is triggered
# if datagenerator sends data for example by a scheduled frequence defined in blueprint with specified url
def callback(data):
    try:
        print "Hello, passive apple:", data.shape
    except:
        print "no passive apple transfered :("
listener.on('generate/apple/data', callback=callback)

# here you force the datagenerator to send data to the listener
# data is created by the options in blueprint with specified url
# p.s.: this is usually handy if you don not define a frequence,
# but you want to simulate a rest api
# p.s.: note that the listener.on above will be triggered too
def emitCallback(data):
    try:
        shape = data.shape
        print "Hello, requested apple:", shape
    except:
        print "no requested apple transfered :("
        print data

listener.emit('generate/apple/data', callback=emitCallback)

if __name__ == '__main__':
    listener.run(app, debug=True, port=port, host=host)
