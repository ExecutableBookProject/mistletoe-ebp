(contribute)=

# Contributing

[![CI Status][travis-badge]][travis-link]
[![Coverage][coveralls-badge]][coveralls-link]
[![Code style: black][black-badge]][black-link]
[![Documentation Status][rtd-badge]][rtd-link]

## Code Style

Code style is tested using [flake8](http://flake8.pycqa.org),
with the configuration set in `.flake8`,
and code formatted with [black](https://github.com/ambv/black).

Installing with `mistletoe-ebp[code_style]` makes the [pre-commit](https://pre-commit.com/)
package available, which will ensure this style is met before commits are submitted, by reformatting the code
and testing for lint errors.
It can be setup by:

```shell
>> cd mistletoe-ebp
>> pre-commit install
```

Optionally you can run `black` and `flake8` separately:

```shell
>> black .
>> flake8 .
```

Editors like VS Code also have automatic code reformat utilities, which can adhere to this standard.

All functions and class methods should be annotated with types and include a docstring. The prefered docstring format is outlined in `mistletoe-ebp/docstring.fmt.mustache` and can be used automatically with the
[autodocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) VS Code extension.

## Testing

For code tests:

```shell
>> cd mistletoe-ebp
>> pytest
```

For documentation build tests:

```shell
>> cd mistletoe-ebp/docs
>> make clean
>> make html-strict
```

## Pull Requests

To contribute, make Pull Requests to the `master` branch (this is the default branch). A PR can consist of one or multiple commits. Before you open a PR, make sure to clean up your commit history and create the commits that you think best divide up the total work as outlined above (use `git rebase` and `git commit --amend`). Ensure all commit messages clearly summarise the changes in the header and the problem that this commit is solving in the body.

Merging pull requests: There are three ways of 'merging' pull requests on GitHub:

- Squash and merge: take all commits, squash them into a single one and put it on top of the base branch.
    Choose this for pull requests that address a single issue and are well represented by a single commit.
    Make sure to clean the commit message (title & body)
- Rebase and merge: take all commits and 'recreate' them on top of the base branch. All commits will be recreated with new hashes.
    Choose this for pull requests that require more than a single commit.
    Examples: PRs that contain multiple commits with individually significant changes; PRs that have commits from different authors (squashing commits would remove attribution)
- Merge with merge commit: put all commits as they are on the base branch, with a merge commit on top
    Choose for collaborative PRs with many commits. Here, the merge commit provides actual benefits.

[travis-badge]: https://travis-ci.org/ExecutableBookProject/mistletoe-ebp.svg?branch=master
[travis-link]: https://travis-ci.org/ExecutableBookProject/mistletoe-ebp
[coveralls-badge]: https://coveralls.io/repos/github/ExecutableBookProject/mistletoe-ebp/badge.svg?branch=master
[coveralls-link]: https://coveralls.io/github/ExecutableBookProject/mistletoe-ebp?branch=master
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
[rtd-badge]: https://readthedocs.org/projects/mistletoe-ebp/badge/?version=latest
[rtd-link]: https://mistletoe-ebp.readthedocs.io/en/latest/?badge=latest
