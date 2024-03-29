with open('Gitpulltest', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('Gitpulltest1', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
