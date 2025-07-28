install:
	uv sync

brain-games:
	uv run brain-games

build: clean
	uv build

package-install:
	uv tool install --force .

lint:
	uv run ruff check brain_games

clean:
	rm -rf dist/

