#!/bin/bash

# Make sure the script is being run with superuser privileges.
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Update package lists
echo "Updating package lists..."
apt-get update

# Install necessary packages
echo "Installing necessary packages..."
apt-get install -y docker docker-compose git

# Clone the project repository
echo "Cloning project repository..."
git clone https://github.com/JRCuster/Setup_of_HomeLab.git
cd Setup_of_HomeLab

# Run the existing setup script
echo "Running the existing setup script..."
chmod +x setup.sh
./setup.sh

# Output the status
echo "Setup process initialized successfully."
