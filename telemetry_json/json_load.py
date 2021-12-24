import json

def scp_files(files):
    print('scp following files {}'.format(files))

with open('3.0.0.328.json') as f:
    datastore = json.load(f)
    print('full content {} :'.format(datastore))
    if 'payload' not in datastore:
        print ('json does not contain payload')
    else:
        print ('json contains payload')

files=['abc','deg','121'];
scp_files(files)

with open('3.0.0.328_payload.json', 'w') as f:
    datastore = datastore['payload']
    print ('payload content {} :'.format(datastore))
    if 'payload' not in datastore:
        print ('json does not contain payload')
    else:
        print ('json contains payload')
    json.dump(datastore, f)

