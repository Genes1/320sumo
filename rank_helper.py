# https://en.wikipedia.org/wiki/Professional_sumo_divisions
import re

# increasing order of rank
divisions = {
                'Maezumo' : 0, 
                'Jonokuchi' : 1,
                'Jonidan' : 2,
                'Sandanme' : 3,
                'Makushita' : 4,
                'Juryo' : 5,
                'Maegashira' : 6,
                'Komusubi' : 7,
                'Sekiwake' : 8,
                'Ozeki' : 9,
                'Yokozuna' : 10
            }

names = {
    
        'Sd' : 'Sandanme',
        'S' : 'Sekiwake',
    
        'Jk' : 'Jonokuchi',
        'Jd' : 'Jonidan',
        'J' : 'Juryo',

        'Mz' : 'Maezumo',
        'Ms' : 'Makushita',
        'M' : 'Maegashira',
    
        'K' : 'Komusubi',
        'O' : 'Ozeki',
        'Y' : 'Yokozuna'
}



    
# 'Jk47e' -> 'Jonokuchi'
def long_rank(rank): 
    if rank[1].isdigit():
        return names[rank[0]] 
    else:
        return names[rank[:2]]
        
# 'Jk47e' -> ('Jonokuchi', 47) 
def full_rank(rank): 
    n = re.findall('\d+', rank)
    n = None if not n else int(n[0])
    return (long_rank(rank), n)
    
    
# checks to see if the rank [in form 'Jk47e'] is in the top two divisions.
def rank_is_top(rank, is_long=False):

    if not is_long:
        try:
            return divisions[long_rank(rank)] >= 5
        except: 
            return False
    else:
        try:
            return divisions[rank] >= 5
        except: 
            return False


def rank_is_sanyaku(rank):
    return divisions[long_rank(rank)] > 6


#def rank_difference(r1, r2):
