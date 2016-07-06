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
    
def create_digital_files_dir(user_name, repo_name):
    dfd = '/srv/'+repo_name+'/digital_products'
    run('su -c \'mkdir -p /srv/'+repo_name+' && mkdir -p '+dfd+' && chown '+user_name+' '+dfd+'\'')

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
    
def nginx_uwsgi_setup_config(project_name, repo_name, domain_name):
    config_dir = repo_name+'/deploy/config/'
    cmds = [
        'cd '+project_name,
        'sed -i -e "s:__DOMINIO__:'+domain_name+':g" ./'+config_dir+'nginx.conf -e "s:__CARTELLA__:"`pwd`":g" ./'+config_dir+'nginx.conf',
        'sed -i -e "s:__DOMINIO__:'+domain_name+':g" ./'+config_dir+'uwsgi.ini -e "s:__CARTELLA__:"`pwd`":g" ./'+config_dir+'uwsgi.ini',
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
    