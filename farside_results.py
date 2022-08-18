"""Redirect to Farside"""

import sys
from urllib.parse import urlsplit, urlunsplit, urlparse

name = 'Farside Results'
description = 'Rewrite results with farside links'
default_on = True

urlmap = {
    'https://www.reddit.com': 'reddit',
    'https://redit.com': 'reddit',
    'https://old.reddit.com': 'reddit',
    'https://twitter.com': 'twitter',
    'https://mobile.twitter.com': 'twitter',
    'https://imgur.com': 'imgur',
    'https://i.imgur.com': 'imgur',
    'https://youtu.be': 'youtube',
    'https://www.youtube.com': 'youtube',
    'https://medium.com': 'medium',
    'https://wikipedia.org': 'wikipedia',
    'https://en.wikipedia.org': 'wikipedia'  # @todo what about the other locales?
}


def new_generic(url, redirect):
    url_arr = list(urlsplit(url))
    url_arr[0] = 'https'
    url_arr[1] = 'farside.link'
    url_arr[2] = f"/{redirect}{url_arr[2]}"
    return urlunsplit(url_arr)


def new_medium(url):
    # Scribe doesn't handle anything except individual blog posts
    url_arr = list(urlsplit(url))
    path = url_arr[2]
    if path.startswith("/@"):
        return new_generic(url, "scribe")
    else:
        return url


def new_youtube(url):
    return new_generic(url, "invidious")


def new_imgur(url):
    # Rimgo doesn't handle gifv links
    url_arr = list(urlsplit(url))
    path = url_arr[2]
    if path.endswith(".gifv"):
        return url
    else:
        return new_generic(url, "rimgo")


def new_reddit(url):
    return new_generic(url, "libreddit")


def new_twitter(url):
    return new_generic(url, "nitter")


def new_wikipedia(url):
    return new_generic(url, 'wikiless')


def mk_https(url: str):
    url_arr = list(urlsplit(url))
    url_arr[0] = "https"
    return urlunsplit(url_arr)


def new_link(url: str):
    for k in urlmap.keys():
        if mk_https(url).startswith(k):
            return getattr(sys.modules[__name__], "new_%s" % urlmap[k])(url)
    return url


def on_result(request, search, result):
    if result.get('url'):
        replacement = new_link(result['url'])
        result['url'] = replacement
        result['parsed_url'] = urlparse(replacement)
    return True
