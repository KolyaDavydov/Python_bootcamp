import yaml


with open('../../materials/todo.yml', 'r') as file:
    todo = yaml.load(file, yaml.FullLoader)
deploy = [{
    'name': 'Playbook',
    'hosts': 'localhost',
    'become': 'yes',
    'tasks': [
        {
            'name': 'Installation packeges',
            'ansible.builtin.apt': {
                'name': '{{ item }}'
            },
            'loop': todo['server']['install_packages'],
        },
        {
            'name': 'Copying files',
            'ansible.builtin.copy': {
                'src': '{{ item.src }}',
                'dest': '{{ item.dest }}',
            },
            'loop': [
                {
                    'src': '../EX00/exploit.py',
                    'dest': 'exploit.py',
                },
                {
                    'src': '../EX01/consumer.py',
                    'dest': 'consumer.py'
                },
                {
                    'src': '../EX01/producer.py',
                    'dest': 'producer.py'
                },
            ]
        },
        {
            'name': 'Run files',
            'shell': {
                'cmd': '{{ item.cmd }}',
            },
            'loop': [
                {
                    'cmd': 'python3 exploit.py',
                },
            ],
        },
    ],
}]
with open('deploy.yml', 'w') as file:
    yaml.dump(deploy, file, sort_keys=False, default_flow_style=False)