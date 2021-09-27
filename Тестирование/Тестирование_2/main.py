from RailingCalc import RailingCalc

if __name__ == '__main__':
    rc = RailingCalc(5, 18)
    print(rc.get_baluster_positions(float(input("введите длину пролета:\n"))))
