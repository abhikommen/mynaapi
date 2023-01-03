echo "Running.." 

killall gunicorn
sudo systemctl stop nginx
sudo systemctl restart nginx