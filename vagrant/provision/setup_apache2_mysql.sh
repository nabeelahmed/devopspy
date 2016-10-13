#!/bin/bash

echo "Provisioning virtual machine..."

echo "Updating ...."
apt-get update > /dev/null

echo "Installing Git"
apt-get install git -y > /dev/null

echo "Installing Apache2 ..." 
apt-get install -y apache2 > /dev/null

echo "Installing Nginx"
apt-get install nginx -y > /dev/null
	
echo "Preparing MySQL installation ..."
apt-get install debconf-utils -y > /dev/null
debconf-set-selections <<< "mysql-server mysql-server/root_password password 1234"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password 1234"

echo "Installing MySQL ..." 
apt-get install mysql-server -y > /dev/null


