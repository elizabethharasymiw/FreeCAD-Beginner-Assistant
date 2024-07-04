# Python Testing Suite

## Windows
```
# Create Windows python virtual environment folder
python -m venv testing-env
```
```
# Activate Windows python virtual environment
testing-env\Scripts\activate.bat
```
```
# Install our saved testing dependencies
pip install -r requirements.txt
```
```
# Deactivate python virtual environment
deactivate
```

## Unix
```
# Create Unix python virtual environment folder
python3 -m venv testing-env
```
```
# Activate Unix python virtual environment
source testing-env/bin/activate
```
```
# Install our saved testing dependencies
pip install -r requirements.txt
```
```
# Deactivate python virtual environment
deactivate
```

## Python virtual environment maintenance commands
```
# List current python packages in this virtual environment
pip list
```
```
# Example of installing a new python package with pip
pip install package_name
```
```
# Save the current the versions of all python packages used in this
# virtual environment. This can be used later to recreate another 
# virtual environment in the future with the same dependencies.
pip freeze > requirements.txt
```
