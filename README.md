# ghactions
learning about github actions

## Workflows
Each workflow consists of one or more jobs, and each job consists of one or more steps.

- CI: run tests, build & push image
  - [Test](<.github/workflows/01-python-app.yml>)
  - [Build & Push](<.github/workflows/02-build_push_sdai-sbox-gh-actions-app001.yml>)
- CD: deploy, using correct trigger.
  - [Deploy](<.github/workflows/03-deploy_sdai-sbox-gh-actions-app001.yml>)
- Different triggers (Documentation)
  - [Triggering a workflow](<https://docs.github.com/en/actions/using-workflows/triggering-a-workflow>)
  - [Events that trigger workflows](<https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows>)
  - [Workflow Syntax](<https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on>)

## Links
- [Building and testing Python](<https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python>)
- [Workflow syntax for GitHub Actions](<https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategy>)  
- You can cache and restore the dependencies using the [setup-python action](<https://github.com/actions/setup-python>).  
- [Starter workflow for python-app](<https://github.com/actions/starter-workflows/blob/main/ci/python-app.yml>)
- [upload-artifact](<https://github.com/actions/upload-artifact>)
- To use a pre-installed version of Python or PyPy on a GitHub-hosted runner, use the [setup-python action](<https://github.com/actions/setup-python>).
- External reading and explanation [link](<https://www.learnenough.com/blog/git-actions-tutorial>) 

## Testing
Running tests in GitHub Actions

```yml
- name: Test with pytest
      run: |
        python -m pytest # <--
```