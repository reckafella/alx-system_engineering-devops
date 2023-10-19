# Change OS config so it is possible to login with "holberton" user and open
# files without an error message

user {'holberton':
  ensure     => 'present',
  name       => 'holberton',
  home       => '/home/holberton',
  managehome => true,
}

exec {'increase-hard-limit':
  command => 'sed -i "/holberton hard /s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/bin:/bin',
}

exec {'increase-soft-limit':
  command => 'sed -i "/holberton soft /s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/bin:/bin',
}
