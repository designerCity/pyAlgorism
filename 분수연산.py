class Rational:
    def __init__(self, top = 1, bottom = 1):  # 초기화하는 함수 __init_를 constructor
        if bottom == 0:
            raise ZeroDivisionError("Cannot have 0 denominator")
        self.numerator = abs(top)
        self.denominator = abs(bottom)
        self.sign = (top* bottom) / (self.numerator * self.denominator)
        self.simplify()
    
    def gcd(x, y):
        while y:
            z = x
            x = y
            y = z % y
        return x
    
    def simplify(self):
        common = Rational.gcd(self.numerator, self.denominator)
        self.numerator /= common
        self.denominator /= common
        
    def __neg__(self):
        return Rational(-self.sign * self.numerator, self.denominator)
    
    def __add__(self, other):
        return Rational(
            self.sign * self.numerator * other.denominator +
            other.sign * other.numerator * self.denominator,
            self.denominator * other.denominator
        )
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        return Rational(self.numerator * other.numerator,
                       self.sign * self.denominator * other.sign * other.denominator)
    
    def __div___(self, other):
        return Rational(self.numerator * other.denominator,
                        self.sign * self.denominator * other.sign * other.numerator)
    def __truediv__(self, other):
        return self.__div___(other)
    
    def __eq__(self,other):
        return (self-other).numerator == 0
    
    def __lt__(self,other):
        return (self-other).sign < 0
    
    def __gt__(self,other):
        return (self-other).sign > 0
    
    def __le__(self,other):
        return (self < other) or(self == other)
    
    def __ge__(self,other):
        return (self > other) or (self == other)
    
    def __ne__(self,other):
        return not (self == other)
    
    def __abs__(self):
        return Rational(self.numerator, self.denominator)
    
    def __str__(self):
        if self.sign == -1:
            signString = "-"
        else:
            signString = ""
        
        if self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return "%s%d" % (signString, self.numerator)
        else:
            return "%s%d/%d" % \
                (signString, self.numerator, self.denominator)
        
