"""Performs operations on a movie data file"""
def read_file(path: str, year:int=0) -> list:
    """
    reads data from the file passed in the path argument starting
    with year and returns a list of lists
    where each inner list corresponds to a single movie record.
    >>> read_file('films.csv',2016)[:3]
    [['3', 'Split', 'Horror,Thriller', 'Three girls are kidnapped by a man with a diagnosed \
    23 distinct personalities. They must try to escape before the apparent emergence of a \
    frightful new 24th.', \
    'M. Night Shyamalan', 'James McAvoy, Anya Taylor-Joy, Haley Lu Richardson, Jessica Sula'\
        , '2016', '117', \
    '7.3', '157606', '138.12', '62.0'], ['4', 'Sing', 'Animation,Comedy,Family', "In a city \
        of humanoid animals, \
    a hustling theater impresario's attempt to save his theater with a singing competition becomes \
        grander than \
    he anticipates even as its finalists' find that their lives will never be the \
        same.", 'Christophe Lourdelet', \
    'Matthew McConaughey,Reese Witherspoon, Seth MacFarlane, Scarlett Johansson', '2016',\
         '108', '7.2', '60545', \
    '270.32', '59.0'], ['5', 'Suicide Squad', 'Action,Adventure,Fantasy', 'A secret government\
         agency recruits some \
    of the most dangerous incarcerated super-villains to form a defensive task force. Their first\
         mission: save the \
    world from the apocalypse.', 'David Ayer', 'Will Smith, Jared Leto, Margot Robbie, Viola Davis\
        ', '2016', '123', '6.2', \
    '393727', '325.02', '40.0']]
    """
    list_films = []
    with open(path, 'r',encoding="utf8") as file:
        file.readline()
        for line in file:
            lst_line = line.replace('\n', '').split(';')
            if int(lst_line[6]) > year:
                list_films.append(lst_line)
    return list_films
def selection_sort(lst):
    """
    Sort the list using the selection sort method.
    Return a sorted list
    >>> [('Action,Adventure,Sci-Fi', '8.8'), ('Action,Biography,Drama', '8.8'),\
    ('Action,Crime,Drama', '9.0')]
    [('Action,Biography,Drama', '8.8'), ('Action,Adventure,Sci-Fi', '8.8'), \
    ('Action,Crime,Drama', '9.0')]
    """
    def swap(list_, min_inx_, inx_):
        """
        swap elements in list
        """
        list_[inx_], list_[min_inx_] = list_[min_inx_], list_[inx_]
        return list_

    for inx in range(len(lst)):
        min_inx = inx
        for j in range(inx + 1, len(lst)):
            if lst[j][1] <lst[min_inx][1]:
                min_inx = j
        swap(lst, min_inx, inx)
    return lst

def top_n(data:list, num_rait:int) -> list:
    """
    given input data which is a list of lists about movies forms a list
    of tuples (Title, Rating), sorts the list of tuples in descending order
    based on the Rating value, and returns the first n movies with the highest value.
    >>> top_n(read_file('films.csv'),3)
    [('The Dark Knight', 9.0), ('Inception', 8.8), ('Dangal', 8.8)]
    [('Action,Biography,Drama', '8.8'), ('Action,Adventure,Sci-Fi', '8.8'), \
('Action,Crime,Drama', '9.0')]
    >>> top_n(read_file('films.csv'),4)
    [('Adventure,Drama,Sci-Fi', '8.6'), ('Action,Biography,Drama', '8.8'),\
        ('Action,Adventure,Sci-Fi', '8.8'), ('Action,Crime,Drama', '9.0')]
    """
    lst_of_top_films = []
    for film_date in data:
        lst_of_top_films.append((film_date[2], film_date[8]))
    return selection_sort(lst_of_top_films)[-num_rait:]
def genre_count(data:list) -> dict:
    """
    counts how many movies belong to a certain genre in the list of lists
    data. Returns a dictionary where the key is the name of the genre and
    the value is how many movies have that genre.
    >>> sorted(list(genre_count(read_file('films.csv')).items()))[:3]
    [('Action', 303), ('Adventure', 259), ('Animation', 49)]
    """
    films_genre = {}
    for film_date in data:
        if film_date[2] in films_genre:
            films_genre[film_date[2]]+=1
        else:
            films_genre[film_date[2]] = 1
    return films_genre
def write_file(genres: dict, file_name: str)-> None:
    """
    Writes data to file, name of file is given as second argument
    Takes input from genre_count function and writes data as follows
    (next lines must be in the file):
    Action,Adventure,Sci-Fi,50
    Adventure,Mystery,Sci-Fi,2
    Horror,Thriller,16
    .....
    """
    with open(file_name, "w",encoding="utf8") as file:
        for filp_gane in genres:
            file.write(str(filp_gane)+','+str(genres[filp_gane])+'\n')

if __name__ == "__main__":
    write_file(genre_count(read_file('films.csv')), "film.csv")
    import doctest
    print(doctest.testmod())
