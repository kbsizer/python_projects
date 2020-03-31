# Python Scripting Snippets

[TOC]

## Invoking Python from the Command Line

### Explicitly invoking the Python interpreter

```bash
$ python --version
Python 3.8.2

$ python --help

$ python -c "print('Real Python')"

$ python myPythonScript.py
```

### Indirectly, via the shell

```bash
# Create a short little demo script
$ cat tst.py
import sys
print(sys.executable, sys.version)

# Attempt to run it like a shell script
$ ./tst.py
./tst.py: line 1: import: command not found
./tst.py: line 2: syntax error near unexpected token `sys.executable,'
./tst.py: line 2: `print(sys.executable, sys.version)'

# Add "shebang" as the first line of the script
$ cat tst.py
#!/usr/bin/env python
import sys
print(sys.executable, sys.version)

# Now, the shell knows what to do and we can invoke our python program like a shell script
$ ./tst.py
C:\Python38\python.exe 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)]
```



***Shebang Notes***, i.e., why put that `#!/usr/bin/env python` line at the top of every Python script?

* The "shebang" line becomes relevant when you run a script in Unix by making it executable (`chmod +x myscript.py`) and then running it directly: `./myscript.py`, (as opposed to `python myscript.py`)

* If you have several versions of Python installed, `/usr/bin/env` will ensure the interpreter used is the first one on your environment's `$PATH`. The alternative would be to hardcode something like `#!/usr/bin/python`; that's ok, but less flexible.

* In Unix, an *executable* file that's meant to be interpreted can indicate what interpreter to use by having a `#!` at the start of the first line, followed by the interpreter (and any flags it may need).

* On other platforms, this rule does not apply (but that "shebang line" does no harm, and will help if you ever copy that script to a platform *with* a Unix base, such as Linux, Mac, etc).



## Reading a Text File Line by Line Using an Iterator

```python
f = open('my_text_file.txt')
for line in f:
    print(line)
fh.close()
```

Or, with more robust resource management using `try..finally`

```python
f = open('my_text_file.txt')
try:
	for line in f:
    	print(line)     
finally:
	fh.close()
```

Note: `line` will contain the line terminator character(s) found in the source file.  To remove these, use `line.rstrip()`

## Command-line Arguments

### Using `sys` 

**Example 1: write out script name and command-line args**

Source

```python
# listargs.py

import sys

print(f"Name of the script      : {sys.argv[0]=}")    # note: {...=} is Python 3.8 syntax
print(f"Arguments of the script : {sys.argv[1:]=}")
```

Output

```b
$ python listargs.py
Name of the script      : sys.argv[0]='listargs.py'
Arguments of the script : sys.argv[1:]=[]

kesize@d10b237 MINGW64 ~
$ python listargs.py arg1 arg2 arg3
Name of the script      : sys.argv[0]='listargs.py'
Arguments of the script : sys.argv[1:]=['arg1', 'arg2', 'arg3']

```

**Example 2: reverse the first command-line arg**

Source

```python
#!/usr/bin/env python
import sys
arg = sys.argv[1]        # get first arg  (argv[0] is the script's name)
print(arg[::-1])
```

Output

```
$ reverse.py foo
oof

$ reverse.py "Help, I'm trapped in a PDP-11"
11-PDP a ni deppart m'I ,pleH
```

### Simple Option and Argument Handling

**Example: Modify the case of the Python command line arguments.** 

Three options are available:

* **`-c`** to capitalize the arguments
* **`-u`** to convert the arguments to uppercase
* **`-l`** to convert the argument to lowercase

Source

```python
#!/usr/bin/env python

import sys

# Using list comprehensions, 
# separate command-line args into options (prefixed with a hyphen) and 
# program arguments (not prefixed with a hyphen)
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-c" in opts:
    print(" ".join(arg.capitalize() for arg in args))
elif "-u" in opts:
    print(" ".join(arg.upper() for arg in args))
elif "-l" in opts:
    print(" ".join(arg.lower() for arg in args))
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")
```

Output

```
$ python cul.py -c un deux trois
Un Deux Trois
```

## String Processing in Python

### Trimming Leading or Trailing Whitespace

```python
leadingSpaceRemoved = s.lstrip()
trailingSpaceRemoved = s.rstrip()
bothRemoved = s.strip()
```

Note: Python's `strip()` methods take an optional argument; the characters to strip.  For example, to remove the CR+LF at the end of Windows files, use `s.rstrip('\r\n')`

### Replacing Occurrences of a Substring

```python
s = "geeks for geeks geeks geeks geeks" 
   
# Prints the string by replacing geeks by Geeks  
print(string.replace("geeks", "Geeks"))  
  
# Prints the string by replacing only 3 occurrence of Geeks   
print(string.replace("geeks", "GeeksforGeeks", 3)) 
```

### Replacing a Section of a String using Slices

`s = s[:position] + replacement + s[position+length_of_replaced:]`

Example:

```python
# replace 'sat' with 'slept'
text = "The cat sat on the mat"
text = text[:8] + "slept" + text[11:]
```



## Regular Expressions in Python

### Compiling Patterns and Using Them to Find Matches

Reference: https://docs.python.org/3/howto/regex.html

**Example: Basic Regex Operations**

```python
import re

p = re.compile(r'yourRegularExpression')    # note use of (r)aw strings to avoid having to escape backslashes and such
m = p.search('string we want to scan')
if m:
    print('Match found: ', m.group())
```



**Example: A simple grep clone**

```python
#!/usr/bin/env python
import re
import sys

# process command-line args
# if 2 args were not passed on the command-line, print usage and exit
if len(sys.argv) < 3:
    raise SystemExit(f"Usage: {sys.argv[0]} <regex> <fileToScan>")
regex = sys.argv[1]
fileToScan = sys.argv[2]

# build regex
regexPattern = re.compile(regex)

# process file line-by-line
f = open(fileToScan)
try:
    for line in f:
        if regexPattern.search(line):
        	print(line)
finally:
    f.close()
```

Output

```
$ simpleGrep.py 'abc.*label'  gateway.xml
          <sas_workflow_common:label>abc</sas_workflow_common:label>

    <sas_workflow_common:label>abc</sas_workflow_common:label>
```



**Note**: You can learn about this by interactively experimenting with the [`re`](https://docs.python.org/3/library/re.html#module-re) module. If you have [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter) available, you may also want to look at [Tools/demo/redemo.py](https://github.com/python/cpython/tree/3.8/Tools/demo/redemo.py), a demonstration program included with the Python distribution. It allows you to enter REs and strings, and displays whether the RE matches or fails.

### Replacing an Occurrence of a Regular Expression

The method `sub( regExPattern, repl, srcString [, count [, flags ] ] )`  returns the string obtained by replacing the leftmost non-overlapping occurrences of *regExPattern* in *srcString* by the replacement *repl*. If the pattern isn’t found, *string* is returned unchanged.

Examples:

```python
# Replace "and" with "&" (case-insensitive)
s = 'Baked Beans And Spam'
print(re.sub(r'\sAND\s', ' & ', s, flags=re.IGNORECASE))
# 'Baked Beans & Spam'

# Replace using a function to generate the replacement text
def dashrepl(matchobj):
	if matchobj.group(0) == '-': 
        return ' '
	else: 
        return '-'
s = 'pro----gram-files'
print(re.sub('-{1,2}', dashrepl, s))
# 'pro--gram files'

```

Notes:

* *repl* may be a string or a function
* *regExPattern* may be a string or a Pattern object