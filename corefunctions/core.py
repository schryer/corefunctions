'''
Module that provides basic functions to be used in most Python projects.
'''

__all__ = ['collections', 'namedtuple', 'defaultdict', 'OrderedDict', 'convert_nested_defaultdict_to_dict',
           'make_nested_defaultdict', 'pprint', 'pf', 'pp', 'itertools', 'pairwise', 'resource', 'memory_used']

############################  Functions based on the progressbar module (external)  ################################
import progressbar

def make_progressbar(msg='Default progressbar message: ', maxval=0)
    return progressbar.ProgressBar(widgets=[msg, progressbar.Percentage(),
                                            progressbar.Bar(widget=marker=progressbar.RotatingMarker())],
                                   maxval=maxval).start()
####################################################################################################################

############################  Functions based on the collections module  ###########################################
import collections
from collections import namedtuple, defaultdict, OrderedDict

def convert_nested_defaultdict_to_dict(dd):
    return {k:convert_nested_defaultdict_to_dict(v) for k,v in dd.items()} if isinstance(dd, defaultdict) else dd
    
def make_nested_defaultdict(inner_type, N=1):
    if N == 1:
        return defaultdict(lambda:defaultdict(inner_type))
    elif N == 2:
        return defaultdict(lambda:defaultdict(lambda:defaultdict(inner_type)))
    elif N == 3:
        return defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:defaultdict(inner_type))))
    elif N == 4:
        return defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:defaultdict(inner_type)))))
    elif N == 5:
        return defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:defaultdict(inner_type))))))
    else:
        raise NotImplementedError('This level of nested defaultdict has not yet been implemented.', N)
#####################################################################################################################


        
##############################  Functions used for text formatting  #################################################
import pprint

def pf(item):
    return pprint.pformat(item)

def pp(item):
    print(pf(item))
######################################################################################################################
    

    
##############################  Functions based on the itertools module  #############################################
import itertools
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
######################################################################################################################


    
##############################  Functions used in debugging  #########################################################
import resource
def memory_used(units='kB'):
    m = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if units in ['mB', 'MB']:
        m = m / 1024.0
    return '{} kB'.format(m)
######################################################################################################################