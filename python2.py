Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import keyword
dir(keyword)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'iskeyword', 'issoftkeyword', 'kwlist', 'softkwlist']
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
len(keyword.kwlist)
35
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
keyword.iskeyword('while')
True
keyword.iskeyword('man')
False

keyword.iskeyword('return')
True
keyword.iskeyword('import')
True
keyword.iskeyword('else')
True
keyword.iskeyword('int')
False
keyword.iskeyword('for')
True
keyword.iskeyword('print')
False
keyword.iskeyword('as')
True
keyword.iskeyword('add')
False
keyword.iskeyword('help')
False
help('assert')
The "assert" statement
**********************

Assert statements are a convenient way to insert debugging assertions
into a program:

   assert_stmt ::= "assert" expression ["," expression]

The simple form, "assert expression", is equivalent to

   if __debug__:
       if not expression: raise AssertionError

The extended form, "assert expression1, expression2", is equivalent to

   if __debug__:
       if not expression1: raise AssertionError(expression2)

These equivalences assume that "__debug__" and "AssertionError" refer
to the built-in variables with those names.  In the current
implementation, the built-in variable "__debug__" is "True" under
normal circumstances, "False" when optimization is requested (command
line option "-O").  The current code generator emits no code for an
assert statement when optimization is requested at compile time.  Note
that it is unnecessary to include the source code for the expression
that failed in the error message; it will be displayed as part of the
stack trace.

Assignments to "__debug__" are illegal.  The value for the built-in
variable is determined when the interpreter starts.

help('switch')
No Python documentation found for 'switch'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help('array')

help('print')
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

>>> keyword.iskeyword('print')
False
>>> keyword.iskeyword('NULL')
False
>>> help('True')

>>> help('False')

>>> help('array')

>>> keyword.iskeyword('sys')
False
>>> help('elif')
The "if" statement
******************

The "if" statement is used for conditional execution:

   if_stmt ::= "if" assignment_expression ":" suite
               ("elif" assignment_expression ":" suite)*
               ["else" ":" suite]

It selects exactly one of the suites by evaluating the expressions one
by one until one is found to be true (see section Boolean operations
for the definition of true and false); then that suite is executed
(and no other part of the "if" statement is executed or evaluated).
If all expressions are false, the suite of the "else" clause, if
present, is executed.

Related help topics: TRUTHVALUE

