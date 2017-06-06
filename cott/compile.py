from jinja2 import Environment, FileSystemLoader
from os.path import join, abspath, realpath, dirname


THIS_DIR = dirname(abspath(__file__))
TEMPLATE_DIR = join(dirname(THIS_DIR), 'templates')


def print_html_doc():
    j2_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)
    print(j2_env.get_template('test.txt').render(title='Hellow Gist from GutHub'))


def run():
    print_html_doc()
