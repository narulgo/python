

def calculate_hits(history):
    hits = {}
    for user, sites in history.items():
        for site in sites:
            if site not in hits:
                hits[site] = 1
            else:
                hits[site] = hits[site] + 1

    return hits


history = { 'user1': ['google.com', 'teachbase.ru'],
            'user2': ['yandex.ru', 'teachbase.ru'],
            'user3': ['google.com', 'youtube.com', 'mail.ru'],
            'user4': ['google.com', 'stackoverflow.com', 'python.org'] }


print(calculate_hits(history))


