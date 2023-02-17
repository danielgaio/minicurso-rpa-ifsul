import sys
sys.path.append('src')
from main import run_automation


def test_run_automation():
    result = run_automation()
    assert result
