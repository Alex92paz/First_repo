from decimal import Decimal, getcontext

getcontext().prec = 6
print(Decimal("233") / Decimal("7"))
