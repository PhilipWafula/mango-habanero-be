# CHANGELOG



## v0.4.0 (2024-04-26)

### Chore

* chore(CI-CD): Triages failure in bot bypass to rule-sets.

- Refactors app-id and private-key arguments to address deprecation warning.
- Removes unrecognized persist credentials argument from semantic release step. ([`f9cee96`](https://github.com/mango-habanero/mango-habanero-be/commit/f9cee96c0234d3b4466d2511ab9a18f456e27ee5))

* chore(docker): Matches renaming of app module to src. ([`7ac0a95`](https://github.com/mango-habanero/mango-habanero-be/commit/7ac0a95eaaf81ea26815c12eb2165cf6c3af7351))

* chore(dependencies): Adds logging and http request related dependencies.

- Adds reload functionality to granian for development.
- Adds asgi-correlation-id for adding correlation ids for all incoming
requests.
- Adds structlog for logging. ([`85d802c`](https://github.com/mango-habanero/mango-habanero-be/commit/85d802c0ff806174c0681bc3ed451eb81382857e))

### Feature

* feat(releases): Integrates mango-habanero-bot to safely bypass branch protection ruleset. (#19) ([`03eb962`](https://github.com/mango-habanero/mango-habanero-be/commit/03eb962b27e0eb93cc202fb42cf502b44388dfa8))

* feat(middleware): Adds a custom http request logging middleware.

- Adds contextual information for API http request logging. ([`dc0c0bc`](https://github.com/mango-habanero/mango-habanero-be/commit/dc0c0bcd7355b49e3f30b9838d8190d4fe59521f))

* feat(logging): Implements structlog for structure logging of within application.

- Adds a generic system logger that implements structlog logging. ([`75ddd59`](https://github.com/mango-habanero/mango-habanero-be/commit/75ddd59e55ce8e85e624ed32a918e5392b0147ca))

### Refactor

* refactor(structure): Moves application creation and configuration into app module. ([`5558504`](https://github.com/mango-habanero/mango-habanero-be/commit/5558504d8bc758ef3356b61e700e566daa409a8c))

* refactor(structure): Renames app directory to src. ([`71b965b`](https://github.com/mango-habanero/mango-habanero-be/commit/71b965ba324e124c7f7d99403e83d0e8daa297d9))

### Unknown

* Merge pull request #18 from mango-habanero/philip/feat/logging

Enhance logging, refactor project structure, and update development settings. ([`584376e`](https://github.com/mango-habanero/mango-habanero-be/commit/584376eb39e546783e8879a21389f28c9cd9e7bd))

* Merge &#39;https://github.com/mango-habanero/mango-habanero-be&#39; main into philip/feat/logging ([`4ccd4ad`](https://github.com/mango-habanero/mango-habanero-be/commit/4ccd4adf6536d812bcf9c089603b7ac3a2c2608d))

* ⬆ Bump ruff from 0.4.1 to 0.4.2 (#17)

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.4.1 to 0.4.2.
- [Release notes](https://github.com/astral-sh/ruff/releases)
- [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md)
- [Commits](https://github.com/astral-sh/ruff/compare/v0.4.1...v0.4.2)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`560a58a`](https://github.com/mango-habanero/mango-habanero-be/commit/560a58ae550ea2ea917a9ca1e6e5ff439bedcf08))

* Merge pull request #16 from mango-habanero/dependabot/pip/mypy-1.10.0

⬆ Bump mypy from 1.9.0 to 1.10.0 ([`70c602f`](https://github.com/mango-habanero/mango-habanero-be/commit/70c602f4f5d8efa8585f8599e83fda39ea29984b))

* ⬆ Bump mypy from 1.9.0 to 1.10.0

Bumps [mypy](https://github.com/python/mypy) from 1.9.0 to 1.10.0.
- [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md)
- [Commits](https://github.com/python/mypy/compare/1.9.0...v1.10.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`81d9648`](https://github.com/mango-habanero/mango-habanero-be/commit/81d9648ad3cadb7fccd96a5fab9234fd950cbc90))


## v0.3.0 (2024-04-24)

### Chore

* chore(release): Release 0.3.0 🚀. ([`cb25093`](https://github.com/mango-habanero/mango-habanero-be/commit/cb25093c3405b5ceab57485b8bacd47fddc70d0f))

* chore(CI-CD): Grant python-semantic-release access to full commit history. ([`fe3896f`](https://github.com/mango-habanero/mango-habanero-be/commit/fe3896f8948598a3f18dfda4a1f7cfa67f5e0be6))

* chore(commits): Adds custom commit message for releases. ([`752ac16`](https://github.com/mango-habanero/mango-habanero-be/commit/752ac164bc356e5fc99d20d4450ccbf1377047bd))

### Feature

* feat(CI-CD): Introduces composite actions and package caching.

- Adds composite action to set up python and install dependencies using
poetry.
- Introduced caching poetry dependencies to speed up builds.
- Adds version based tagging for cleaner imager tags. ([`b2bb71c`](https://github.com/mango-habanero/mango-habanero-be/commit/b2bb71c862ae36c4962be87f0e2566ed32e498d6))

### Fix

* fix(CI-CD): Removes unnecessary value with in versioning. ([`c3fea79`](https://github.com/mango-habanero/mango-habanero-be/commit/c3fea792bde09b1529a2e5adaa278f3df50d9cae))

* fix(CI-CD): Corrects outputs to properly access build version. ([`7d54d47`](https://github.com/mango-habanero/mango-habanero-be/commit/7d54d475f77eba74f94ca56366a35ec334960304))

* fix(CI-CD): Adds check to fail at versioning task if version is not appropriately determined. ([`89afbf8`](https://github.com/mango-habanero/mango-habanero-be/commit/89afbf80e5837029f4206ce14a5d934b6caeec92))

* fix(CI-CD): Implements syntax fixes to workflow.

- Patches soon-to-be deprecated &#34;set-out&#34; in favor of updated syntax.
- Prefixes semantic-release command with poetry run. ([`52182f2`](https://github.com/mango-habanero/mango-habanero-be/commit/52182f2d4b1c53f1109468f014ab3c6801f84e25))

* fix(CI-CD): Implements correct composite action syntax with &#34;action.yml&#34;. ([`cfd1e2c`](https://github.com/mango-habanero/mango-habanero-be/commit/cfd1e2c9c1f1075fc14b7216436ac674b0879352))

### Refactor

* refactor(CI-CD): Separates versioning into individual job. ([`875c47f`](https://github.com/mango-habanero/mango-habanero-be/commit/875c47f11692bfca69d6b21b4457d8915db78582))

* refactor(containerization): Switches Dockerfile base image to alpine.

- Ensure app is not run by root user. ([`88e0057`](https://github.com/mango-habanero/mango-habanero-be/commit/88e0057f727890897a084aaa5139c31cc421b50a))

### Unknown

* Merge pull request #15 from mango-habanero/philip/refactor/ci-cd

Enhance CI/CD workflow with composite actions, alpine base Image, and improved tagging. ([`8249245`](https://github.com/mango-habanero/mango-habanero-be/commit/82492459455b818b9daf1d20cf3fe422c56689ff))


## v0.2.0 (2024-04-24)

### Build

* build(docker): Refactors docker startup cmd to run granian server. ([`8941bdf`](https://github.com/mango-habanero/mango-habanero-be/commit/8941bdf3e2883a6e22ba292ffd582211c81e760b))

* build(security): Adds dependabot configuration to enable daily security checks and dependency updates. ([`05f4227`](https://github.com/mango-habanero/mango-habanero-be/commit/05f42273dd55731e3d746ac28fccbec49ebb6ab3))

### Chore

* chore(server): Replaces uvicorn with granian.

- Swaps uvicorn for granian dependency. ([`1d90d2c`](https://github.com/mango-habanero/mango-habanero-be/commit/1d90d2c19ed187001b08f9378b51887a2deb6b3b))

### Feature

* feat(server): Implements granian server in development and generic server cli commands. ([`1470cc8`](https://github.com/mango-habanero/mango-habanero-be/commit/1470cc80b78fec16697dbd6aaa12cce95176c771))

### Unknown

* 0.2.0

Automatically generated by python-semantic-release ([`d903c90`](https://github.com/mango-habanero/mango-habanero-be/commit/d903c90be14d864790a983a2fbd6545baec17118))

* Merge pull request #12 from mango-habanero/philip/feat/granian

Implement Granian server and enhanced performance. ([`c04658f`](https://github.com/mango-habanero/mango-habanero-be/commit/c04658fcaa3723ddffff23b9afc0a48c01993c7d))

* Merge pull request #11 from PhilipWafula/philip/feat/dependabot

Integrate depandabot. ([`b306021`](https://github.com/mango-habanero/mango-habanero-be/commit/b3060212a703e395141b9cc4bc8a91d105afba93))


## v0.1.0 (2024-04-23)

### Build

* build(dependencies): Adds ci-cd related dependencies and corresponding pyproject.toml configurations.

- Explicitly defined app as package to include with poetry install.
- Adds click for cli definition.
- Adds pre-commit to implement git pre-commit hooks.
- Adds python-semantic release to handle semantic release in CI-CD
workflow.
- Implements configurations for mypy, ruff and semantic-release dependencies. ([`a549f40`](https://github.com/mango-habanero/mango-habanero-be/commit/a549f403897d7594566c9f004d758358e675a653))

* build(git-hooks): Adds configuration file for pre-commit git hooks. ([`961d242`](https://github.com/mango-habanero/mango-habanero-be/commit/961d2426a033badd93b6cc278b66896c5fd8a54c))

* build(versioning): Adds distinct version definition for use with python-sematic-release. ([`355c686`](https://github.com/mango-habanero/mango-habanero-be/commit/355c68627512effee44d8d623a9bd4c1c449fb3c))

### Chore

* chore(CI-CD): Enables manual triggering of workflows. ([`84b62a1`](https://github.com/mango-habanero/mango-habanero-be/commit/84b62a17b1f878062f7de15b4197f0b8ad4746be))

* chore(exception): Adds custom app exceptions module. ([`a9268d1`](https://github.com/mango-habanero/mango-habanero-be/commit/a9268d10b1a4a962cc841d05c652f8f503c4590d))

### Ci

* ci(CI-CD): Removes unnecessary run of CI-CD workflow in pull request. ([`a418f8c`](https://github.com/mango-habanero/mango-habanero-be/commit/a418f8c7624eed9c42ebd5a89c1c7398587d88c4))

* ci(CI-CD): Integrates GitHub actions.

- Implements GitHub Actions CI-CD workflow. ([`a87aec9`](https://github.com/mango-habanero/mango-habanero-be/commit/a87aec90119edd61c65220a0c9e1ae9c732e7dff))

* ci(containerization): Implements docker.

- Adds Dockerfile to containerize application.
- Adds docker-compose file to spin up docker image instance.
- Adds .dockerignore file for files to exclude from docker image. ([`49bf21f`](https://github.com/mango-habanero/mango-habanero-be/commit/49bf21f760590d402e95f352401dc96a33d52532))

* ci(integrations): Add GitHub Pull Request templates.

- Adds pull request template file. ([`946ce8b`](https://github.com/mango-habanero/mango-habanero-be/commit/946ce8b061c3733dae0b2b56eb14dd5340c4a2b2))

* ci(integrations): Add GitHub issue templates.

- Adds template files to enable the creation of consistent bug reports,
feature and refactor requests. ([`dfbf414`](https://github.com/mango-habanero/mango-habanero-be/commit/dfbf41456e72c27dc263b49fbbbafb94e57e4108))

### Feature

* feat(devX): Adds generic mh CLI for server related operations.

- Implements a CLI to handle starting the server. ([`f5c64a1`](https://github.com/mango-habanero/mango-habanero-be/commit/f5c64a1ca7569305cd5cf36b18357ea0e2ea5155))

* feat(structure): Initialize the Fast API application. ([`4ec891e`](https://github.com/mango-habanero/mango-habanero-be/commit/4ec891e8912185056847945231430152e6a7e44f))

### Fix

* fix(CI-CD): Adds access to all history as required by python-semantic-release. ([`459c64d`](https://github.com/mango-habanero/mango-habanero-be/commit/459c64d250b8bf381b2bac614c5a2133af91ba29))

* fix(CI-CD): Corrects docker image tags in build-push CI-CD job. ([`6b8ddbe`](https://github.com/mango-habanero/mango-habanero-be/commit/6b8ddbe4925733929c3daa8bcde0cedb0c552c02))

### Style

* style(structure): Moves all modules into paranet package app. ([`fc96e49`](https://github.com/mango-habanero/mango-habanero-be/commit/fc96e493f0863550c212c64b1fe113b4e8288789))

* style(style-guide): Adds dependencies for formatting, linting and static type checking.

- Adds ruff for formatting and linting.
- Adds mypy for static type checking.
- Adds ruff and mypy configurations in pyproject.tml. ([`dcbf3dd`](https://github.com/mango-habanero/mango-habanero-be/commit/dcbf3dd1a3e5449a899fca72dea160e7b4abe350))

### Unknown

* 0.1.0

Automatically generated by python-semantic-release ([`d1a7c3a`](https://github.com/mango-habanero/mango-habanero-be/commit/d1a7c3a889a246c3470e579ff027c9d43f8631d6))

* Merge pull request #9 from PhilipWafula/philip/feat/ci-cd

Infrastructure setup: CI/CD Integration, CLI tools, containerization, and more. ([`5e8d609`](https://github.com/mango-habanero/mango-habanero-be/commit/5e8d6091948ba8fc813488c43c6ac5cb08ec27e3))

* Merge branch &#39;main&#39; into philip/feat/ci-cd ([`da8d578`](https://github.com/mango-habanero/mango-habanero-be/commit/da8d5789f48474a4182ff5b65858daf87be72450))

* Merge pull request #8 from PhilipWafula/philip/feat/python-style-guide

Integrate Ruff and Mypy for enhanced code quality. ([`74ea0f4`](https://github.com/mango-habanero/mango-habanero-be/commit/74ea0f4037307b2855249c5786d21528af2d22ba))

* Merge pull request #6 from PhilipWafula/philip/integrations/github-templates

Implement standardized GitHub Issue and pull request templates. ([`c7be4e5`](https://github.com/mango-habanero/mango-habanero-be/commit/c7be4e5077642d9b12a82bdd160b037780fc838f))
