# Better python depedencies management using poetry
For many year pip is the only package manager to maintain python depedencies. In this blog I will show you one of alternative package depedencies poetry.


Before continue this blog, I assume you guys know how to manage python package using pip. If you don't know how to manage python package using pip you can see my previous blog make maintainable python project TODO link blog.


## Maintain Python Project using poetry
### Install poetry
make sure you have python installed then follow one of these installation instruction:
[https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

### Create Project
poetry have command to initiate project `poetry new` and `poetry init`

- `poetry new` Scafolding project. Suitable for create new python project from scratch.
- `poetry init` Only generate pyproject.toml. Suitable for existing python project.


### Adding depedencies
- Adding depedencies using `poetry add [package name]`
What makes diffrent from pip it use pyproject.toml to note it's depedencies. Other than pyproject.toml there is poetry.lock. poetry.lock to lock package version (make it repeatable), cache repository and stored package depedencies.

- To reinstall all depedencies `poetry install`.

- You can also grouping depedencies using --group flag `poetry add [package name] --group [group name]`
by grouping specific depedencies we can install only specific package

- to install specific group you can use:
    - `poetry install --only [group name]`
    - `poetry install --without [group name]`
    - `poetry install --only-root`

more feature see [https://python-poetry.org/docs/managing-dependencies/](https://python-poetry.org/docs/managing-dependencies/)


## More about poetry
### No dangling depedencies
When using packages some packages have package depedencies. For example pandas depedends numpy. If you install pandas you also install numpy. 
When perform `pip install pandas` pip will install both pandas and numpy. But when perform `pip uninstall pandas` pip will only uninstall pandas.
which is anoying I am not used numpy but it still on my python environtment make depedencies bloat. But if you use poetry `poetry remove pandas` it will
remove both pandas and numpy.

### Easier Creating python library
Maybe you try to create python library. In order to create python library you must follow project structure standard (https://packaging.python.org/en/latest/tutorials/packaging-projects/). Poetry scafolding follow this project structure standard. Poetry also have command to publish to pypi (https://python-poetry.org/docs/libraries/)

### I need poetry feature but my service provider doesn't support poetry
When you deploy python project to some service doesn't have support for poetry only pip. But i still need poetry feature. The solution just convert pyproject.toml to requiremnents.txt.
you can convert your poetry pyproject.toml to requirements.txt using this command `poetry export --without-hashes --format=requirements.txt > requirements.txt`

## Should I move from pip to poetry
As most of answer in software development. It depends. If you need poetry feature like depedencies group, scafolding, Easier creating python package, etc
you should move to poetry. If you don't need poetry feature, stick with pip it's ok (as long you follow best practice).
