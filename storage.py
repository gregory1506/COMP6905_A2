from azure.storage.table import TableService, Entity
from azure.storage.queue import QueueService

class AzStore(object):
    def __init__(self):
        self.name = 'Azure storage for assignment'
        self.storage_name = 'comp69052017a25'
        self.storage_key = 'g/VkNQQNh0TAK7tmUpujDjakv6jHnwtyFV/eafy1MQChBHVjATHEcoDDPdjmHMDowt9hjJ0N8afn9AcQRM+EOA=='
        #self.table_service = TableService(account_name='devstoreaccount1', account_key=\
        #                     'Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==',\
        #                      is_emulated=True)
        #self.queue_service = QueueService(account_name='devstoreaccount1', account_key=\
        #                     'Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==',\
        #                     is_emulated=True)
        self.table_service = TableService(account_name=self.storage_name, account_key=self.storage_key)
        self.queue_service = QueueService(account_name=self.storage_name, account_key=self.storage_key)
        if not self.table_service.exists('Events'):
            self.table_service.create_table('Events')
        if not self.table_service.exists('Shots'):
            self.table_service.create_table('Shots')
        if not self.table_service.exists('Recievers'):
            self.table_service.create_table('Recievers')
        if not self.table_service.exists('Traces'):
            self.table_service.create_table('Traces')
        self.queue_service.create_queue('eventqueue')

def createStorage():
    return AzStore()

mystorage = createStorage()