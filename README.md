[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Documentation and SOP
The SOP is currently being migrated to Sphinx documentation. The
documentation can be found at
``MagnetometryGui/docs/build/html/index.html``.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](gpl-3.0.txt) file for details.

The following assume that a compiler like MSVC or GCC is installed.
To compile the cython component run in your python environment:

```
python setup.py build_ext --inplace       
```
To pack an executable, run
```
pyinstaller ./main_window.spec
```


## AI Disclaimer
This project uses AI-assisted development.
Some code, documentation, and/or other content may have been generated or assisted by AI.
To check the grammar within documentation, tools like free version of ChatGPT and paid version of Grammerly has been used. 
Furthermore, the development was assisted using the free version of ChatGPT.
All AI-generated contributions are reviewed and tested by the project maintainer, but users should independently verify the code before using it.