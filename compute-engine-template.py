import yaml

def GenerateConfig(context):

    network_name = 'a-new-network'
    zone = 'europe-west1-d'

    resource_dict = {
        'resources': 
        [
            {
                'name': 'the-first-vm',
                'type': 'vm-template.py',
                'properties':{
                    'network': network_name,
                    'zone': zone,
                    'machineType': 'f1-micro',
                },
            },
            {
                'name': 'the-second-vm',
                'type': 'vm-template.py',
                'properties':{
                    'network': network_name,
                    'zone': zone,
                    'machineType': 'g1-small',
                }
            },
            {
                'name': network_name,
                'type': 'network-template.py'
            },
            {
                'name': '%s-firewall'%network_name,
                'type': 'firewall-template.py',
                'properties':{
                    'network': network_name
                },
            },
        ]
    }

    return yaml.dump(resource_dict)
