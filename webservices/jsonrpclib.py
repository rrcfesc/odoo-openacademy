import jsonrpclib

HOST = 'localhost'
PORT = 8069
DB = 'odoo-db'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)
# server proxy object
URL = "http://%s:%s/jsonrpc" % (HOST, PORT)
SERVER = jsonrpclib.Server(URL)
# log SERVER the given database
uid = SERVER.call(service="common", method="login", args=[DB, USER, PASS])


# helper function for invoking model methods
def invoke(model, method, *args):
    ARGS= [DB, uid, PASS, model, method] + list(args)
    return SERVER.call(service="object", method="execute", args=ARGS)


# create a new note
ARGS = {
    'name': 'New course'
}
NOTE_ID = invoke('openacademy.session', 'create', ARGS)
