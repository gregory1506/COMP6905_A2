import mystorage
import datetime

def loadeventsfrompath(path):
    ''' Loads events from a text files and adds an entry in Event store table and a copy on the processing queue. 
        Returns a message to indicate if anything was added to the queue or Event Store '''
    with open(path,"r") as infile:
        tmp = infile.readlines()
        size = len(tmp) 
        counter = 0
        for index,line in enumerate(tmp):
            if line.startswith("#") or len(line.split()) < 15:
                continue
            sline,rline,soux,souy,recx,recy,d1,d2,d3,sp,d4,rec,fbp,d5,action = line.split()
            if action not in ['add','delete']:
                continue
            try:
                seq = int(sline) % 10000
            except:
                continue
            seq = int(sline) % 10000
            ctime = datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
            spmes = {'PartitionKey': 'Shot-'+ctime, 'RowKey': str(int(sline)*10000+int(sp)),'sou_x' : soux, 'sou_y' : souy, 'event' : action }
            recmes = {'PartitionKey': 'Rec-'+ctime, 'RowKey': str(int(rline)*10000+int(rec)), 'rec_x' : recx, 'rec_y' : recy , 'event' : action}
            tmes = {'PartitionKey': 'Trace-'+ctime, 'RowKey': str(int(sp)*10000+seq)+rline+rec, 'fbp' : float(fbp), 'event' : action }
            mystorage.table_service.insert_entity('Events',spmes)
            mystorage.table_service.insert_entity('Events',recmes)
            mystorage.table_service.insert_entity('Events',tmes)
            mystorage.queue_service.put_message('eventqueue',str(spmes))
            mystorage.queue_service.put_message('eventqueue',str(recmes))
            mystorage.queue_service.put_message('eventqueue',str(tmes))
            counter += 1
            if index % 20 == 0:
                print("completed line "+str(index)+ " of "+str(size))
        print("completed processing file " + path)
    if counter > 0: 
        return "completed processing file " + path
    else:
        return "Error No events added to queue. Check event file"





