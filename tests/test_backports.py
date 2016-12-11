from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_backports(Command):
    assert 'backports' in Command('apt-cache policy').stdout
