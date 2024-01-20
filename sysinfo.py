import sys

from flask import Flask, url_for

from app import create_app, basedir, APPNAME

print('START sysinfo')

app = create_app()
    
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
