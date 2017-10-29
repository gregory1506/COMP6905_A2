from storage import mystorage
from azure.storage.table import Entity
import datetime
import json

# process the queue
def processQueue():
    ''' Processes the Queue of events. Based on tags in the message different events triggered.
        Returns message to indicate if queue processed.'''
    if mystorage.queue_service.get_queue_metadata('eventqueue').approximate_message_count == 0:
        return "Warning Queue is empty"
    mescounter = 0
    while mystorage.queue_service.get_queue_metadata('eventqueue').approximate_message_count > 0:
        messages = mystorage.queue_service.get_messages('eventqueue',num_messages=20)
        for message in messages:
            mescounter += 1
            event = message.content.replace("'","\"") # make json friendly
            if "Shot-" in event:
                entity = json.loads(event) # dictionary representing entity
                if entity['event'] == 'add':
                    new_entity = Entity()
                    new_entity.PartitionKey = 'Shot'
                    new_entity.RowKey = entity['RowKey']
                    new_entity.sou_x = entity['sou_x']
                    new_entity.sou_y = entity['sou_y']
                    try:
                        mystorage.table_service.get_entity('Shots',new_entity.PartitionKey,new_entity.RowKey)
                        pass
                    except:
                        mystorage.table_service.insert_entity('Shots',new_entity)
                if entity['event'] == 'delete':
                    try:
                        mystorage.table_service.delete_entity('Shots','Shot',entity['RowKey'])
                    except:
                        print("cant delete "+event)
                        pass
            elif "Rec-" in event:
                entity = json.loads(event)
                if entity['event'] == 'add':
                    new_entity = Entity()
                    new_entity.PartitionKey = 'Reciever'
                    new_entity.RowKey = entity['RowKey']
                    new_entity.rec_x = entity['rec_x']
                    new_entity.rec_y = entity['rec_y']
                    try:
                        mystorage.table_service.get_entity('Recievers',new_entity.PartitionKey,new_entity.RowKey)
                        pass
                    except:
                        mystorage.table_service.insert_entity('Recievers',new_entity)
                if entity['event'] == 'delete':
                    try:
                        mystorage.table_service.delete_entity('Recievers','Reciever',entity['RowKey'])
                    except:
                        print("cant delete "+event)
                        pass
            elif "Trace-" in event:
                entity = json.loads(event)
                if entity['event'] == 'add':
                    new_entity = Entity()
                    new_entity.PartitionKey = 'Trace'
                    new_entity.RowKey = entity['RowKey']
                    new_entity.fbp = entity['fbp']
                    try:
                        mystorage.table_service.get_entity('Traces',new_entity.PartitionKey,new_entity.RowKey)
                        pass
                    except:
                        mystorage.table_service.insert_entity('Traces',new_entity)
                if entity['event'] == 'delete':
                    try:
                        mystorage.table_service.delete_entity('Traces','Trace',entity['RowKey'])
                    except:
                        print("cant delete "+event)
                        pass
            else:
                print(message.id, " is not actionable")
            mystorage.queue_service.delete_message('eventqueue', message.id, message.pop_receipt)
        if mescounter % 20 == 0:
            print("Processed "+str(mescounter)+" events in queue")
    print("Completed processing Queue")
    return "Completed processing Queue"
