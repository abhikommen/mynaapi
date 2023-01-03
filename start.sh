echo "Running.." 

killall gunicorn3
killall gunicorn
echo "Restarting Ngnix..."
sudo systemctl stop nginx
sudo systemctl restart nginx
echo "Ngnix Restarted..."
gunicorn3 --log-level debug app:app