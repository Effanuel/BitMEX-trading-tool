from decimal import Decimal

import math
import functools


def toNearest(num, tickSize):
    """Given a number, round it to the nearest tick. Very useful for sussing float error
       out of numbers: e.g. toNearest(401.46, 0.01) -> 401.46, whereas processing is
       normally with floats would give you 401.46000000000004.
       Use this after adding/subtracting/multiplying numbers."""
    tickDec = Decimal(str(tickSize))
    return float((Decimal(round(num / tickSize, 0)) * tickDec))


def roundHalf(number, inc, prec=2) -> float:
    return round(inc * round(float(number) / inc), prec)


# /**
#  * Probability density function
#  * @param {number} mean of the distribution
#  * @param {number} x is a point in that distribution
#  * @param {number} delta is a variance parameter
#  * @returns {number} location probability of that x
#  */
def gaussian(mean, x, delta) -> float:
    member1 = 1 / (delta * math.sqrt(2 * math.pi))
    member2 = math.pow(math.E, -((x - mean) ** 2) / (2 * delta ** 2))
    return member1 * member2


def Uniform(quantity, n_tp, start, end, side, symbol):
    inc = 0.5 if symbol == "XBTUSD" else 0.05
    # start = toNearest(start, inc)
    start1 = roundHalf(start, inc)
    end1 = roundHalf(end, inc)

    orders = []
    increment = roundHalf((end1 - start1) / (n_tp - 1), inc)
    mean = math.floor(quantity / n_tp)
    # startEndPutOrders(orders.orders, start, end, mean, side)

    for i in range(n_tp):
        # ROUND TO NEAREST 0.5

        orders.append(
            {
                "symbol": symbol,
                "side": side,
                "orderQty": mean,
                "price": float(start1 + i * increment),
                "ordType": "Limit",
                "text": "order",
            }
        )
    return orders


def Positive(quantity, n_tp, start, end, side, symbol):
    inc = 0.5 if symbol == "XBTUSD" else 0.05

    start1 = roundHalf(start, inc)
    end1 = roundHalf(end, inc)

    START_CFG = -1
    END_CFG = 1

    incrementQty = (END_CFG - START_CFG) / (n_tp - 1)

    # arr = []
    # for i in range(n_tp):
    #    arr.append(gaussian(-1, START_CFG + i * incrementQty, 1)) #//mean == -1

    # summ = functools.reduce(lambda a, b: a + b, arr)

    orders = []

    increment = roundHalf((end1 - start1) / (n_tp - 1), inc)
    for i in range(n_tp):
        orders.append(
            {
                symbol: symbol,
                side: side,
                orderQty: math.floor((arr[i] / summ) * quantity),
                price: float((start1 + i * increment)),
                ordType: "Limit",
                text: "order",
            }
        )

    return orders


def Negative(quantity, n_tp, start, end, side, symbol):
    inc = 0.5 if symbol == "XBTUSD" else 0.05

    start1 = roundHalf(start, inc)
    end1 = roundHalf(end, inc)

    START_CFG = -1
    END_CFG = 1

    incrementQty = (END_CFG - START_CFG) / (n_tp - 1)

    arr = []
    for i in range(n_tp):
        arr.append(gaussian(1, START_CFG + i * incrementQty, 1))  # //mean == 1

    summ = functools.reduce(lambda a, b: a + b, arr)

    increment = roundHalf((end1 - start1) / (n_tp - 1), inc)

    orders = []
    for i in range(n_tp):
        #  //ROUND TO NEAREST 0.5
        orders.append(
            {
                symbol: symbol,
                side: side,
                orderQty: math.floor((arr[i] / summ) * quantity),
                price: float((start1 + i * increment)),
                ordType: "Limit",
                text: "order",
            }
        )

    return orders


def Normal(quantity, n_tp, start, end, side, symbol):
    inc = 0.5 if symbol == "XBTUSD" else 0.05

    start1 = roundHalf(start, inc)
    end1 = roundHalf(end, inc)
    START_CFG = -2
    END_CFG = 2

    incrementQty = (END_CFG - START_CFG) / (n_tp - 1)

    arr = []

    for i in range(n_tp):
        arr.append(gaussian(0, START_CFG + i * incrementQty, 1))  # //mean == 0

    summ = functools.reduce(lambda a, b: a + b, arr)

    increment = roundHalf((end1 - start1) / (n_tp - 1), inc)
    orders = []
    for i in range(n_tp):
        orders.append(
            {
                symbol: symbol,
                side: side,
                orderQty: math.floor((arr[i] / summ) * quantity),
                price: float((start1 + i * increment)),
                ordType: "Limit",
                text: "order",
            }
        )

    return orders


#   return orders
# }

# # /**
# #  * Setting one of the distributions
# #  */


def orders_distribution(distr, props):
    distro = {
        "uniform": Uniform,
        "positive": Positive,
        "negative": Negative,
        "normal": Normal,
    }
    return distro[distr](**props)

