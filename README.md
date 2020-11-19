# topalias

[![Build Status](https://travis-ci.com/CSRedRat/topalias.svg?branch=master)](https://travis-ci.com/CSRedRat/topalias)
[![Test Status](https://github.com/CSRedRat/topalias/workflows/Test/badge.svg?branch=master)](https://github.com/CSRedRat/topalias/actions?query=workflow%3ATest)
[![Coverage](https://coveralls.io/repos/github/CSRedRat/topalias/badge.svg?branch=master)](https://coveralls.io/github/CSRedRat/topalias?branch=master)
[![GitLab pipeline](https://gitlab.com/CSRedRat/topalias/badges/master/pipeline.svg)](https://gitlab.com/CSRedRat/topalias/-/pipelines)
[![Python Version](https://img.shields.io/pypi/pyversions/topalias.svg)](https://pypi.org/project/topalias/)
[![Downloads](https://static.pepy.tech/personalized-badge/topalias?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/topalias)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/CSRedRat/topalias/?ref=repository-badge)

[topalias](https://github.com/CSRedRat/topalias) - Linux bash/zsh alias generator and statistics from command history, written on [Python](https://pypi.org/project/topalias/).

## Features

-   Generate short alias for popular command from bash/zsh shell history
-   Command history statistics & analytics
-   Parametrised input
-   Console help for all commands, options and arguments
-   Shell workflow hints

## Installation

From [pypi.org repository](https://pypi.org/project/topalias/):

```bash
pip3 install -U --user topalias
```

From source:

```bash
git clone https://github.com/CSRedRat/topalias
python3 topalias/setup.py install --user
```

Run as python script without install:

```bash
git clone https://github.com/CSRedRat/topalias
python3 topalias/topalias/cli.py -h
```

### Install requirements

```bash
sudo apt install python3 python3-pip -y
```

Add PATH environment variable for run Python tools as Linux utility:

```bash
echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc
source ~/.bashrc
```

## Usage

![generated bash aliases](https://github.com/CSRedRat/topalias/raw/master/images/bash_screenshot.png "Bash topalias output")

Syntax: `topalias [OPTIONS] COMMAND [ARGUMENTS]`

Without command utility check if you use alias in ~/.bash_aliases - analyze and print usage statistics, offers to find new simple aliases

```bash
python3 -m topalias  # run as python module
topalias  # check aliases and print suggestion bash command history
topalias -h  # print help
topalias --zsh  # work with zsh shell command history
topalias --min=2  # set minimal length for generated acronym filter, so that exclude some short command and find long, hard, usable command
topalias --debug history  # only analyze local bash history and print filtered rows
```

Files path search order:

-   directory from execution parameter
-   .bash_history in . current directory
-   .bash_history in ~ user home directory
-   example development files in topalias/data

You can change dot files search path to another user home directory:

```bash
topalias -f /home/user  # or topalias --path /home/user
```

Also you can use topalias utility in [Bash for Git](https://gitforwindows.org/) on Windows and in [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux).

## TODO

-   multiline command in history
-   add any another acronym algorithm with semantic
-   more statistics & analytics (used dir, utils, parameters, time)
-   alias max length parameter

Please add you feature requests: [https://github.com/CSRedRat/topalias/issues/new](https://github.com/CSRedRat/topalias/issues/new)

## License

[GPLv3](https://github.com/CSRedRat/topalias/blob/master/LICENSE)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://metin2wiki.ru/"><img src="https://avatars1.githubusercontent.com/u/1287586?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sergey Chudakov</b></sub></a><br /><a href="https://github.com/CSRedRat/topalias/commits?author=CSRedRat" title="Code">💻</a> <a href="#infra-CSRedRat" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#ideas-CSRedRat" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-CSRedRat" title="Maintenance">🚧</a> <a href="#platform-CSRedRat" title="Packaging/porting to new platform">📦</a> <a href="#mentoring-CSRedRat" title="Mentoring">🧑‍🏫</a> <a href="#example-CSRedRat" title="Examples">💡</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

_GitLab repository mirror with CI/CD: [https://gitlab.com/CSRedRat/topalias](https://gitlab.com/CSRedRat/topalias)_

_GitHub Pages: [https://csredrat.github.io/topalias/](https://csredrat.github.io/topalias/)_
