# -*- coding: cp936 -*-
class OpenMovieFiles:
        def __init__(self, *endstring):
                self.ends = endstring
        
        def endWith(self):
                def run(s):
                        f = map(s.endswith,self.ends)
                        if True in f: return s
                return run

        

