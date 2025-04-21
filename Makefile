help:
clean:
	rm -rf dist target coverage
run:
	poetry run terminalizer2asciinema test-data.yml
build:
	scripts/set-version.sh
	poetry build
install:
	poetry install
flake8:
	poetry run flake8
update:
	poetry update
test:
	 poetry run pytest --junit-xml=coverage/test-results.xml \
	 --cov=terminalizer2asciinema \
	 --cov-report term-missing  \
	 --cov-report xml:coverage/coverage.xml \
	 --cov-report html:coverage/coverage.html \
	 --cov-report lcov:coverage/coverage.info

all: clean install flake8 build test

release:
	scripts/release.sh

commit:
	scripts/git-commit.sh
