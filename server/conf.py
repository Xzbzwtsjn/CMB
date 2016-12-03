import sys
import os

MesosMasterAddress = ['172.29.152.185','172.29.152.186','172.29.152.188']

MesosMasterPort = 5050

dbRoot = os.path.abspath('.') + '/db/sqlite.db'
dbPath = "sqlite:///db/sqlite.db"

template_path = os.path.join(os.path.dirname(__file__),'templates')


Cassandra = '172.29.152.188'
CassandraListenPort = 29953

backEnd = 'tcp://127.0.0.1:4242'
