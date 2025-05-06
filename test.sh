#python3 -m unittest discover -v -s tests
#!/bin/bash
PYTHONPATH=src python3 -m unittest discover tests
#python3 -m unittest -v tests/test_block_handlers.py