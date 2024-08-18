#this is going to Fix the  bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.
#Using strace

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
