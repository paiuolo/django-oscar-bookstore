from fabric.api import run, sudo, execute, settings

def su(pwd, command):
    with settings(
        password= "%s" % pwd,
        sudo_prefix="su - -c ",
        sudo_prompt="Password:"
        ):
        sudo(command)

def install_deps(packages):
    run('su -c \'apt-get update && apt-get install '+packages+'\'')
    #execute(su, pwd, 'apt-get update && apt-get install '+packages)

def create_dir(project_name):
    run('mkdir -p '+project_name)

def create_virtualenv(project_name):
    run('cd '+project_name+' && python3 -m venv virtualenv')

def install_python_deps(project_name):
    cmds = [
        'cd '+project_name,
        'source virtualenv/bin/activate',
        'pip install git+https://github.com/paiuolo/django-oscar.git',
        'pip install pycountry django-compressor django-debug-toolbar django-ckeditor redis',
        'pip install -U celery[redis]',
        'pip install git+https://github.com/paiuolo/django-oscar-paypal@modifiche_python3_utf'
        ]
    cmd = str.join(' && ', cmds)
    run(cmd)
    
def clone_repo(project_name, repo_url):
    run('cd '+project_name+' && git clone '+repo_url)
    
def init_repo(project_name, repo_name):
    cmds = [
        'cd '+project_name,
        'source virtualenv/bin/activate',
        'cd '+repo_name,
        'git checkout -b '+project_name,
        './manage.py makemigrations',
        './manage.py makemigrations paypal',
        './manage.py migrate',
        './manage.py oscar_populate_countries',
        './manage.py loaddata bookstore/fixtures/initial_data.json',
        ]
    cmd = str.join(' && ', cmds)
    run(cmd)
    
def run_tests(project_name, repo_name):
    cmds = [
        'cd '+project_name,
        'source virtualenv/bin/activate',
        'cd '+repo_name,
        './manage.py test apps.books',
        ]
    cmd = str.join(' && ', cmds)
    run(cmd)
    