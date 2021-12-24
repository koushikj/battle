import os
import json

REMOTE_SERVER_AVRO_FILES_LOCATION = '/root/avro_validation/'
GENERATED_AVRO_FILE = 'testtelemetry.avro'
DECODED_FINAL_JSON = 'decoded_telemetry.json'

TELEMETRY_DATA_FILE = 'ise-telemetry.json'
TELEMETRY_AVRO_SCHEMA_FILE = 'ise-telemetry.avsc'
TELEMETRY_AVRO_UTIL = 'avroutil.py'

telemetryJsonFilePath = os.path.dirname(os.path.realpath(__file__)) + "/" + TELEMETRY_DATA_FILE
avscFilePath = "/Users/kojayaku/Documents/GitHub/ise/cpm/jars/infrastructure/telemetry/src/main/resources/avro-schema/" + TELEMETRY_AVRO_SCHEMA_FILE
avroUtilFilePath = os.path.dirname(os.path.realpath(__file__)) + "/" + TELEMETRY_AVRO_UTIL

def getFQN(stack_for_fqn):
    return ":".join(stack_for_fqn)


def getData(data, stack_for_fqn, final_data):
    for key, value in data.items():
        if (isinstance(value, dict) or isinstance(value, list)):
            stack_for_fqn.append(key)
        elif "xmlns" not in key:
            final_data.add(getFQN(stack_for_fqn) + ":" + key)

        if (isinstance(value, dict)):
            getData(value, stack_for_fqn, final_data)
        elif (isinstance(value, list)):
            for aElem in value:
                getData(aElem, stack_for_fqn, final_data)

        if (isinstance(value, dict) or isinstance(value, list)):
            stack_for_fqn.pop()


def getAllData(data):
    stack_for_fqn = []
    final_data = set()
    getData(data, stack_for_fqn, final_data)
    return final_data


class avro_validation():
    def __init__(self):
        pass

    def testAvroValidation(self):
        print("##########################")
        print("read {}".format(telemetryJsonFilePath))
        with open(telemetryJsonFilePath) as f:
            datastore = json.load(f)
        datastore = datastore['payload']
        print(datastore)
        print("##########################")

        avro_validation_cmd = 'python2.7 {} validate -s {} -d {}'.format(TELEMETRY_AVRO_UTIL, TELEMETRY_AVRO_SCHEMA_FILE,
                                                                      TELEMETRY_DATA_FILE)
        print(avro_validation_cmd)

        encode_cmd = 'python2.7 {} encode -s {} -d {} -o {}'.format(TELEMETRY_AVRO_UTIL, TELEMETRY_AVRO_SCHEMA_FILE,
                                                                 TELEMETRY_DATA_FILE, GENERATED_AVRO_FILE)
        print(os.system(encode_cmd))

        decode_cmd = 'python2.7 {} decode -a {} > {}'.format(TELEMETRY_AVRO_UTIL, GENERATED_AVRO_FILE,
                                                          DECODED_FINAL_JSON)

        print(os.system(decode_cmd))


        # os.system(
        #     'rm {} {} {} {} {}'.format(TELEMETRY_AVRO_UTIL, DECODED_FINAL_JSON, TELEMETRY_AVRO_SCHEMA_FILE,
        #                                TELEMETRY_DATA_FILE, GENERATED_AVRO_FILE))

        telemetry_data = sorted(getAllData(datastore))

        with open(DECODED_FINAL_JSON) as f:
            datastore = json.load(f)

        final_data = sorted(getAllData(datastore))

        diff = set(telemetry_data).difference(set(final_data))

        print(diff)

        assert (not diff)


if __name__ == '__main__':
    validate = avro_validation()
    validate.testAvroValidation()
