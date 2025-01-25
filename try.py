print("Hello World")

import os

# Check the current working directory
print("Before:", os.getcwd())

# Change the working directory
os.chdir("C:/Users/sekha/OneDrive/Desktop/coding")

# Verify the change
print("After:", os.getcwd())