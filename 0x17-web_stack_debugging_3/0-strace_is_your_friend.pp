# Fix wordpress file extension

exec {'fix-file-name':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
}
