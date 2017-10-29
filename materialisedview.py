from storage import mystorage
from flask_table import Table, Col

class RecieverTable(Table):
    PartitionKey = Col('PartitionKey')
    RowKey = Col('RowKey')
    Timestamp = Col('Timestamp')
    #etag = Col('etag')
    rec_x = Col('rec_x')
    rec_y = Col('rec_y')

class ShotTable(Table):
    PartitionKey = Col('PartitionKey')
    RowKey = Col('RowKey')
    Timestamp = Col('Timestamp')
    #etag = Col('etag')
    sou_x = Col('sou_x')
    sou_y = Col('sou_y')

class TraceTable(Table):
    PartitionKey = Col('PartitionKey')
    RowKey = Col('RowKey')
    Timestamp = Col('Timestamp')
    #etag = Col('etag')
    fbp = Col('fbp')

class SummaryTable(Table):
    Entity = Col('Entity')
    Total = Col('Total')

def getRecQuery():
    recquery = [] 
    for task in mystorage.table_service.query_entities('Recievers', num_results=10):
        recquery.append(task)
    return RecieverTable(recquery, border=True).__html__()

def getShotQuery():
    shotquery = [] 
    for task in mystorage.table_service.query_entities('Shots', num_results=10):
        shotquery.append(task)
    return ShotTable(shotquery, border=True).__html__()

def getTrcQuery():
    tracequery = [] 
    for task in mystorage.table_service.query_entities('Traces', num_results=10):
        tracequery.append(task)
    return TraceTable(tracequery, border=True).__html__()

def getSummary():
    totalshot,totalrec,totaltrc = (0,0,0)
    for ts in mystorage.table_service.query_entities('Shots', filter="PartitionKey eq 'Shot'"):
        totalshot +=1
    for tr in mystorage.table_service.query_entities('Recievers', filter="PartitionKey eq 'Reciever'"):
        totalrec +=1
    for tt in mystorage.table_service.query_entities('Traces', filter="PartitionKey eq 'Trace'"):
        totaltrc +=1
    return SummaryTable([{'Entity': 'Shot','Total': totalshot},{'Entity': 'Reciever','Total': totalrec},{'Entity': 'Trace','Total': totaltrc}], border=True).__html__()

