# Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password.

file_line {'Turn off passwd auth':
  line => 'PasswordAuthentication no',
  path => '/etc/ssh/sshd_config',
  match => '^PasswordAuthentication no',
  ensure => 'present',
}

file_line {'Declare identity file':
  line => 'DeclareIdentity ~/.ssh/school',
  path => '/etc/ssh/sshd_config',
  ensure => 'present',
}
