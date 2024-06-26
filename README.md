# ghactions
Yaml examples:

- [Lint & Test](<.github/workflows/01-python-app.yml>)
- [Build & Push to ACR](<.github/workflows/02-build_push_sdai-sbox-gh-actions-app001.yml>)
- [Deploy Azure Web App](<.github/workflows/03-deploy_sdai-sbox-gh-actions-app001.yml>)
- [Trigger with Python](<.github/workflows/05-repository_dispatch-event.yml>) (repository_dispatch)

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

## Secrets
Under `Settings` tab for the repository, go to `Secrets and variables` in the `Security` section.  
Here you can set __environment variables, repository variables, environment secrets__ and __repository secrets__
- [About secrets in GitHub Actions](<https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions>)
- [About Variables](<https://docs.github.com/en/actions/learn-github-actions/variables#about-variables>)
- [Contexts](<https://docs.github.com/en/actions/learn-github-actions/contexts>)

## Actions Marketplace
- [GitHub Marketplace](<https://github.com/marketplace?type=actions>) for Actions
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

## Azure
- [Starter Action Workflows to deploy to Azure](<https://github.com/Azure/actions-workflow-samples>)
- [Tutorial: Deploy to App Service and connect to a database](<https://learn.microsoft.com/en-gb/azure/app-service/app-service-sql-asp-github-actions>)

### ACR
- [__Image tag best practices__](<https://learn.microsoft.com/en-us/azure/container-registry/container-registry-image-tag-version>)
- [__Retention policy for unused images__](<https://learn.microsoft.com/en-us/azure/container-registry/container-registry-retention-policy>)
  - Command group `acr config retention` is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
  - Policies are only supported for managed registries in Premium SKU. (Our sbox is "Standard")

### More on tagging
- __git commit__ – works until you start supporting base image updates, where your build system will kick off, with the same git commit as the previous built. However, the base image will have new content. Using a git commit winds up being a semi-stable tag.
- __date-time-stamp__ – this is a fairly common approach as you can clearly tell when the image was built. But, how do correlate it back to your build system? Do you have to find the build that was completed at the same time? What time zone are you in? Are all your build systems calibrated to UTC?
- __digest__ – it’s unique, or should be. But, it’s really not usable as it’s just toooooo long. And, it doesn’t really correlate with anything easily found.
- __build id__ – this one is __closest to the best__ as its likely incremental, gives you correlation back to the specific build to find all the artifacts and logs.
- __build_system-build_id__ – If your company has __several build systems__, prefixing the tag with the build system helps you differentiate the API team’s Jenkins build system from the Web teams VSTS build system.

## GitHub Actions Costs & Billing
- [About Billing](<https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions>)
- [About Spending limits](<https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#about-spending-limits>)
- [Per minute rates](<https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#per-minute-rates>)
- [Creating configuration variables for an organization](<https://docs.github.com/en/actions/learn-github-actions/variables#creating-configuration-variables-for-an-organization>)
  - Organization-level secrets and variables are not accessible by private repositories for GitHub Free

## Links
- [Starter workflow for python-app](<https://github.com/actions/starter-workflows/blob/main/ci/python-app.yml>)
- [Building and testing Python](<https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python>)
- [Workflow syntax for GitHub Actions](<https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategy>)  
- [Storing workflow data as artifacts](<https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts>)
- [upload-artifact](<https://github.com/actions/upload-artifact>)
  - Artifacts allow you to persist data after a job has completed, and share that data with another job in the same workflow.
- You can cache and restore the dependencies using the [setup-python action](<https://github.com/actions/setup-python>)
- To use a pre-installed version of Python or PyPy on a GitHub-hosted runner, use the [setup-python action](<https://github.com/actions/setup-python>).
- [Build and Push wheels](<https://andrewpwheeler.com/2022/05/10/building-wheel-files-in-github-actions/>)
- External reading and explanation of [GitHub Actions](<https://www.learnenough.com/blog/git-actions-tutorial>) 
- [Adding Self-hosted runners](<https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners>)
- [About Self-hosted runners](<https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners>) 
  - "We recommend that you only use self-hosted runners with private repositories. This is because forks of your public repository can potentially run dangerous code on your self-hosted runner machine by creating a pull request that executes the code in a workflow." 
s