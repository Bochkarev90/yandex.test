import pytest

from config import treads

pytest.main(args=[f'-n {treads}', '--html=./out_report.html'])
