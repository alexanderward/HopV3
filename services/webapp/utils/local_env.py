import yaml
import os


def set_env_vars(base_dir):
    with open(os.path.join(base_dir, "../../docker-compose.yml"), 'r') as f:
        data = yaml.full_load(f)

    for item in data['services']['webapp']['environment']:
        key, value = item.split('=')
        if 'HOST' in key:
            value = "localhost"
        os.environ[key] = value
