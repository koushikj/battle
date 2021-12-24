# importing the requests library
from datetime import datetime

import requests
import time
import json
import logging

# api-endpoint
from requests.auth import HTTPBasicAuth

logging.basicConfig(filename=datetime.now().strftime('mnt_query_%H_%M_%d_%m_%Y.log'),
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Let us Create an object
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

count = 0
while True:
    logger.info("mnt call - {}".format(count))
    URL = "https://10.126.68.193/admin/API/mnt/Telemetry/getAuthTypeInfoData"
    try:
        start = time.time()
        r = requests.get(
            URL,
            auth=HTTPBasicAuth('admin', 'Lab123'),
            verify=False
        )
        timetaken = time.time() - start
        # extracting data in json format
        data = r.json()
        endpoint_count = data['authTypeInfoUniqueMacAddressPassedFailed'][0]['endpointCount']
        session_count = data['authTypeInfoSessionCounts'][0]['sessionCount']
        logger.info('response = {}'.format(json.dumps(data)))
        logger.info('sessionCount = {} , endpointCount = {} and time taken to query (in minutes) = {}'.format(session_count,endpoint_count, timetaken / 60))
        #logger.info('time taken (in minutes) = {}'.format(timetaken / 60))
    except Exception as e:
        logger.error('Failed to get response {}'.format(e))
    logger.info("-----------------------------------------------------------------")
    time.sleep(001)
    count = count+1
