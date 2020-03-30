# Ken's Python Notes				[Python Resources](Python_Resources.md)

[TOC]

## Setup & Configuration

### Location of files

`C:\Users\kbsiz\Documents\Python`

### How to change or update the Anaconda/Jupyter start up folder

1. Enter `anaconda prompt` into Windows search/launch field

2. Launch `Anaconda Prompt` 

3. Enter `jupyter notebook --generate-config`

   System should respond with

   `Writing default config to: C:\Users\kbsiz\.jupyter\jupyter_notebook_config.py`

4. Edit this file using Notepad++, etc.

5. Search for this section:

  ```python
  ## The directory to use for notebooks and kernels.
  #c.NotebookApp.notebook_dir = u''
  ```

6. Uncomment and enter the desired path (note: Must use forward slashes or escape back slashes)

   ```python
   ## The directory to use for notebooks and kernels.
   c.NotebookApp.notebook_dir = u'C:\\Users\\kbsiz\\Documents\\Python\\Jupyter Notebooks'
   ```

   ​

7. Save config file, then restart Anaconda (see below)

For more details, see: https://stackoverflow.com/questions/35254852/how-to-change-jupyter-start-folder

### Starting and Stopping Jupyter and/or Anaconda 

#### From Anaconda Command Prompt

Start > **Anaconda Prompt**, then enter **jupyter notebook**

```
(C:\Anaconda2) C:\Users\kbsiz> jupyter notebook
```

The server will respond with

```
[I 23:22:46.924 NotebookApp] JupyterLab alpha preview extension loaded from C:\Anaconda2\lib\site-packages\jupyterlab
JupyterLab v0.27.0
Known labextensions:
[I 23:22:46.927 NotebookApp] Running the core application with no additional extensions or settings
[I 23:22:47.055 NotebookApp] Serving notebooks from local directory: C:\Users\kbsiz\Documents\Python\Jupyter Notebooks
[I 23:22:47.055 NotebookApp] 0 active kernels
[I 23:22:47.056 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/?token=9d1d622ecfe8da2e2a98aa2f2267ce98b359303e9a3d7d1a
[I 23:22:47.056 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 23:22:47.063 NotebookApp]
```

*Note customized local directory*

As stated in console messages, simple use `CTRL-C` to shutdown the server.

#### From Anaconda Navigator

Start > **Anaconda Navigator**, then click the Jupyter Notebook's **Launch** button

To shut down, select the "Quit" option for running notebooks when exiting  **Anaconda Navigator**

### How to add Python3  to existing Python2 Anaconda Environment

Open an Anaconda prompt using `Anaconda Prompt`, a shortcut which maps to:

`%windir%\System32\cmd.exe "/K" C:\Anaconda2\Scripts\activate.bat C:\Anaconda2`

Enter the following **conda** command to add python 3.6 (the latest stable version for Anaconda3 and Miniconda3 as of 2018-01-18)

```
> conda create -n py36 python=3.6 ipykernel
```

When prompted to proceed, type `y`

While downloading, you should see a status display like this:

```
vs2015_runtime 100% |###############################| Time: 0:01:15  27.72 kB/s
vc-14-h0510ff6 100% |###############################| Time: 0:00:00  33.56 kB/s
python-3.6.4-h  26% |########                       | Time: 0:02:51  35.00 kB/s
```

Once the environment is created, activate and register it 

```
> activate py36                                        # activate new environment
(py36) C:\Users\kbsiz> python -V                       # verify we have expected version
Python 3.6.4 :: Anaconda, Inc.
(py36) C:\Users\kbsiz> ipython3 kernel install         # register the python 3 kernel with ipython (Jupyter)
```

(note change in prompt when new environment activated)

Finally, restart your local Jupyter server. 

Should now have the option of choosing **Python3** when creating new notebooks.

#### How to start over when installation fails due to network problems, etc.

```
> conda remove --name py36 --all
Remove all packages in environment C:\Anaconda2\envs\py36:
Proceed ([y]/n)? y
> conda create --name py36 python=3.6 ipykernel
```

Note: `conda` has an `update` command, but I could never get the packages and names right.  Starting over from scratch was easier.

