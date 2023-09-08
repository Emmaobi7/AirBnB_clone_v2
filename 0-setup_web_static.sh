#!/usr/bin/env bash
# sets up server for deployment of static files

#install nginx
sudo apt update
sudo apt install -y nginx

#folders and test folder
folder="/data/web_static/"
mkdir -p "$folder"
mkdir -p "$folder/releases/test/"
mkdir -p "$folder/shared"

echo "my test config" > "$folder/releases/test/index.html"

symlink="$folder/current"
if [ -L "$symlink" ]; then
	rm "$symlink"
fi

ln -s "$folder/releases/test/" "$symlink"


sudo chown -R ubuntu:ubuntu /data/

server_config="
server {
        listen 80;
        listen [::]:80 default_server;

        add_header X-Served-By $HOSTNAME;

        root /var/www/html;
        index index.nginx-debian.html;

	location /hbnb_static {
		alias /data/web_static/current/;
	}

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        error_page 404 /c404.html;
        location =/c404.html {
                root /usr/share/nginx/html;
                internal;
        }
}"

echo "$server_config" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
