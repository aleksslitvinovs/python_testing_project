# Quick reference

## Virtual enviornment (venv)

### Creating venv

```bash
python -m venv env
```

### Activating it

> This will prepend that directory to your `$PATH`, so that running `python` will invoke the environment’s Python interpreter and you can run installed scripts without having to use their full path.

Mac

```bash
source env/bin/activate
```

Windows

```shell
<venv>\Scripts\activate.bat
```

### Deactivating it

```bash
deactivate
```

### Installing packages

```bash
pip install pytest
```

### Saving them in `requirements.txt`

```bash
pip freeze > requirements.txt
```

### Installing dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

## Running tests

```bash
pytest 'path/to/file'
```

```bash
pytest 'path/to/tests_file.py'
```

### Running with markers

Only `marker_name` tests

```bash
pytest 'path/to/folder' -m marker_name
```

Inverse selection by adding `not marker_name`

```bash
pytest 'path/to/folder' -m "not marker_name"
```
