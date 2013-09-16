
import subprocess
import sys
import setup_util
import os
from os.path import expanduser

home = expanduser("~")

def start(args):
  setup_util.replace_text("php-fatfree/index.php", "host=.*;", "host=" + args.database_host + ";")
  setup_util.replace_text("php-fatfree/deploy/php", "\".*\/FrameworkBenchmarks", "\"" + home + "/FrameworkBenchmarks")
  setup_util.replace_text("php-fatfree/deploy/php", "Directory .*\/FrameworkBenchmarks", "Directory " + home + "/FrameworkBenchmarks")
  setup_util.replace_text("php-fatfree/deploy/nginx.conf", "root .*\/FrameworkBenchmarks", "root " + home + "/FrameworkBenchmarks")
  
  try:
    if os.name == 'nt':
      subprocess.check_call('appcmd add site /name:PHP /bindings:http/*:8080: /physicalPath:"C:\\FrameworkBenchmarks\\php-fatfree"', shell=True)
      return 0
    
    #subprocess.check_call("sudo cp php-fatfree/deploy/php /etc/apache2/sites-available/", shell=True)
    #subprocess.check_call("sudo a2ensite php", shell=True)
    #subprocess.check_call("sudo /etc/init.d/apache2 start", shell=True)
    
    subprocess.check_call("sudo chown -R www-data:www-data php-fatfree", shell=True)
    subprocess.check_call("sudo chmod -R www-data:www-data php-fatfree", shell=True)
    subprocess.check_call("sudo php-fpm --fpm-config config/php-fpm.conf -g " + home + "/FrameworkBenchmarks/php-fatfree/deploy/php-fpm.pid", shell=True)
    subprocess.check_call("sudo /usr/local/nginx/sbin/nginx -c " + home + "/FrameworkBenchmarks/php-fatfree/deploy/nginx.conf", shell=True)
    
    return 0
  except subprocess.CalledProcessError:
    return 1
def stop():
  try:
    if os.name == 'nt':
      subprocess.check_call('appcmd delete site PHP', shell=True)
      return 0
    
    subprocess.call("sudo /usr/local/nginx/sbin/nginx -s stop", shell=True)
    subprocess.call("sudo kill -QUIT $( cat php-fatfree/deploy/php-fpm.pid )", shell=True)
    subprocess.check_call("sudo chown -R $USER:$USER php-fatfree", shell=True)
    
    return 0
  except subprocess.CalledProcessError:
    return 1