### How to switch to Python3 environment

```
(C:\Anaconda2) C:\Users\kbsiz> python -V
Python 2.7.14 :: Anaconda, Inc.                                        # Initially, Anaconda prompt is set for Python2

(C:\Anaconda2) C:\Users\kbsiz> activate py36                           # switch to Python3

(py36) C:\Users\kbsiz> python -V
Python 3.6.4 :: Anaconda, Inc.                                         # verify environment
```

### Adding Scientific Computing Packages to Python3 Environment

```
(C:\Anaconda2) C:\Users\kbsiz>activate py36                            # switch to Python3
(py36) C:\Users\kbsiz> conda install numpy scipy sympy matplotlib      # use conda to install packages
```



## Working with Jupyter Notebooks

### Making Plots Inline and Setting Their Size

```python
# use built-in line magic to make plots appear in the notebook
%matplotlib inline

# set default plot size (in inches)
matplotlib.rcParams['figure.figsize'] = [11.0, 8.5]
```



## Python Coding Style and Conventions

Typing `import this` at the command line gives a summary of Python principles. Less well known is that the source code for `import this` is decidedly, and by design, **unpythonic**! Take a look at it for an example of what not to do.



## Popular Python Packages

### Scientific Computing

`$ conda install ipython ipython-notebook spyder numpy scipy sympy matplotlib cython`

| Package          | Description                              |
| ---------------- | ---------------------------------------- |
| ipython          | Interactive Python interpreter and console; kernel for Jupyter |
| ipython-notebook | browser-based notebook environment (now known as Jupyter) |
| spyder           | Python IDE                               |
| numpy            | Fundamental array and numeric computing package; base of the SciPy stack; supports N-dimensional array objects, linear algebra, Fourier transforms, etc. |
| scipy            | Core package for scientific computing (SciPy is also used to refer to the entire scientific computing stack which consists of the NumPy, SciPy, Matplotlib, Sympy, Pandas packages) |
| sympy            | Symbolic mathematics package             |
| matplotlib       | Comprehensive 2D plotting package        |
| cython           | Optimising static compiler facilitates writing C extensions for Python, bidirectional calling between C/C++ and Python code;  the Cython language is a superset of the Python language that additionally supports calling C functions and declaring *C types. |

