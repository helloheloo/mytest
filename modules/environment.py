import os

name = 'environment'


def run(**args):
    print('[*] In environment module.')
    return str(os.environ)
