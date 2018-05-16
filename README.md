# py3gci
A simple example python3 web server with CGI

### Usage

```
 python server.py
```

This will serve at [http://localhost:8000/](http://localhost:8000/).

To stop serving, simply type `Ctrl+c` in the terminal. The webserver will keep running if you don't explicitly kill it.

#### Troubleshooting Common Issues

* Make sure that the shebang at the top of `parseForm.py` contains the path to your installation of python3.
i.e., replace the line `#!/usr/local/bin/python3` with `#!<this_is_where_my_python_lives`. If you don't know the path, issuing `which python` to find out. If you get a 501, this is likely the solution.

* If you see a message like the following, you are probably using python2 instead of python3:

```
$ python server.py
Traceback (most recent call last):
  File "server.py", line 3, in <module>
    import http.server
ImportError: No module named http.server
```

* If there is a port conflict, you can change the default port from 8000 to another port by simply changing the `PORT` variable in the script.
