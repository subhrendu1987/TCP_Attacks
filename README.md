# TCP Attacks
## Initialize
```
sudo docker-compose -f docker-compose-httpd.yml build
```
or
```
sudo docker compose -f docker-compose-httpd.yml build
```
## SYN Flooding
### Launch http-server-container
```
sudo docker-compose -f docker-compose-httpd.yml up -d
```
or
```
sudo docker compose -f docker-compose-httpd.yml up -d
```
### Launch flood script
```
python3 flood.py 
```