See also: [Python Packages for Researchers](http://python-for-researchers.readthedocs.io/en/latest/packages.html)

### Data Science and Analytics

| Package                                  | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [Pandas](http://pandas.pydata.org/)      | Pandas is a library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and [time series](https://en.wikipedia.org/wiki/Time_series). Pandas is [free software](https://en.wikipedia.org/wiki/Free_software) released under the three-clause BSD license |
| [Statsmodels](http://statsmodels.sourceforge.net/) | Statsmodels is a Python module that allows users to explore data, estimate statistical models, and perform statistical tests. An extensive list of descriptive statistics, statistical tests, plotting functions, and result statistics are available for different types of data and each estimator. |
| [scikit-learn](http://scikit-learn.org/stable/) | scikit-learn is an open source library for the Python. It features various classification, regression and clustering algorithms including support vector machines, logistic regression, naive Bayes, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. |
| [Mlpy](http://mlpy.sourceforge.net/)     | Mlpy is a Python machine learning library built on top of NumPy/SciPy, the GNU Scientific Library. mlpy provides a wide range of  machine learning methods for supervised and unsupervised problem.mlpy is multi platform, it works with Python 2 and 3. |
| [NumPy](http://www.numpy.org/)           | NumPy is an open source extension module for Python. The module NumPy provides fast precompiled functions for numerical routines. It adds support to Python for large, multi-dimensional arrays and matrices. Besides that it supplies a large library of high-level mathematical functions to operate on these arrays |
| [SciPy](http://www.scipy.org/)           | SciPy is widely used in scientific and technical computing. SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering. |
| [matplotlib](http://matplotlib.org/)     | matplotlib is a plotting library for NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like wxPython, Qt, or GTK+. |
| [NLTK](http://www.nltk.org/)             | The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs statistical natural language processing (NLP) for the Python. NLTK includes graphical demonstrations and sample data.NLTK has been used successfully as a platform for prototyping and building research systems. |
| [Theano](http://deeplearning.net/software/theano/) | Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently |

### Testing

| Package                                  | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) | The [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest) unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework. |
| [doctest](https://docs.python.org/3/library/doctest.html#module-doctest) | The [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest) module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. |
| [Nose](https://nose.readthedocs.org/en/latest/), [py.test](http://pytest.org/) | Third-party `unittest` frameworks with a lighter-weight syntax for writing tests. |

### [Other Useful Packages](https://wiki.python.org/moin/UsefulModules)

## Escape Sequences in Python String Literals

By default, [escape sequences](http://docs.python.org/reference/lexical_analysis.html) in strings are interpreted according to rules similar to those used by Standard C. The recognized escape sequences are:

```
Escape Sequence   Meaning Notes
\newline  Ignored  
\\    Backslash (\)    
\'    Single quote (')     
\"    Double quote (")     
\a    ASCII Bell (BEL)     
\b    ASCII Backspace (BS)     
\f    ASCII Formfeed (FF)  
\n    ASCII Linefeed (LF)  
\N{name}  Character named name in the Unicode database (Unicode only)  
\r    ASCII Carriage Return (CR)   
\t    ASCII Horizontal Tab (TAB)   
\uxxxx    Character with 16-bit hex value xxxx (Unicode only) 
\Uxxxxxxxx    Character with 32-bit hex value xxxxxxxx (Unicode only) 
\v    ASCII Vertical Tab (VT)  
\ooo  Character with octal value ooo
\xhh  Character with hex value hh
```

However, when an "r" or "R" prefix is present, a character following a backslash is included in the string without change, and all backslashes are left in the string. For example, the string literal `r"\n"`consists of two characters: a backslash and a lowercase "n". String quotes can be escaped with a backslash, but the backslash remains in the string; for example, `r"\""` is a valid string literal consisting of two characters: a backslash and a double quote; `r"\"` is not a valid string literal (even a raw string cannot end in an odd number of backslashes). Specifically, a raw string cannot end in a single backslash (since the backslash would escape the following quote character). Note also that a single backslash followed by a newline is interpreted as those two characters as part of the string, not as a line continuation.



## Python's Built-in Functions

The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.

|                                          |                                          | Built-in Functions                       |                                          |                                          |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| [`abs()`](https://docs.python.org/3/library/functions.html#abs) | [`dict()`](https://docs.python.org/3/library/functions.html#func-dict) | [`help()`](https://docs.python.org/3/library/functions.html#help) | [`min()`](https://docs.python.org/3/library/functions.html#min) | [`setattr()`](https://docs.python.org/3/library/functions.html#setattr) |
| [`all()`](https://docs.python.org/3/library/functions.html#all) | [`dir()`](https://docs.python.org/3/library/functions.html#dir) | [`hex()`](https://docs.python.org/3/library/functions.html#hex) | [`next()`](https://docs.python.org/3/library/functions.html#next) | [`slice()`](https://docs.python.org/3/library/functions.html#slice) |
| [`any()`](https://docs.python.org/3/library/functions.html#any) | [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) | [`id()`](https://docs.python.org/3/library/functions.html#id) | [`object()`](https://docs.python.org/3/library/functions.html#object) | [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) |
| [`ascii()`](https://docs.python.org/3/library/functions.html#ascii) | [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) | [`input()`](https://docs.python.org/3/library/functions.html#input) | [`oct()`](https://docs.python.org/3/library/functions.html#oct) | [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod) |
| [`bin()`](https://docs.python.org/3/library/functions.html#bin) | [`eval()`](https://docs.python.org/3/library/functions.html#eval) | [`int()`](https://docs.python.org/3/library/functions.html#int) | [`open()`](https://docs.python.org/3/library/functions.html#open) | [`str()`](https://docs.python.org/3/library/functions.html#func-str) |
| [`bool()`](https://docs.python.org/3/library/functions.html#bool) | [`exec()`](https://docs.python.org/3/library/functions.html#exec) | [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance) | [`ord()`](https://docs.python.org/3/library/functions.html#ord) | [`sum()`](https://docs.python.org/3/library/functions.html#sum) |
| [`bytearray()`](https://docs.python.org/3/library/functions.html#func-bytearray) | [`filter()`](https://docs.python.org/3/library/functions.html#filter) | [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass) | [`pow()`](https://docs.python.org/3/library/functions.html#pow) | [`super()`](https://docs.python.org/3/library/functions.html#super) |
| [`bytes()`](https://docs.python.org/3/library/functions.html#func-bytes) | [`float()`](https://docs.python.org/3/library/functions.html#float) | [`iter()`](https://docs.python.org/3/library/functions.html#iter) | [`print()`](https://docs.python.org/3/library/functions.html#print) | [`tuple()`](https://docs.python.org/3/library/functions.html#func-tuple) |
| [`callable()`](https://docs.python.org/3/library/functions.html#callable) | [`format()`](https://docs.python.org/3/library/functions.html#format) | [`len()`](https://docs.python.org/3/library/functions.html#len) | [`property()`](https://docs.python.org/3/library/functions.html#property) | [`type()`](https://docs.python.org/3/library/functions.html#type) |
| [`chr()`](https://docs.python.org/3/library/functions.html#chr) | [`frozenset()`](https://docs.python.org/3/library/functions.html#func-frozenset) | [`list()`](https://docs.python.org/3/library/functions.html#func-list) | [`range()`](https://docs.python.org/3/library/functions.html#func-range) | [`vars()`](https://docs.python.org/3/library/functions.html#vars) |
| [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod) | [`getattr()`](https://docs.python.org/3/library/functions.html#getattr) | [`locals()`](https://docs.python.org/3/library/functions.html#locals) | [`repr()`](https://docs.python.org/3/library/functions.html#repr) | [`zip()`](https://docs.python.org/3/library/functions.html#zip) |
| [`compile()`](https://docs.python.org/3/library/functions.html#compile) | [`globals()`](https://docs.python.org/3/library/functions.html#globals) | [`map()`](https://docs.python.org/3/library/functions.html#map) | [`reversed()`](https://docs.python.org/3/library/functions.html#reversed) | [`__import__()`](https://docs.python.org/3/library/functions.html#__import__) |
| [`complex()`](https://docs.python.org/3/library/functions.html#complex) | [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr) | [`max()`](https://docs.python.org/3/library/functions.html#max) | [`round()`](https://docs.python.org/3/library/functions.html#round) |                                          |
| [`delattr()`](https://docs.python.org/3/library/functions.html#delattr) | [`hash()`](https://docs.python.org/3/library/functions.html#hash) | [`memoryview()`](https://docs.python.org/3/library/functions.html#func-memoryview) | [`set()`](https://docs.python.org/3/library/functions.html#func-set) |                                          |

see: https://docs.python.org/3/library/functions.html



## Pretty Printing in Python

Method 1: Simply dump the string representation (easiest, ungliest)

```
# The standard string repr for dicts is hard to read:
>>> my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
>>> my_mapping
{'b': 42, 'c': 12648430. 'a': 23}  # 😞
```
Method 2: Using json.dumps()
```
# Using the "json" module
>>> import json
>>> print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}
# Note: this only works with dicts containing
# primitive types (check out the "pprint" module):
>>> json.dumps({all: 'yup'})
TypeError: keys must be a string

```
Method 3: The [pprint module](https://docs.python.org/3/library/pprint.html)
```
>>> import pprint
>>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
>>> stuff.insert(0, stuff[:])
>>> pp = pprint.PrettyPrinter(indent=4)
>>> pp.pprint(stuff)
[   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']
```
## SQLite Database

[Python SQLite Tutorial](https://www.youtube.com/watch?v=pd-0G0MigUA)

Example: Creating a database with one table

```python
import sqlite3

dbConn = sqlite3.connect('employee.db')
c = dbConn.cursor()
c.execute("""
	CREATE TABLE employees (
		first   TEXT,  /* are these case-sensitive? */
		last    TEXT,
		pay     INTEGER
	)
""")
dbConn.commit()   /* do you need to commit DDL?? */
dbConn.close()
```

