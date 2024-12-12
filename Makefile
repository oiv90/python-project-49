make-lint:
	poetry run flake8 brain_games

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user --force-reinstall dist/*.whl
