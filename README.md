# ghactions
Learn GitHub Actions

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
  - [Schedule (cron)](<https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule>)

## ACR
- [__Image tag best practices__](<https://learn.microsoft.com/en-us/azure/container-registry/container-registry-image-tag-version>)
- [__Retention policy for unused images__](<https://learn.microsoft.com/en-us/azure/container-registry/container-registry-retention-policy>)
  - Command group 'acr config retention' is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
  - Policies are only supported for managed registries in Premium SKU. (Our sbox is "Standard")

## Secrets
Under `Settings` tab for the repository, go to `Secrets and variables` in the `Security` section.  
Here you can set __environment variables, repository variables, environment secrets__ and __repository secrets__
- [Using secrets in GitHub Actions](<https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions>)
- [About Variables](<https://docs.github.com/en/actions/learn-github-actions/variables#about-variables>)
- [Contexts](<https://docs.github.com/en/actions/learn-github-actions/contexts>)

## Links
- [Starter workflow for python-app](<https://github.com/actions/starter-workflows/blob/main/ci/python-app.yml>)
- [Starter Action Workflows to deploy to Azure](<https://github.com/Azure/actions-workflow-samples>)
- [Building and testing Python](<https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python>)
- [Workflow syntax for GitHub Actions](<https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategy>)  
- [Storing workflow data as artifacts](<https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts>)
- [upload-artifact](<https://github.com/actions/upload-artifact>)
- You can cache and restore the dependencies using the [setup-python action](<https://github.com/actions/setup-python>)
- To use a pre-installed version of Python or PyPy on a GitHub-hosted runner, use the [setup-python action](<https://github.com/actions/setup-python>).
- [Build and Push wheels](<https://andrewpwheeler.com/2022/05/10/building-wheel-files-in-github-actions/>)
- External reading and explanation of [GitHub Actions](<https://www.learnenough.com/blog/git-actions-tutorial>) 
- [Self-hosted runners](<https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners>) 
  - "We recommend that you only use self-hosted runners with private repositories. This is because forks of your public repository can potentially run dangerous code on your self-hosted runner machine by creating a pull request that executes the code in a workflow." 



## Actions Marketplace
- [Release Drafter](<https://github.com/marketplace/actions/release-drafter>)
  - Drafts your next release notes as pull requests are merged into master.

## Testing
Running tests in GitHub Actions

```yml
- name: Test with pytest
      run: |
        python -m pytest # <--
        python -B -m pytest # no cache
```