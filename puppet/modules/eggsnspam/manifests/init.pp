class skynet {

  package { ['sqlite3']:
    ensure => present;
  }

  file { '/home/vagrant/skynet':
    ensure => 'link',
    target => '/vagrant',
  }

  file { '/home/vagrant/.virtualenvs':
    ensure => 'directory',
  }

  exec { 'resource title':
    command     => '/home/vagrant/skynet/bin/init_db.sh',
    creates     => '/home/vagrant/skynet/skynet.db',
    cwd         => '/home/vagrant/skynet',
    require     => File['/home/vagrant/skynet'],
  }

  class { 'python' :
    version    => 'system',
    pip        => 'present',
    dev        => 'present',
    virtualenv => 'present',
    gunicorn   => 'absent',
  }

  python::virtualenv { '/home/vagrant/skynet' :
    ensure       => present,
    version      => 'system',
    requirements => '/vagrant/requirements.txt',
    systempkgs   => false,
    distribute   => false,
    venv_dir     => '/home/vagrant/.virtualenvs/skynet',
    owner        => 'vagrant',
    group        => 'vagrant',
    cwd          => '/home/vagrant/skynet',
    require      => [ File['/home/vagrant/.virtualenvs'], File['/home/vagrant/skynet'], Class['python'] ]
  }
}
