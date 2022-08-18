# Farside Results

A highly experimental [SearXNG](https://github.com/searxng/searxng) plugin that rewrites results for certain sites to use privacy-protecting alternatives via [Farside](https://github.com/benbusby/farside/)

There is no configuration, it's all or nothing redirection of the following:

* Imgur
* Medium
* Reddit
* Twitter
* YouTube
* Wikipedia

## Why?

Because:
* The hostname_replace plugin only handles entire hostnames and Medium/Scribe and Imgur/Rimgo needs some extra care
* We don't want to redirect to a single static alternative because that gives those providers too much power
* Because sometimes these alternatives go down and we don't want to keep track of our own list of available providers

## Why not?

Because the owners of farside.link get to see every farside.link that you click on and could be tracking you

To resolve this issue we really need multiple instances of Farside run by different people, but that brings us back to the one of the original problems - that we don't want to do this ourselves

## How?

### Local Development

Copy farside_redirect.py into `searxng/plugins/` and then adding the following to searxng/settings.yml:

```yml
plugins:
  - farside_results
```

### Searxng-docker

Create `Dockerfile`:

```dockerfile
FROM  searxng/searxng:latest

RUN apk add git
RUN pip3 install git+https://github.com/wheresalice/farside-results
```

Replace the `image: searxng/searxng:latest` line with `build: .`

Then enable the plugin in searxng/settings.yml:

```yaml
plugins:
  - farside_results
```

