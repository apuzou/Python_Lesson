import yaml

with open('config.yaml', 'w') as yaml_file:
    yaml.dump({
        'debug': True,
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'database': {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'password',
            'database': 'test_db'
        }
    }, yaml_file, default_flow_style=False)