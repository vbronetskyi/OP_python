"""Lab_10.1"""
import pandas as pd

def read_data():
    """
    This function reads a csv file
    >>> len(read_data())
    146
    """
    solut = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in solut.columns:
        if col[:2] == '01':
            solut.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            solut.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            solut.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            solut.rename(columns={col: '#'+col[1:]}, inplace=True)
    names_ids = solut.index.str.split('\\s\\(')
    solut.index = names_ids.str[0]
    solut['ID'] = names_ids.str[1].str[:3]
    solut = solut.drop('Totals')
    return solut

def first_country(solut):
    """
    Should return a Series containing information
    about the first country in the list
    """
    return solut.iloc[0]

def summer_biggest(solut):
    """
    return the ribbon with the country that
    won the most gold medals
    """
    return solut['Gold'].idxmax()

def difference_biggest(solut):
    """
    return a ribbon with the country with the largest
    difference (modulo) between the number of gold medals
    """
    return abs(solut['Gold'] - solut['Gold.1']).idxmax()

def difference_biggest_relative(solut):
    """
    return the country that won the medals
    """
    solut = solut[(solut['Gold'] != 0) & (solut['Gold.1'] != 0)]
    return abs((solut['Gold'] - solut['Gold.1']) / solut['Gold.2']).idxmax()

def get_points(solut):
    """
    return all countries
    and the amount of points they have earned
    """
    solut["Points"] = (3 * solut['Gold.2']) + ((2 * solut['Silver.2'])) \
     + solut['Bronze.2']
    return solut['Points']

if __name__=="main" :
    import doctest
    print(doctest.testmod())
