def test_backports(Command):
    assert 'backports' in Command('apt-cache policy').stdout
