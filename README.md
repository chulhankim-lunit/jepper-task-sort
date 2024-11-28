# jepper-task-sort

A template project for Python based software.

## Contents

- [How to use](#how-to-use)
- [Requirements](#requirements)
- [Setup](#setup)
    - [Install dependencies](#install-dependencies)
    - [Git hooks](#git-hooks)
- [Preferred structure](#preferred-structure)

## How to use

You can refer to the structure of this project for your new Python project. More preferably, you can set this project as a template when you create a new GitHub private repository.

## Requirements

- Homebrew
- Python 3.12 ([Setup guide](https://lunit.atlassian.net/wiki/x/ZwFEu))
- Poetry
- Docker ([Setup guide](https://lunit.atlassian.net/wiki/x/DYMdw))
- Node.js

## Setup

### Install dependencies

Change information in `pyproject.toml` and `package.json` to your project's information.

```zsh
poetry install --no-root
```

### Git hooks

```shell
npm install
```

The command above enables `commit-msg` and `pre-commit` hooks.

## Preferred structure

The project recommends to be used with hexagonal architecture. A sample package structure is as follows:

```
app
├── adapter
│   ├── _in
│   │   ├── amqp
│   │   │   ├── config
│   │   │   ├── consumer
│   │   │   ├── dto
│   │   │   ├── exception
│   │   │   └── mapper
│   │   └── rest
│   │       ├── config
│   │       ├── consumer
│   │       ├── dto
│   │       ├── exception
│   │       └── mapper
│   └── out
│       ├── amqp
│       │   ├── config
│       │   ├── dto
│       │   ├── exception
│       │   ├── mapper
│       │   └── producer
│       └── persistence
│           ├── rdb
│           │   ├── config
│           │   ├── entity
│           │   ├── mapper
│           │   └── repository
│           └── s3
│               ├── config
│               ├── client
│               └── mapper
├── application
│   ├── domain
│   ├── port
│   │   ├── _in
│   │   └── out
│   └── service
├── common
│   ├── config
│   └── exception
└── main.py
```
