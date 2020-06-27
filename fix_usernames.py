import os

default_line_beginning = 'authors: [  '
default_line_ending = ']\n'

basedir = './'  # content dir
authors_folder = os.path.join(basedir, 'authors')
pub_folder = os.path.join(basedir, 'publication')

usernames = [item for item in os.listdir(authors_folder) if os.path.isdir(os.path.join(authors_folder, item))]
publication_dirs = [os.path.join(pub_folder, item) for item in os.listdir(pub_folder) if os.path.isdir(os.path.join(pub_folder, item))]
for publication_dir in publication_dirs:
    if not (publication_dir is './'):
        if os.path.isfile(os.path.join(publication_dir, 'index.md')):
            print(publication_dir)
            with open(os.path.join(publication_dir, 'index.md'), 'r') as f:
                text = f.readlines()
            for i, line in enumerate(text):
                if default_line_beginning in line:
                    authors_line = line[len(default_line_beginning):-len(default_line_ending)]
                    new_authors = default_line_beginning
                    for author in authors_line.split(', '):
                        author_arr = author.split(' ')
                        name, surname = author_arr[0][1:], author_arr[-1][:-1]
                        username_tmp = f'{name.lower()}_{surname.lower()}'
                        if username_tmp in usernames:
                            new_authors += f' {name.lower()}_{surname.lower()},'
                        else:
                            new_authors += f' {author},'
                    new_authors = new_authors[:-1] + default_line_ending
                    print(new_authors)
                    text[i] = new_authors
                    with open(os.path.join(publication_dir, 'index.md'), 'w') as f:
                        f.writelines(text)



