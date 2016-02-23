
# Created with

  docker run --rm --volume=$(pwd):/srv/jekyll -i -t  -p 127.0.0.1:4000:4000 jekyll/jekyll:pages jekyll new --force .

# Local hosting

  docker run --rm --volume=$(pwd):/srv/jekyll -i -t  -p 127.0.0.1:4000:4000 jekyll/jekyll:pages

This Jekyll website uses `site.github` var, see https://help.github.com/articles/repository-metadata-on-github-pages/,
this var is not available in the docker container only on https://*.github.io
