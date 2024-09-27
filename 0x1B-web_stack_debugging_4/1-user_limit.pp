#this will Change the configuration of OS so that it can possible to login with the
#holberton user and able to open mutiple files without any errors.

exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
