from jinja2 import Environment, FileSystemLoader
from os.path import join, abspath, realpath, dirname
import json


THIS_DIR = dirname(abspath(__file__))
TEMPLATE_DIR = join(dirname(THIS_DIR), 'templates')


def print_simple_data(filename):
    data = json.loads(open(filename).read())
    j2_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
    print(j2_env.get_template('simple_article.j2').render({'article': data}))


