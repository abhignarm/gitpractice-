import pathlib,sys
import pytest
cwd = pathlib.Path.cwd()
import os,pathlib
os.chdir(pathlib.Path.cwd()/'tests')
pytest.main()
