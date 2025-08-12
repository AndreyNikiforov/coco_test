# Exploring coconut lang

Main application -- using for icloudpd project:
- exhaustiveness check through types
- functional composition, functors/applicatives/monads for managing complexity

# Setting up

```shell
python3 -m pip install --disable-pip-version-check "pip>=25.1"
pip3 install --disable-pip-version-check -e . --group test --group dev
coconut --mypy install
```

# Running from source

```shell
coconut-run src/main.coco
```

# Compiling to Python

## without types

### Compile

```shell
coconut src src_py --no-wrap-types --target sys --strict --jobs sys --standalone
```

### Package python into executable

```shell
pyinstaller --onefile src_py/main.py -y
```

```shell
vscode ➜ /workspaces/coco_test (main) $ ls -la dist/main
-rwxr-xr-x 1 vscode vscode 27259592 Aug 12 22:31 dist/main
```

### Run


```shell
dist/main
```

## with types

### Compile

```shell
coconut src src_mypy --no-wrap-types --target sys --strict --jobs sys --mypy
```

Note that `--strict` for mypy does produce errors in builtins declarations

### Package with pyinstaller (for experimentation)

```shell
pyinstaller --onefile src_mypy/main.py -y
```

```shell
vscode ➜ /workspaces/coco_test (main) $ ls -la dist/main
-rwxr-xr-x 1 vscode vscode 35046952 Aug 12 22:32 dist/main
```
### Run

```shell
dist/main
```

Error:
```
Traceback (most recent call last):
  File "main.py", line 36, in <module>
  File "PyInstaller/loader/pyimod02_importers.py", line 457, in exec_module
  File "__coconut__/__init__.py", line 26, in <module>
ImportError: Importing the top-level __coconut__ package should never be done at runtime; __coconut__ exists for type checking purposes only. Try 'import coconut.__coconut__' instead.
[PYI-6816:ERROR] Failed to execute script 'main' due to unhandled exception!
```
