#!/usr/bin/env python

import base64
import getpass
import os
import socket
import sys
import traceback
import paramiko


paramiko.util.log_to_file('sftp.log')
username = ''
if len(sys.argv) != 5:
	print "USAGE: sftp.py <username> <server> <path_on_server> <reportfile_to_upload>"
	sys.exit(1)



username = sys.argv[1]
hostname = sys.argv[2]
path = sys.argv[3]
ufile = sys.argv[4]

print username,"@",hostname," PATH=",path, "Trying to upload report file ", ufile, " to ", path, " on ", hostname
port = 22
password = getpass.getpass('Password for %s@%s: ' % (username, hostname))

hostkeytype = None
hostkey = None
try:
    host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
except IOError:
    try:
        host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
    except IOError:
        print 'Unable to open host keys file'
        host_keys = {}

if host_keys.has_key(hostname):
    hostkeytype = host_keys[hostname].keys()[0]
    hostkey = host_keys[hostname][hostkeytype]
    print 'Using host key of type %s' % hostkeytype
try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password, hostkey=hostkey)
    sftp = paramiko.SFTPClient.from_transport(t)
    try:
        sftp.mkdir(path)
    except IOError:
        print path, " already exists on ", hostname
    sftp.put(ufile, path + "/" + ufile)
    t.close()
    print "Successfully uploaded report file on ", hostname

except Exception, e:
    print 'Exception: %s: %s' % (e.__class__, e)
    try:
        t.close()
    except:
        pass
    sys.exit(1)
