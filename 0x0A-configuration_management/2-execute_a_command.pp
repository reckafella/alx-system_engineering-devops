# Execute a command using 'pkill' to kill a program called 'killmenow'

exec {'killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
