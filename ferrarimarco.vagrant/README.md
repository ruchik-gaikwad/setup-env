# Ansible Role: Vagrant

* Development branch: [![Build Status](https://travis-ci.org/ferrarimarco/ansible-role-vagrant.svg?branch=development)](https://travis-ci.org/ferrarimarco/ansible-role-vagrant)
* Master branch: [![Build Status](https://travis-ci.org/ferrarimarco/ansible-role-vagrant.svg?branch=master)](https://travis-ci.org/ferrarimarco/ansible-role-vagrant)

Ansible role to install Vagrant

## Usage

### Installation
```
ansible-galaxy install ferrarimarco.vagrant
```

### Example Playbook
```
  - hosts: all
    roles:
      - ferrarimarco.vagrant
```

### Testing the role

This role is tested with [Test-Kitchen](https://github.com/test-kitchen/test-kitchen) configured with the [kitchen-docker](https://github.com/test-kitchen/kitchen-docker) driver,
and [kitchen-inspec](https://github.com/chef/kitchen-inspec)

#### Dependencies

- Bundler, 1.13.0+
- Ruby, 2.3.0+
- Docker, 1.13.0+

#### Test

1. Install Bundler: `gem install bundler`
1. Install required gems from inside the root of the project: `bundle install`
1. Run `kitchen test`
