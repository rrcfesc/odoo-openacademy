import jsonrpclib

HOST = 'localhost'
PORT = 8069
DB = 'odoo-db'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)
# server proxy object
Url_server = "http://%s:%s/jsonrpc" % (HOST, PORT)
Server = jsonrpclib.Server(url_server)
# log in the given database
uid = Server.call(service="common", method="login", args=[DB, USER, PASS])


# helper function for invoking model methods
def invoke(model, method, *args):
    Args2= [DB, uid, PASS, model, method] + list(args)
    return Server.call(service="object", method="execute", args=Args2)


# create a new note
Args = {
    'name': 'New course'
}
Note_id = invoke('openacademy.session', 'create', Args)
