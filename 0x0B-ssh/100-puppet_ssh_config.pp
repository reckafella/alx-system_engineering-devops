# Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that
# you can connect to a server without typing a password.

file_line {'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication no',
}

file_line {'Declare identity file':
  path => '/etc/ssh/sshd_config',
  line => 'DeclareIdentity ~/.ssh/school',
}
