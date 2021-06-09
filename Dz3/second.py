class C32:

    state = "A"

    def skid(self):
        if self.state == 'A':
            self.state = 'B'
            return 0

        elif self.state == 'E':
            self.state = 'F'
            return 7

        elif self.state == 'C':
            self.state = 'G'
            return 4

        elif self.state == 'G':
            self.state = 'H'
            return 10

        else:
            raise RuntimeError

    def shade(self):
        if self.state == 'B':
            self.state = 'C'
            return 1

        elif self.state == 'C':
            self.state = 'E'
            return 5

        elif self.state == 'F':
            self.state = 'G'
            return 8

        elif self.state == 'G':
            self.state = 'D'
            return 11

        else:
            raise RuntimeError

    def fill(self):
        if self.state == 'B':
            self.state = 'F'
            return 2

        elif self.state == 'C':
            self.state = 'D'
            return 3

        elif self.state == 'D':
            self.state = 'E'
            return 6

        elif self.state == 'F':
            self.state = 'C'
            return 9

        else:
            raise RuntimeError


#[0, 2, 8, 11, 6, 7, 9, 5, 7, 9, 4, 10]

#A skid 0
#B fill 2
#F shade 8
#G shade 11
#D fill 6
#E skid 7
#F fill 9
#C shade 5
#E skid 7
#F fill 9
#C skid 4
#G skid 10
#H

#obj = C32()
#print(obj.skid())
#print(obj.fill())
#print(obj.shade())
#print(obj.shade())
#print(obj.fill())
#print(obj.skid())
#print(obj.fill())
#print(obj.shade())
#print(obj.skid())
#print(obj.fill())
#print(obj.skid())
#print(obj.skid())



