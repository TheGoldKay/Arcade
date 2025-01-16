#!/bin/bash

echo "Installing OpenGL dependencies for Python 3"
echo "CHECK IF NALA IS INSTALLED"

sudo nala install python3-opengl
sudo nala install python3-dev
sudo nala install libgl1-mesa-glx 
sudo nala install libgl1-mesa-dri