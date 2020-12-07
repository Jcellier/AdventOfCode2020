responses = []
response2 = []

def get_response(response):
    return len(list(dict.fromkeys(response)))


def get_response2(response):
    return len(list(set(response[0]).intersection(*response)))


for i in open("day6.txt").read().split("\n\n"):
    responses.append(get_response(i.replace("\n", "")))
    response2.append(get_response2(i.strip().split("\n")))

print(sum(responses))
print(sum(response2))