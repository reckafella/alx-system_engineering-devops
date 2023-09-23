# A script to create a file in /tmp folder
$doc_root = '/tmp'

file {$doc_root:
  ensure => 'directory'
}

file {"${doc_root}/school":
  ensure  => 'present',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
  require => File[$doc_root]
}
