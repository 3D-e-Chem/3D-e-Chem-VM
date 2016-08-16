

# Created with

```
docker run --rm --volume=$(pwd):/srv/jekyll -i -t  -p 127.0.0.1:4000:4000 jekyll/jekyll:pages jekyll new --force .
```

# Generate config

```
pip install -r utils/requirements.txt
python utils/gen_config.py <organization> <repo>
```

This will use the Github API to fetch information about the repo and write the `_config.yml` file. The `_config.yml` must be edited to complete the configuration.

# Local hosting

```
docker run --rm --volume=$(pwd):/srv/jekyll -i -t  -p 127.0.0.1:4000:4000 jekyll/jekyll:pages
```

The website will be hosted at `http://localhost:4000/<repo name>/`.
