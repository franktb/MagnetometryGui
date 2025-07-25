[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](gpl-3.0.txt) file for details.

The following assume that a compiler like MSVC or GCC is installed.
To compile the cython component run in your python environment:

```
python setup.py build_ext --inplace       
```
To pack an executable, run first
```
pyi-makespec main_window.py --onefile
```
and thereafter
```
pyinstaller ./main_window.spec
```