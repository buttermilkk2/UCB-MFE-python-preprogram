# Lecture 5: Productionization I

## Goal
- Be very good at debugging Python code
- Understand different varieties of testing


## Setup
- `conda create -n lecture_5 python=3.10 -y`
- `conda activate lecture_5`

## Debugging

- Why bother debugging? 
- You need to debug when:
	- you see a Shape ratio of 40
	- you are trying to understand your teammate's code
- How many of you debug via:
	- `print(...)`
	- Binary search
	- `pdb`/`ipdb` (or `breakpoint`) (need to install `ipdb`)
        - `breakpoint` will default use `pdb`, if you want to use `ipdb` need to `export PYTHONBREAKPOINT=ipdb.set_trace`
- Examples 
	- debug in `ipdb` (make sure you `pip install ipdb`)
	- debug in `jupyter notebook` (use the magic command `%debug` after you see an error)
- reference: 
    - https://wangchuan.github.io/coding/2017/07/12/ipdb-cheat-sheet.html

## Testing

- Why bother testings?
- Different types of tests
	- lint checks
	- [unit test](https://en.wikipedia.org/wiki/Unit_testing)
	- [integration test](https://en.wikipedia.org/wiki/Integration_testing)
	- [regression test](https://en.wikipedia.org/wiki/Regression_testing)

## Lint check
- code quality matters
    - It does what it is supposed to do
    - It does not contain defects or problems
    - It is easy to read, maintain, and extend
- [PEP8](https://pep8.org/)
    - indentation
    - tabs vs. spaces
    - max line length
    - imports
    - `"` vs `'`
    - white spaces
    - ...
- Linters
    - Logical Lint
        - Code errors
        - Code with potentially unintended results
        - Dangerous code patterns
    - Stylistic Lint
        - Code not conforming to defined conventions
    - Commonly used linters
        - [`flake8`](https://flake8.pycqa.org/en/latest/)
            - logical & stylistic lint
            - `pip install flake8`
            - `flake8 path/to/code/to/check.py` or `flake8 path/to/code/`
            - note that flake8 cannot identify spacing issues
        - [`black`](https://github.com/psf/black)
            - stylistic lint
            - `pip install black`
            - `black` can be applied to a folder or file
            - try it on `code/lint/black.py`
            - note that black cannot identify undefined variable
        - [`isort`](https://github.com/PyCQA/isort)
            - stylistic lint
            - `pip install isort`
            - try `isort lint/isort.py`
            - note that isort cannot identify undefined modules neither
        - [`mypy`](http://mypy-lang.org/)
            - logical & stylistic lint
            - [type hinting](https://realpython.com/lessons/type-hinting/) 
            - `pip install mypy`
            - more examples
                - http://mypy-lang.org/examples.html
                - https://mypy.readthedocs.io/en/stable/getting_started.html
    - we usually use all of them ;)
- reference:
    - https://realpython.com/python-code-quality/
    - https://siderlabs.com/blog/about-style-guide-of-python-and-linter-tool-pep8-pyflakes-flake8-haking-pyling-7fdbe163079d/


## Unit test
- Why unit tests are important?
    - I didn't write any unit test until...
    - It's super unlikely that you wrote 100% of the code snippet in a collaborative environment (and in fact, when I am writing this session, the model hasn't been built) 
    - Even it's your code, you are unlikely to remember what you wrote 3 months ago.
    - It gives you confidence to change stuff
    - It finds bug faster
    - It serves great documentation (code are alive, comments are not)
    - Rule of composition: a chain of unit tested functions = unit-tested software
- What to unit test?
    - Rule 1: unit test should just test the function itself, not the functions that function calls 
    - Rule 2: isolate & control everything else (I/O, random seed, timestamp, output of other functions)
    - Rule 3: be innovative, test for edge cases
- When **NOT** to unit test?
    - Not all codes are created equal
    - "private" functions that's wrapped by other "public" function (yes, sometimes you can be lazy)
    - Functions in the notebook (aka those not going to the production)
- [live demo] intro to unit test
    - `pip install pytest` and `pip install unittest`
    - [what's the difference?](https://www.pythonpool.com/python-unittest-vs-pytest/)
        - we usually mix them up as long as it gets things done
    - most useful concepts
        - basic tests
        - parametrize
            - avoid repetition
        - expect failure
            - failure can also be verified
        - mock
            - assume the behavior of downstream/slow/IO logic
        - [fixture](https://docs.pytest.org/en/6.2.x/fixture.html#what-fixtures-are)
            - to prepare something to be shared (e.g. dataset, models)

## Integration test and Regression test
- Integration test
    - data cleansing pipeline
    - model training pipeline
    - model serving
    - ...
- Regression test
    - latency & responding time
    - backtest (?)
    - ...
- reference:
    - https://www.kdnuggets.com/2019/11/testing-machine-learning-pipelines.html


## makefile
- Make your life easier
- `make lint` instead of running `flake8` +  `mypy` + ...
- `make install` <- who doesn't like 1-click setup?
- checkout `Makefile`
- Note: indentation needs to be `Tab`. It cannot be `Spaces`

# ==== if time allows ===

## Development Environment
- **Local/Development**: your laptop or a sandbox on a development server 
- **Testing**: for all the tests, shares the same environement as `staging` and `production`
- **Staging**: an environment for final testing immediately prior to deploying to production. A mirror of `production`, but not facing to the users.
- **Production**: the environment that users/clients directly interact with
- [some white board illustration here]

## What does productionization mean?
- when your customers are going to meet your code
- [white-boarding] illustrate how customers interact with your code (while you are sleeping) 
  - example: what happens when you type www.google.com (while google engineers enjoy Saturday vacation)
    - find the ip of www.google.com -> xxx.xx.xx.xx
    - establish a TCP connection with that ip 
    - send http or https request via the connection
    - wait for response (error code + content)
  - How do we bring our model to the customers?

