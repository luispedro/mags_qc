import subprocess
from os import path, makedirs
from jug import TaskGenerator


@TaskGenerator
def download_checkm2_database():
    """
    Downloads the CheckM2 database to the current working directory.
    """
    databases_dir = path.join(path.abspath('.'), 'databases')
    makedirs(databases_dir, exist_ok=True)

    subprocess.check_call(
            ['checkm2', 'database',
             '--download',
             '--path', databases_dir])
    return databases_dir


@TaskGenerator
def run_checkm2(databases_dir):

    subprocess.check_call(
            ['checkm2', 'predict',
             '--input', 'data',
             '--output-directory', 'checkm2_output',
             '-x', '.fna.gz',
             '--database_path', databases_dir + '/CheckM2_database/uniref100.KO.1.dmnd'])
    return 'checkm2_output'


database_dir = download_checkm2_database()
run_checkm2(database_dir)


