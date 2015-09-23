import yaml

def GenerateConfig(context):

    name = context.env['name']
    project = context.env['project']
    zone = context.properties['zone']
    machine_type = context.properties['machineType']
    network = context.properties['network']
    machine_type_string = 'https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/machineTypes/{machine_type}'.format(zone=zone, project=project, machine_type=machine_type)
    source_image = 'https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20150818'

    startup_script = '''
        #! /bin/bash
        apt-get update
        apt-get install -y build-essential ruby ruby-dev rubygems
        gem install puppet puppet-pip
    '''

    resource_dict = {
        'resources': [{
            'name': name,
            'type': 'compute.v1.instance',
            'properties': {
                'zone': zone,
                'machineType': machine_type_string,
                'disks': [{
                    'autoDelete': True,
                    'boot': True,
                    'deviceName': 'boot',
                    'initializeParams': {
                        'sourceImage': source_image,
                    },
                    'type': 'PERSISTENT'
                }],
                'metadata': {
                    'items': [{
                        'key': 'startup-script',
                        'value': startup_script,
                    }]
                },
                'networkInterfaces': [{
                    'network': '$(ref.%s.selfLink)'%network,
                    'accessConfigs': [{
                        'name': 'External NAT',
                        'type': 'ONE_TO_ONE_NAT',
                    }],
                }],
            },
        }]
    }

    return yaml.dump(resource_dict)