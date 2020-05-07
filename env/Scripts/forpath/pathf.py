import pathlib, sys
import pytest
cwd = pathlib.Path.cwd()
sys.path.appeend(tr(cwd.src))
pytest.main()
