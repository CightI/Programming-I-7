from stanfordkarel import *


class ktools:

    def m(self):
        """Short for Move"""
        move()

    def tl(self):
        """Turn Left"""
        turn_left()

    def tr(self):
        """Turn Right"""
        self.tl()
        self.tl()
        self.tl()

    def ta(self):
        """Turn Around"""
        self.tl()
        self.tl()

    def pick(self):
        """Pick Beeper"""
        pick_beeper()

    def put(self):
        """Put beeper"""
        put_beeper()

    def put2(self):
        """Put 2 beepers in a line"""
        self.put()
        self.m()
        self.put()

    def put5(self):
        self.put2()
        self.m()
        self.put2()
        self.m()
        self.put()

    def h(self):
        """Print H using beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.tr()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()

    def e(self):
        """Print E using beepers"""

        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.put2()
        self.put2()
        self.ta()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.put2()
        self.ta()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.put2()
        self.m()
        self.m()

    def l(self):
        """Print L using beepers"""
        self.tl()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.put2()
        self.m()
        self.m()

    def o(self):
        """Print o using beepers"""
        self.put2()
        self.m()
        self.put()
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.put()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()

    def u(self):
        """Print U using beepers"""
        self.put2()
        self.m()
        self.put()
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.put()
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.put()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()

    def k(self):
        """Print K using beepers"""
        self.tl()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.m()
        self.tr()
        self.m()
        self.put()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tr()
        self.put()
        self.m()
        self.tr()
        self.m()
        self.put()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.tr()
        self.m()
        self.tl()


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.l()
    kt.u()
    kt.k()
    kt.e()

    pass


if __name__ == "__main__":
    run_karel_program()
