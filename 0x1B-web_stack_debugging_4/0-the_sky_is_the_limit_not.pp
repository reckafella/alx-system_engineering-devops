# Resolve the error: Too many open files on Nginx Server

exec {'fix-too-many-open-files':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 9999\"/" /etc/default/nginx'
}

exec {'restart-nginx':
  command => 'sudo service nginx restart'
}
