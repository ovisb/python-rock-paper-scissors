# Python Project 'python_rock_paper_scissors'

## Project
This is the *Rock Paper Scissors (Python)* project that is part of Hyperskill platform from Jetbrains Academy.

## Project description
Rock Paper Scissors CLI game application.

How to play:
- Input user name
- input the options e.g `rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire`
- Input any of the above options to start playing
- press `!exit` to quit game or `!rating` to see current score
- You get 100 points for win and 50 points for draw
- Have fun!

#### Install steps

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

#### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
