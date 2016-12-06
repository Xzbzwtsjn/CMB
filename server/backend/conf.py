import sys
import os

MesosMasterAddress = ['172.29.152.185','172.29.152.186','172.29.152.188']
MesosMasterPort = 5050

ChronosMaster = '172.29.152.185'
ChronosPort = 4400

Cassandra = '172.29.152.188'
CassandraListenPort = 29953

dbRoot = os.path.split(os.path.realpath(__file__))[0] + '/db/sqlite.db'
dbPath = "sqlite:///db/sqlite.db"

