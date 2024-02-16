"""Lab10.2"""
import pandas as pd

def read_data(f_csv) :
    """
    str -> DataFrame
    returns text from csv file
    >>> len(read_data('census.csv'))
    3193
    """
    text_f = pd.read_csv(f_csv)
    return text_f


def max_counties(f_csv):
    """
    Returns the seat with the largest number of counties
    >>> max_counties(read_data('census.csv'))
    'Texas'
    """
    return f_csv['STNAME'].value_counts().index[0]

def max_difference(f_csv):
    '''
    return country that contains the largest absolute change
    in the number of the population during 2010-2015.
    >>> max_difference(read_data('census.csv'))
    'Harris County'
    '''
    indx = f_csv.columns.get_loc('POPESTIMATE2010')
    indx_2 = f_csv.columns.get_loc('POPESTIMATE2015')


    data = f_csv.iloc[:, indx : indx_2]
    f_csv['diff'] = data.max(axis=1) - data.min(axis=1)
    idx = f_csv['diff'][(f_csv['SUMLEV'] == 50)].idxmax()

    return str(f_csv.at[idx,'CTYNAME'])


def conditional_counties(solut):
    '''
    function counties belonging to regions 1 or 2 whose name starts with 'Washington'
    This function should return a 5x2 DataFrame with columns = ['STNAME', 'CTYNAME']
    '''
    solut = solut[(((solut['REGION']) == 1) | ((solut['REGION']) == 2))]

    solut = solut.drop((solut[(solut['POPESTIMATE2015']) < (solut['POPESTIMATE2014'])]).index)
    solut = solut[["CTYNAME", "STNAME", 'REGION']]

    return solut[(solut['CTYNAME'].str.startswith('Washington'))]
if __name__=="main" :
    import doctest
    print(doctest.testmod())
