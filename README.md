# CMB
Cloud Metering and Billing

# Denpendence

    pip install Jinja2

    pip install Werkzeug

    pip install sqlalchemy

    pip install simplejson

# API
  monthlyBill

    curl http://ip:port/monthlyBill?keyword=8&type=date

  dailyBill
    curl http://ip:port/dailyBill?keyword=2015-06-06&type=date

  getMachine
    curl http://ip:port/getMachine?pid=slave(1)@172.29.152.188:5051
  Response:

  getResources
    curl http://ip:port/getResources
  Response:
    [{'active': True, 'hostname': 'master3', 'pid': 'slave(1)@172.29.152.188:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S2'}, 
     {'active': True, 'hostname': 'slave1', 'pid': 'slave(1)@172.29.152.181:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S9'}, 
     {'active': True, 'hostname': 'master2', 'pid': 'slave(1)@172.29.152.186:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S6'}, 
     {'active': True, 'hostname': 'master1', 'pid': 'slave(1)@172.29.152.185:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S4'}, 
     {'active': True, 'hostname': 'slave3', 'pid': 'slave(1)@172.29.152.183:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S8'}, 
     {'active': True, 'hostname': 'slave6', 'pid': 'slave(1)@172.29.152.184:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S7'}, 
     {'active': True, 'hostname': 'slave2', 'pid': 'slave(1)@172.29.152.182:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S0'}, 
     {'active': True, 'hostname': 'slave7', 'pid': 'slave(1)@172.29.152.189:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S3'}, 
     {'active': True, 'hostname': 'slave5', 'pid': 'slave(1)@172.29.152.187:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S1'}, 
     {'active': True, 'hostname': 'slave4', 'pid': 'slave(1)@172.29.152.190:5051', 'id': '3b23bbfe-f950-4e09-9517-078205515035-S5'}]
