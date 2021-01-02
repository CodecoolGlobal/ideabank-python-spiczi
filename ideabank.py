import sys


def write_ideas():
    try:
        while True:
            idea = input("What is your new idea? ")
            fh = open("ideas.txt", "a")
            fh.write(idea + '\n')
            fh.close()
            list = open("ideas.txt").readlines()
            for number, letter in enumerate(list, 1):
                print(number, letter)
    except KeyboardInterrupt:
        pass


def read_ideas():
    fh = open('ideas.txt','r')
    lines = fh.readlines()
    for number,letter in enumerate(lines,1):
        print(number, letter.strip())
    fh.close()


def delete_ideas(n):
    n = n - 1
    fh = open('ideas.txt','r')
    lines = fh.readlines()
    fh.close()
    lines2 = []
    for i in range(len(lines)):
        if i != n:
            lines2.append(lines[i])
    fh = open('ideas.txt','w')
    print(lines2)
    fh.writelines(lines2)
    fh.close()


if len(sys.argv) > 1 and sys.argv[1] == "--list":
    read_ideas()
elif len(sys.argv) == 3 and sys.argv[1] == "--delete":
    delete_ideas(int(sys.argv[2]))
else:
    write_ideas()


if __name__ == "__main__":
    pass