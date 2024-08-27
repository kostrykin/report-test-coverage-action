# *[report-test-coverage-action](https://github.com/kostrykin/report-test-coverage-action)*

[![Report test coverage example](https://github.com/kostrykin/report-test-coverage-action/actions/workflows/test.yml/badge.svg)](https://github.com/kostrykin/report-test-coverage-action/actions/workflows/test.yml)

Determines the test coverage of a Python module using [*coverage.py*](https://coverage.readthedocs.io/en/7.4.2/).
Generates a badge for the determined coverage when triggered by a `push` event.
When triggered by a `pull_request` event, the determined coverage is added as a comment to the corresponding pull request.

<img width="907" src="https://github.com/kostrykin/report-test-coverage-action/assets/6557139/75bab889-fd88-4ac1-91f9-22b6f2836783">

Example badge generated using this action:

[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/kostrykin/d152375a04f7ab9ee9b247de41245b24/raw/report-test-coverage-action.json)](https://github.com/kostrykin/report-test-coverage-action/actions/workflows/test.yml)

---

**Steps required to set this action up for a repository:**

1. The workflow should be triggered by `push` and `pull_request` events. For `push` events, make sure that the workflow is only triggered on the main branch, or whichever branch you want to be associated with the value reported by the generated badge:
   ```yml
   on:
     pull_request:
     push:
       branches: ['master']
   ```
2. Make sure the workflow job has the following permissions:
   ```yml
   permissions:
     issues: write
     pull-requests: write
   ```
3. Create a Gist which will be used to store the values for the badge. To do that, simply create an empty Gist. You will need the ID of the Gist. If `https://gist.github.com/kostrykin/d152375a04f7ab9ee9b247de41245b24` is the URL of your Gist, then `d152375a04f7ab9ee9b247de41245b24` is the ID.
4. Create a PAT with Gist permission, and add it as your `GIST_SECRET` by going to your repository **Settings > Secrets and variables > Actions > New repository secret**.
5. Add the action to the workflow and replace `d152375a04f7ab9ee9b247de41245b24` by your Gist ID:
   ```yml
   - uses: kostrykin/report-test-coverage-action@v1.0.1
     with:
       gist-id: d152375a04f7ab9ee9b247de41245b24
       github-auth: ${{ secrets.GITHUB_TOKEN }}
       gist-auth: ${{ secrets.GIST_SECRET }}
   ```
   When embedded into a matrix strategy (e.g., for testing multiple Python versions), the reporting should be restricted to a single step. This can be achieved, for example, by adding:
   ```yml
       report: ${{ strategy.job-index == 0 }}
   ```
   You can also specify a `working-directory` as a relative path to the root of the repository (e.g., `./example`) if your Python module and the corresponding `tests` directory are not direct descendents of the repository root.

For a full example, see the workflow file *.github/workflows/example.yml* and the *example/* directory.

**List of further examples:**
- https://github.com/BMCV/giatools
- https://github.com/BMCV/segmetrics
- https://github.com/kosmotive/cs2pb
- https://github.com/kostrykin/repype
- https://github.com/kostrykin/pypers
- https://github.com/kostrykin/tournaments
