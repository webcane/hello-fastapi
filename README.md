# Hello App

## prerequisites
install poetry
```commandline
brew install poetry
```

## first time setup
```commandline
poetry env activate
```

## run app
```commandline
poetry run uvicorn hello_app.main:app --reload --app-dir src
```