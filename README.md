# dash-executable
Simple dash app converted to an executable with pyinstaller

## Create the environment

In the top-level directory, run:

```{bash}
python3 -m venv venv
```

```{bash}
pip3 install -r requirements.txt
```

```{bash}
source venv/bin/activate
```

## Running the app
```{bash}
python app.py
```

## Building the executable
```{bash}
pyinstaller app.spec
```