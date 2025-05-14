#python3 -m unittest discover -v -s tests
#!/bin/bash
#PYTHONPATH=src python3 -m unittest discover tests
#PYTHONPATH=src python3 -m unittest -v tests/test_block_handlers.py
PYTHONPATH=src python3 -m unittest tests/test_html_handlers.py
#python3 -m unittest -v tests/test_block_handlers.py