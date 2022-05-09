pip install pytest
pip install pytest-cov
pip install pytest-html


pytest
pytest --cov=. --cov-report=html:.html
pytest --html=report.html --self-contained-html