test:
	nosetests

pep8:
	pep8 moat tests

autopep8:
	autopep8 --in-place -r moat tests

publish:
	python setup.py sdist upload