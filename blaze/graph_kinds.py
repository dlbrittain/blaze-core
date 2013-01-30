#------------------------------------------------------------------------
# Graph Node Kinds
#------------------------------------------------------------------------

# In APL parlance OP would be a Verb, FUN would Adverb, APP would be the
# conjunction of Adverb and Verbs and VAL would be Nouns.

OP  = 0
APP = 1
VAL = 2
FUN = 3

class graph_kind:
    OP  = OP
    APP = APP
    VAL = VAL
    FUN = FUN

__all__ = [
    'OP', 'APP', 'VAL', 'FUN'
]
