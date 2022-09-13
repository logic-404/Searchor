import enum
from urllib.parse import quote

class Engine:
    UrbanDictionary = "https://www.urbandictionary.com/define.php?term={query}"
    LinkedIn = "https://www.linkedin.com/search/results/all/?keywords={query}"
    Microsoft = "https://www.microsoft.com/en-us/search/explore?q={query}"
    InstantGaming = "https://www.instant-gaming.com/en/search/?q={query}"
    ChromeWebStore = "https://chrome.google.com/webstore/search/{query}"
    Mmoga = "https://www.mmoga.com/advanced_search.php?keywords={query}"
    OperaAddons = "https://addons.opera.com/en/search/?query={query}"
    CrunchyrollBeta = "https://beta.crunchyroll.com/search?q={query}"
    Wikipedia = "https://en.wikipedia.org/w/index.php?search={query}"
    Youtube = "https://www.youtube.com/results?search_query={query}"
    StackOverflow = "https://www.stackoverflow.com/search?q={query}"
    Lenovo = "https://www.lenovo.com/us/en/search?fq=&text={query}"
    Crunchyroll = "https://www.crunchyroll.com/search?q={query}"
    Facebook = "https://www.facebook.com/search/top/?q={query}"
    JetBrains = "https://www.jetbrains.com/search/?q={query}"
    Dictionary = "https://www.dictionary.com/browse/{query}"
    Target = "https://www.target.com/s?searchTerm={query}"
    Textures = "https://www.textures.com/search?q={query}"
    Thesaurus = "https://www.thesaurus.com/browse/{query}"
    Walmart = "https://www.walmart.com/search?q={query}"
    DuckDuckGo = "https://www.duckduckgo.com/?q={query}"
    Twitch = "https://www.twitch.tv/search?term={query}"
    Yahoo = "https://search.yahoo.com/search?p={query}"
    Github = "https://www.github.com/search?q={query}"
    Google = "https://www.google.com/search?q={query}"
    Genius = "https://www.genius.com/search?q={query}"
    Reddit = "https://www.reddit.com/search?q={query}"
    Twitter = "https://twitter.com/search?q={query}"
    Quora = "https://www.quora.com/search?q={query}"
    Bing = "https://www.bing.com/search?q={query}"
    Apple = "https://www.apple.com/search/{query}"
    Amazon = "https://www.amazon.com/s?k={query}"
    Custom = None

def search(query, engine=Engine.Google):
    return engine.format(query=quote(query, safe=""))

assert search("test") == "https://www.google.com/search?q=test"
assert search("test", Engine.Custom, "https://example.com/?q={query}") == "https://example.com/?q=test"
assert search("hello, world!") == "https://www.google.com/search?q=hello%2C%20world%21"