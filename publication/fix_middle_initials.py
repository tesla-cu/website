import os

default_line_beginning = 'authors: ['
default_line_ending = ']\n'
basedir = './'
for publication_dir, _, files in os.walk(basedir):
    if not (publication_dir is './'):
        print(publication_dir, files[1])
        with open(os.path.join(publication_dir, files[1]), 'r') as f:
            text = f.readlines()
        print(text[4])
        authors_line = text[4][len(default_line_beginning):-2]
        new_authors = default_line_beginning
        for authors in authors_line.split(', '):
            author_arr = authors.split(' ')
            name, surname = author_arr[0], author_arr[-1]
            new_authors += f' {name} {surname},'
        new_authors = new_authors[:-1] + default_line_ending
        print(new_authors)
        text[4] = new_authors
        with open(os.path.join(publication_dir, files[1]), 'w') as f:
            f.writelines(text)



