# scout-vagrant
Vagrantfile and provisioning tasks for the scout project

**To get started:**

    1. Install Vagrant: https://www.vagrantup.com/
    2. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
    3. Install ansible: sudo pip install ansible
    
**Install**

    $ git clone https://github.com/uw-it-aca/scout-vagrant.git 
    $ cd scout-vagrant
    $ git submodule init
    $ git submodule update
    $ vagrant plugin install vagrant-host-shell
    $ MY_VAR='scout' vagrant up

To reload configuration changes: 
    
    $ MY_VAR='scout' vagrant reload --provision

To start fresh: 
    
    $ vagrant destroy
    $ MY_VAR='scout' vagrant up

**Run your Django server (from Vagrant):**
    
    $ vagrant ssh 
    vagrant@vagrant $ cd /vagrant/venv
    vagrant@vagrant $ source bin/activate
    (venv)vagrant@vagrant $ cd scoutproject
    (venv)vagrant@vagrant $ python manage.py runserver 0:8000
