import yaml

def GenerateConfig(context):

    name = context.env['name']

    resource_dict = {
        'resources': [{
            'name': name,
            'type': 'compute.v1.network',
            'properties':{
                'IPv4Range': '10.0.0.1/16',
            }
        }]
    }

    return yaml.dump(resource_dict)