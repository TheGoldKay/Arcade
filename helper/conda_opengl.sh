#!/bin/bash

echo "Installing OpenGL dependencies for Python Arcade..."


# Install OpenGL and related libraries
conda install -c conda-forge pyopengl

# Install additional dependencies if needed
conda install -c conda-forge freeglut
conda install -c conda-forge libstdcxx-ng