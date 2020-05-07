from app import printing
import pytest
def test_index():
	assert printing() == "hello world"
