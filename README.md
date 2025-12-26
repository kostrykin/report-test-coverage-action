# *[report-test-coverage-action](https://github.com/kostrykin/report-test-coverage-action)*

[![Report test coverage example](https://github.com/kostrykin/report-test-coverage-action/actions/workflows/test.yml/badge.svg)](https://github.com/kostrykin/report-test-coverage-action/actions/workflows/test.yml)

Determines the test coverage of a Python module using [*coverage.py*](https://coverage.readthedocs.io/en/7.4.2/).
Generates a badge for the determined coverage when triggered by a `push` event.
When triggered by a `pull_request` event, the determined coverage is added as a comment to the corresponding pull request.

<img width="909" height="282" alt="Bildschirmfoto 2025-12-24 um 16 08 51" src="https://github.com/user-attachments/assets/875d1eb0-ec97-474f-bb9a-b75bb4fe7849" />

Example badge generated using this action:

[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/kostrykin/d152375a04f7ab9ee9b247de41245b24/raw/report-test-coverage-action.json)](https://github.com/kostrykin/report-test-coverage-action/actions/workflows/test.yml)

## Installation

### Create the main `test.yml` workflow

1. The main workflow should be given an expressive name, such as:
   ```yml
   name: Report test coverage
   ```
2. The main workflow should be triggered by `push` and `pull_request` events. For `push` events, make sure that the workflow is only triggered on the main branch, or whichever branch you want to be associated with the value reported by the generated badge:
   ```yml
   on:
     pull_request:
     push:
       branches: ['master']
   ```
3. Create a Gist which will be used to store the values for the badge. To do that, simply create an empty Gist. You will need the ID of the Gist. If `https://gist.github.com/kostrykin/d152375a04f7ab9ee9b247de41245b24` is the URL of your Gist, then `d152375a04f7ab9ee9b247de41245b24` is the ID.
4. Create a PAT with Gist permission, and add it as your `GIST_SECRET` by going to your repository **Settings > Secrets and variables > Actions > New repository secret**.
5. Add the action to the workflow and replace `d152375a04f7ab9ee9b247de41245b24` by your Gist ID:
   ```yml
   - uses: kostrykin/report-test-coverage-action@v2.0.2
     with:
       gist-id: d152375a04f7ab9ee9b247de41245b24
       gist-auth: ${{ secrets.GIST_SECRET }}
   ```
   When embedded into a matrix strategy (e.g., for testing multiple Python versions), the reporting should be restricted to a single step. This can be achieved, for example, by adding:
   ```yml
       report: ${{ strategy.job-index == 0 }}
   ```
   You can also specify a `working-directory` as a relative path to the root of the repository (e.g., `./example`) if your Python module and the corresponding `tests` directory are not direct descendents of the repository root.

For a full example, see the workflow file *.github/workflows/test.yml* and the *example/* directory.

### Create the `post-comment.yml` workflow

To report the test coverage as comments in pull requests, a second workflow must be set up. This is because the main workflow runs in the context of the base branch of the pull request (which potentially is a fork repository that has no permissions to post comments into the pull request of the upstream repository). The `post-comment.yml` workflow should look as follows:
```yml
name: Post pull request comment

on:
  workflow_run:
    workflows: [Report test coverage]  # Replace this by EXACT NAME of the main workflow!
    types: [completed]

jobs:
  post_pr_comment:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:

      - uses: kostrykin/post-gh-comment-from-artifact-action@v1.0.2
        with:
          signature: '<!-- report-test-coverage-action -->'
```

## Examples

List of further examples:

- https://github.com/BMCV/giatools
- https://github.com/BMCV/segmetrics
- https://github.com/kosmotive/cs2pb
- https://github.com/kostrykin/repype
- https://github.com/kostrykin/tournaments
