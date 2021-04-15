# Ansible for PerformanceMQActorSize Experiment 

## How to Use

### Chameleon Cloud Configuration
- Sign into Chameleon Cloud.
- Go to the Project Dashboard
- Identity > Application Credentials
- Create a new Application Credential
  - Choose role 'member'
  - Check box for access 'unrestricted'
- Download the clouds.yaml file
- Download the openrc file
- Click on username in upper righthand corner
- Click on "Openstack RC File"
- Download file
- Save the files to the directory you will run Vagrant in

### Vagrant Configuration
- Open `Vagrantfile` and change the PEM files for your keys registered with Chameleon Cloud

### Ansible Configuration
- Open `.ansible.cfg` and change the PEM files for your key registered with Chameleon Cloud
- Change your username in the `tasks/0*` files
- Change the fork repo in `2_redis_python.yml` to your project fork
- Change the filenames of the producer/consumer in `3_redis_consumer.yml` and `3_redis_producer.yml`

*Note: This will fail on `vagrant up` because of a missing environment variables. You need to source the Openstack RC file after boot.*

```
vagrant up
vagrant ssh
cd /vagrant
source CH-822922-openrc.sh
ansible-playbook playbook_master.yml
```


...
```
