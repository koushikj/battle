import os
import json

TELEMETRY_DATA_FILE = 'ise-telemetry.json'
TELEMETRY_AVRO_SCHEMA_FILE = 'ise-telemetry.avsc'
TELEMETRY_AVRO_UTIL = 'avroutil.py'

telemetryJsonFilePath = os.path.dirname(os.path.realpath(__file__)) + "/" + TELEMETRY_DATA_FILE
avscFilePath = "/Users/kojayaku/Documents/Koushik/pycharm/test/ise-telemetry-rowan.avsc"
avscFilePath_ise = "/Users/kojayaku/Documents/Koushik/pycharm/test/ise-telemetry.avsc"
avroUtilFilePath = os.path.dirname(os.path.realpath(__file__)) + "/" + TELEMETRY_AVRO_UTIL


def write_data(data):
    with open('data.json', 'w') as f1:
        json.dump(data, f1)


def update_ise_data(data):
    with open(avscFilePath_ise,'r') as f2:
        avro_data = json.load(f2)
        avro_data['fields'] = data
        print avro_data

    with open(avscFilePath_ise, 'w') as f3:
        json.dump(avro_data, f3)


if __name__ == '__main__':
    with open(avscFilePath) as f:
        avro_data = json.load(f)
        print('actual avro file content {} :'.format(avro_data))
    if 'fields' in avro_data:
        for fields in avro_data['fields']:
            if fields['name'] == 'payload':
                print fields['type']
                for f in fields['type']['fields']:
                    if f['name'] == 'payload':
                        #write_data(f['type']['fields'])
                        update_ise_data(f['type']['fields'])

        # datastore = avro_data['fields']
        # print (datastore)
