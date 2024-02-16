"""
Shedule_for_CK
(sorry for my English;)
"""
# import modules to get todasfd dates
import time
def CK_shedule(
    cleaning_room=903,
    num_of_days=6,
    rooms_str='903,904,905,906,908,909,910,911,912,913,914,915'):
    """
    this func create shedule for CK colegium for 12 days
    #>>> CK_shedule(903, 1)
    #       10.4 -  903
    #
    """
    # str of rooms
    rooms_str = rooms_str.split(',')
    # list str elemhents -> list int elemhents
    rooms = [int(room) for room in rooms_str]
    # amount days in every month
    amount_days_in_mounth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # get this year, month, day of month, day of weekday
    year = time.localtime(time.time()).tm_year
    month = time.localtime(time.time()).tm_mon
    m_day = time.localtime(time.time()).tm_mday
    w_day = time.localtime(time.time()).tm_wday+1
    # get index of room
    ind_of_room = rooms.index(cleaning_room)
    # create result str - schedule
    shedule = ""
    # cycle adds every cleanings to result str
    while num_of_days:
        # if Sunday, then we skip these iteration
        # day of weekday = 1(Monday)
        # day of month += 1(the next day)
        flag = False
        if w_day == 7:
            w_day=1
            m_day+=1
            flag = True
        # if day of month > days in month, then month+=1, day of month = 1
        if m_day > amount_days_in_mounth[month-1]:
            month+=1
            m_day=1
        # if month > 12, then month = 1, and we add one year
        if month>12:
            month = 1
            year+=1
        if flag:
            continue
        # add cleaning to result str
        shedule+= f"\t{m_day}.{month} -\t{rooms[ind_of_room]}\n"
        # get the next room index
        ind_of_room+=1
        # if we get the last index, then we get the first indx of list rooms
        if ind_of_room==len(rooms):
            ind_of_room=0
        # add one to month day
        m_day+=1
        # add one to weeknes day
        w_day+=1
        # numbers of cleaning -=1
        num_of_days-=1
    return shedule
# print(CK_shedule(903, 12)) # test schedule
