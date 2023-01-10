echo "Running.." 

killall gunicorn
echo "Restarting Ngnix..."
sudo systemctl stop nginx
sudo systemctl restart nginx
echo "Ngnix Restarted..."
gunicorn -w 4 app:app >/dev/null &