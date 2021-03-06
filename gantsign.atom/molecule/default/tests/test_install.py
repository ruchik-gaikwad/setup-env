import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_atom(Command):
    assert Command('which atom').rc == 0


def test_apm(Command):
    assert Command('apm --version').rc == 0
