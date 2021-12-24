import json


def read_json_file():
    file_path = "/Users/kojayaku/Documents/ISE/TELEMETRY/jsons/IseTelemetryPrd-ise-base-telemetry-20210331010011.json"
    print('\nparsing telemetry json file : {}'.format(file_path))
    with open(file_path) as f:
        return json.load(f)


def dump_json(json_dict):
    print('\t' + json.dumps(json_dict))


def dump_json_pretty(json_dict):
    print('\t' + json.dumps(json_dict, indent=3))


def get_payload(json_dict):
    return json_dict['data']['payload']['payload']


def get_info(payload, param):
    return payload[param]


json_dict = read_json_file()

# dump the entire json file
# print dump_json(json_dict['telemetryParts'])

# print the number of json
print('\t total number of telemetry objects : {}'.format(len(json_dict['telemetryParts'])))

# dump one of the telemetry data
#print dump_json_pretty(json_dict['telemetryParts'][3])

count = 0
# find number of nodes in deployments
for i in json_dict['telemetryParts']:
    payload = get_payload(i)
    # print dump_json(payload.keys())
    # print dump_json_pretty(payload['DeploymentInfo']['DeploymentInfo']['NodeList']['Node'])
    if 'NodeList' in payload['DeploymentInfo']['DeploymentInfo']:
        print('\t Index {} : total number of nodes in a deployment : {}'.format(count, len(
            payload['DeploymentInfo']['DeploymentInfo']['NodeList']['Node'])))
        no_of_nodes=len(payload['DeploymentInfo']['DeploymentInfo']['NodeList']['Node'])
        if 'Node' in payload['DeploymentInfo']['DeploymentInfo']['NodeList']:
            for j in payload['DeploymentInfo']['DeploymentInfo']['NodeList']['Node']:
                #print dump_json(j)
                if 'Version' in j:
                    #print dump_json(j)
                    print('\t Node Version : {} '.format(j['Version']))

                            # if no_of_nodes>2:
                    #     print dump_json_pretty(payload['DeploymentInfo']['DeploymentInfo']['NodeList'])
                    #     break

                    # dump_json(get_info(payload,'NetworkAccessInfo'))
            count += 1


