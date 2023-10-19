# Resolve the error: Too many open files on Nginx Server

exec {'fix-too-many-open-files':
  command => '/usr/bin/env sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx'
}

exec {'restart-nginx':
  command => '/usr/bin/env service nginx restart'
}
