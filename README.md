# Farside Results

A highly experimental [SearXNG](https://github.com/searxng/searxng) plugin that rewrites results for certain sites to use privacy-protecting alternatives via [Farside](https://github.com/benbusby/farside/)

There is no configuration, it's all or nothing redirection of the following:

* Imgur
* Medium
* Reddit
* Twitter
* YouTube

## Why?

Because:
* The hostname_replace plugin only handles entire hostnames and Medium/Scribe needs some extra care
* We don't want to redirect to a single static alternative because that gives those providers too much power
* Because sometimes these alternatives go down and we don't want to keep track of our own list of available providers

## How?

Well I'm copying farside_redirect.py into `searxng/plugins/` and then adding the following to searxng/settings.yml:

```yml
plugins:
  - farside_results
```

But there's probably a better way
