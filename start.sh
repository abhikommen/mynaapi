echo "Running.." 

killall gunicorn
echo "Restarting Ngnix..."
sudo systemctl stop nginx
sudo systemctl restart nginx
echo "Ngnix Restarted..."
nohup gunicorn app:app