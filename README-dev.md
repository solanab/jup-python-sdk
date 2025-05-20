## **Local Development**
If you want to make changes to the SDK and test it locally:

1. In this project's directory, install the package in editable mode by running:
   ```sh
   pip install -e .
   ```

2. To use this library in another project while making changes to it, install the package from its local path in that project:
   ```sh
   pip install -e /path/to/jup-python-sdk
   ```

   Replace `/path/to/jup-python-sdk` with the absolute or relative path to this project directory.

By installing in editable mode, any changes you make to the SDK will immediately reflect in your tests without needing to reinstall the package.
