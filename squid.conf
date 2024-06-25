# Dockerfile to set up Squid with a custom configuration
FROM sameersbn/squid:latest

COPY squid.conf /etc/squid/squid.conf

# squid.conf file content
http_port 3128
visible_hostname squid-proxy
acl localnet src 172.18.0.0/16
http_access allow localnet
