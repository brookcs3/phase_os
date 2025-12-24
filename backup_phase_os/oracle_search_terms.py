# Oracle Search Terms — for yt-dlp queries
# These can be rotated or extended to feed into Oracle Seed Engine

SEARCH_TERMS = [
    "rare vinyl breakbeats full album",
    "obscure funk LP",
    "lofi soul 1970s",
    "b-side disco 45",
    "italian horror soundtrack",
    "library music compilation",
    "japanese city pop cassette",
    "gospel soul vinyl",
    "soviet jazz record",
    "field recording folk LP",
    "spoken word experimental vinyl",
    "russian disco 80s",
    "private press psych rock",
    "avant-garde ambient vinyl",
    "children's educational music tape",
    "vhs music sampler rip",
    "industrial noise tape rip",
    "haunted vocal loops",
    "found sound archive"
]

if __name__ == "__main__":
    for term in SEARCH_TERMS:
        print(f"ytsearch5:{term}")
