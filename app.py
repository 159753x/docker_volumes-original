def read_comments(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def write_comment(filename, comment):
    with open(filename, 'a') as file:
        file.write(comment + '\n')

if __name__ == '__main__':
    comments = read_comments('comments.txt')
    for comment in comments:
        print(comment.strip())

    new_comment = input('Unesite novi komentar: ')
    write_comment('comments.txt',  new_comment)