#!/bin/bash

set -e  # Exit on any error
echo "Starting deployment..."
cd ~/cloud_lab_1
echo "Pulling latest code from GitHub..."
git pull origin main
echo "Activating virtual environment..."
source venv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt --quiet
echo "Restarting application service..."
sudo systemctl restart myapp
echo "Checking service status..."
sudo systemctl is-active --quiet myapp && echo "Service is running" || echo "Service failed to start"
sudo journalctl -u myapp -n 10 --no-pager
echo "Deployment completed successfully!"