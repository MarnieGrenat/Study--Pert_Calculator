#round(f, n)

def truncate(f, n) -> bool:
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

class Estimate:
    def __init__(self, o, n, p) -> None:
        self.o = o
        self.n = n
        self.p = p
        
    def set_optimistic(self, o:int) -> None:
        self.o = o
    def set_nominal(self, n:int) -> None:
        self.n = n
    def set_pessimistic(self, p:int) -> None:
        self.p = p
        
    def get_deadline(self):
        return self.mi_value()

    def get_probable_lateness(self):
        return self.probable_lateness()

    def get_estimates(self):
        return {
            'deadline': self.get_deadline(),
            'lateness': self.get_probable_lateness()
        }
    
    def mi_value(self) -> int:
        '''
        Calculates the MI {median} of a given set of values.
        O: optimistic estimate, N: nominal estimate, P: pessimistic estimate
        '''
        mi = (self.o + (4 * self.n) +  (self.p))/6
        if mi % int(mi) != 0:
            return int(mi) + 1
        return int(mi)
    
    def div_padrao(self) -> bool:
        '''
        Calculates the standard deviation of a given set of values.
        O: optimistic estimate, P: pessimistic estimate
        '''
        return (self.p - self.o) / 6

    def probable_lateness(self) -> int:
        '''
        Calculates the probable end date of a given set of values.
        '''
        return (self.mi_value() + self.div_padrao())
def set_estimate_values(data:Estimate, optimistic:float, nominal:float, pessimistic:float) -> None:
    data.set_optimistic(optimistic)
    data.set_nominal(nominal)
    data.set_pessimistic(pessimistic)