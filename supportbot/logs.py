
import logging

# Create and configure logger
logging.basicConfig(filename="supportbot.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

log = logging.getLogger()
