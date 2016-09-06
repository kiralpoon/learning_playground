PDB
===============

commands
---------------

- list (list the code)
- s (steps through)
- p <variable> (print the curr value of a variable)
- n (move through code, without going into the function)
- break (view current break point)
- break <number> (create a break point)
- c (continues until reaching an enable break point)
- disable (disable a breakpoint)
- enable (enable a breakpoint)
- clear (delete a breakpoint)
- tbreak (create a temperary break point)

usage
----------------


break 2 # breakpoint created for line 2

break 2, k < 0 # breakpoint created if k < 0

