# -*- coding: utf-8 -*-
import functools
import xmlrpc.client


HOST = 'localhost'
PORT = 8069
DB = 'odoo-db'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print("Logged in as %s (uid: %d)" % (USER, uid))

CALL = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# Read the SESSIONS
SESSIONS = CALL('openacademy.session', 'search_read', [], ['name', 'seats'])
for session in SESSIONS:
    print("Session %s (%s seats)" % (session['name'], session['seats']))

# Create a new session from Course 0
COURSE_ID = CALL(
    'openacademy.course',
    'search',
    [('name', 'ilike', 'curso 1')]
)[0]
SESSION_ID = CALL('openacademy.session', 'create', {
    'name': 'My session',
    'course_id': 2,
    })
