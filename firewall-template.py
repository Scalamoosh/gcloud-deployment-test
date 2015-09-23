import yaml

def GenerateConfig(context):

    name = context.env['name']
    network = context.properties['network']

    resource_dict = {
        'resources': [{
            'name': name,
            'type': 'compute.v1.firewall',
            'properties':{
                'network': '$(ref.%s.selfLink)'%network,
                'sourceRanges': ["0.0.0.0/0"],
                'allowed':[{
                    'IPProtocol': 'TCP',
                    'ports': ["80"],
                },
                {
                    'IPProtocol': 'TCP',
                    'ports': ["443"],
                },
                {
                    'IPProtocol': 'TCP',
                    'ports': ["22"],
                }]
            }
        }]
    }

    return yaml.dump(resource_dict)