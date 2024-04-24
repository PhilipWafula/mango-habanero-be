# CHANGELOG



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

* Merge pull request #9 from PhilipWafula/philip/feat/ci-cd

Infrastructure setup: CI/CD Integration, CLI tools, containerization, and more. ([`5e8d609`](https://github.com/mango-habanero/mango-habanero-be/commit/5e8d6091948ba8fc813488c43c6ac5cb08ec27e3))

* Merge branch &#39;main&#39; into philip/feat/ci-cd ([`da8d578`](https://github.com/mango-habanero/mango-habanero-be/commit/da8d5789f48474a4182ff5b65858daf87be72450))

* Merge pull request #8 from PhilipWafula/philip/feat/python-style-guide

Integrate Ruff and Mypy for enhanced code quality. ([`74ea0f4`](https://github.com/mango-habanero/mango-habanero-be/commit/74ea0f4037307b2855249c5786d21528af2d22ba))

* Merge pull request #6 from PhilipWafula/philip/integrations/github-templates

Implement standardized GitHub Issue and pull request templates. ([`c7be4e5`](https://github.com/mango-habanero/mango-habanero-be/commit/c7be4e5077642d9b12a82bdd160b037780fc838f))
