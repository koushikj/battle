import json


def read_json_file():
    dir_name = '/Users/kojayaku/Documents/ISE/TELEMETRY/jsons/'
    file_name = 'IseTelemetryPrd-ise-base-telemetry-20211210010013.json'
    file_path = dir_name + file_name
    pretty_print_output_30space('parsing telemetry json file',file_path)
    with open(file_path) as f:
        return json.load(f)


def convert_set_to_list(dict_with_set_value):
    for key in dict_with_set_value:
        val = dict_with_set_value[key]
        if isinstance(val, set):
            dict_with_set_value[key] = list(val)
    return dict_with_set_value


def write_to_file(data, fine_name):
    with open(fine_name, 'w') as f:
        json.dump(data, f)


def dump_json(json_dict):
    print('\t' + json.dumps(json_dict))


def dump_json_pretty(json_dict):
    print('\t' + json.dumps(json_dict, indent=3))


def get_payload(json_dict):
    return json_dict['data']['payload']['payload']


def get_info(payload, param):
    return payload[param]


def pretty_print_header(string):
    delimiter = '--------------------------------------'
    print '\n{:10s} {} {:10s}'.format(delimiter, string, delimiter)


def pretty_print_output_80spaces(string, count):
    print '{:80s}: {}'.format(string, count)


def pretty_print_output_30space(string, count):
    print '{:30s}: {}'.format(string, count)


def pretty_print_output_80spaces_diff_count(string, count, difference):
    print '{:80s}: {} ({})'.format(string, count, difference)


def get_nad_info(nad_info_count, payload, deployment_id):
    if 'NADInfo' in payload and 'NADInfo' in payload['NADInfo']:
        nad_info_whole = payload['NADInfo']
        nad_info = nad_info_whole['NADInfo']
        if 'DeploymentID' in nad_info:
            nad_info_count = nad_info_count + 1
            if nad_info['DeploymentID'] == deployment_id:
                pretty_print_output_30space('NADInfo', json.dumps(nad_info_whole))
    return nad_info_count


def get_network_access_info(network_access_info_count, payload, deployment_id):
    if 'NetworkAccessInfo' in payload and 'NetworkAccessInfo' in payload['NetworkAccessInfo']:
        network_access_info_whole = payload['NetworkAccessInfo']
        network_access_info = network_access_info_whole['NetworkAccessInfo']
        if 'DeploymentID' in network_access_info:
            network_access_info_count = network_access_info_count + 1
            if network_access_info['DeploymentID'] == deployment_id:
                pretty_print_output_30space('NetworkAccessInfo', json.dumps(network_access_info_whole))
    return network_access_info_count


def get_deployment_info(deployment_info_count, payload, deployment_id):
    if 'DeploymentInfo' in payload and 'DeploymentInfo' in payload['DeploymentInfo']:
        deployment_info_whole = payload['DeploymentInfo']
        deployment_info = deployment_info_whole['DeploymentInfo']
        if 'DeploymentID' in deployment_info:
            deployment_info_count = deployment_info_count + 1
            if deployment_info['DeploymentID'] == deployment_id:
                pretty_print_output_30space('Full Telemetry JSON', json.dumps(payload))
                pretty_print_output_30space('DeploymentInfo', json.dumps(deployment_info_whole))
    return deployment_info_count


def get_deployment_id_and_ise_version(version_mapping, payload):
    deployment_ids = set()
    if 'DeploymentInfo' in payload and 'DeploymentInfo' in payload['DeploymentInfo']:
        deployment_info_whole = payload['DeploymentInfo']
        deployment_info = deployment_info_whole['DeploymentInfo']
        if 'DeploymentID' in deployment_info and 'NodeList' in deployment_info and 'Node' in deployment_info[
            'NodeList']:
            nodes = deployment_info['NodeList']['Node']
            dep_id = deployment_info['DeploymentID']
            deployment_ids.add(dep_id)
            if isinstance(nodes, list):
                for node in nodes:
                    if 'Version' in node and isinstance(node['Version'], unicode):
                        version = node['Version']
                        if version in version_mapping:
                            version_mapping[version].update(deployment_ids)
                        else:
                            version_mapping[version] = deployment_ids

            elif isinstance(nodes, dict):
                if 'Version' in nodes and isinstance(nodes['Version'], unicode):
                    version = nodes['Version']
                    if version in version_mapping:
                        version_mapping[version].update(deployment_ids)
                    else:
                        version_mapping[version] = deployment_ids
    return version_mapping


def main():
    print ('\n')
    json_dict = read_json_file()
    pretty_print_output_30space('length of telemetryParts', len(json_dict['telemetryParts']))
    deployment_id = '05b5bead-fecb-47da-8489-1a49f40ff859'
    count = 0
    nad_info_count = 0
    network_access_info_count = 0
    deployment_info_count = 0
    version_mapping = {}
    file_name_versions_deployment_id = 'versions-deployment-ids.json'
    pretty_print_header('getting data for deployment id : {}'.format(deployment_id))
    for i in json_dict['telemetryParts']:
        payload = get_payload(i)
        count = count + 1
        deployment_info_count = get_deployment_info(deployment_info_count, payload, deployment_id)
        nad_info_count = get_nad_info(nad_info_count, payload, deployment_id)
        network_access_info_count = get_network_access_info(network_access_info_count, payload, deployment_id)
        version_mapping = get_deployment_id_and_ise_version(version_mapping, payload)
    pretty_print_header('summary')
    pretty_print_output_80spaces('total telemetry jsons counts', count)
    pretty_print_output_80spaces_diff_count('total deployment info counts ', deployment_info_count,
                                            deployment_info_count - count)
    pretty_print_output_80spaces_diff_count('total nad info counts', nad_info_count, nad_info_count - count)
    pretty_print_output_80spaces_diff_count('total network access info counts', network_access_info_count,
                                            network_access_info_count - count)
    write_to_file(convert_set_to_list(version_mapping), file_name_versions_deployment_id)
    pretty_print_output_80spaces('version-deployment Ids mapping is written to the file',
                                 file_name_versions_deployment_id)


main()
