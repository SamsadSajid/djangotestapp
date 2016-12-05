## About

Basic "hello world" Django app showing a Facebook Page contents (e.g. `IsaacAsimov`) or Facebook Post (`isaacasimov/posts/735289683296645`)

## Instalation

1. Copy `settings.py`:
```
cp testapp/{_,}settings.py
```

2. Add Facebook GraphAPI and SECRET Tokens into the settings file
3. Run tests:
```
python manage.py test
```
4. Run server:
```
python manage.py runserver
```
Access locally at `localhost:8000`

## TODO

- [] production mode Debug=False
- [] the view has too much logic I don't think it belongs there
- [] 12factor
- [] DRY up tests
- [] Limit is 30 instead of 40 because of a bug similar to [this issue](https://github.com/mobolic/facebook-sdk/issues/281).
