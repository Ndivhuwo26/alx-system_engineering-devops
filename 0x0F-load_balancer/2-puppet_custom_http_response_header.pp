#this will  Ensure the system is updated
exec { 'update system':
  command => '/usr/bin/apt-get update -y',
  path    => ['/usr/bin', '/usr/sbin'],
}

# this will Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update system'],
}

#this will  Create the index.html file with Hello World content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

#this will Add the redirect rule to the Nginx configuration
exec { 'redirect_me':
  command  => 'sed -i "/server_name _;/a\\\t\\trewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
  notify   => Service['nginx'], # Restart Nginx if the file changes
}

#this will Add the custom HTTP header to the Nginx configuration
exec { 'HTTP header':
  command  => 'sed -i "/server_name _;/a\\\t\\tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
  notify   => Service['nginx'], # Restart Nginx if the file changes
}

#this will  Ensure Nginx service is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => Exec['redirect_me', 'HTTP header'], # Subscribe to changes in execs
}

