import json


def read_json_file():
    dir = '/Users/kojayaku/Documents/ISE/TELEMETRY/jsons/'
    file_name = 'IseTelemetryDev-20200511000010.json'
    file_path = dir + file_name
    file_path = "/Users/kojayaku/Documents/Koushik/pycharm/test/ise-telemetry.json"
    print('\nparsing telemetry json file : {}'.format(file_path))
    with open(file_path) as f:
        return json.load(f)


def dump_json(json_dict):
    print('\t' + json.dumps(json_dict))


def dump_json_pretty(json_dict):
    print('\t' + json.dumps(json_dict, indent=3))


def get_payload(json_dict):
    return json_dict[0]['payload']['payload']


def get_info(payload, param):
    return payload[param]


json_dict = read_json_file()
payload = get_payload(json_dict)
#print dump_json(payload.keys())
nad_info = payload['NADInfo']['NADInfo']['NodeList']['Node']['NAD']
print('\tNAD size {}'.format(len(nad_info)))
name_set= set()
for i in nad_info:
    #print dump_json_pretty(i['Name'])
    #print type(i['Name'])
    name_set.add(type(i['Name']))

print name_set
# dump_json(get_info(payload,'NetworkAccessInfo'))
