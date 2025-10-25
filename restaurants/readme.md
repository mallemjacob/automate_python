# Create a folder 
mkdir restaurants

# Change into the directory
cd restaurants

# Create virtual environment
Linux: python3 -m venv .venv
Windows: python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Create requirments.txt
touch requirments.txt

# Add requests to requirments.txt file
echo "requests" > requirments.txt

# Run requirments.txt
pip install -r requirments.txt

# create a new python file app.py
touch app.py

# Use these apis
https://dummyjson.com/recipes
or
https://fakerestaurantapi.runasp.net/api/Restaurant


# Create objects from Restaurant class with json data
From line 13 in app.py file, write the logic to create objects from Restaurant class.

# run a python file
Linux: python3 app.py
Windows: python app.py

# deactivate virtual environment
deactivate