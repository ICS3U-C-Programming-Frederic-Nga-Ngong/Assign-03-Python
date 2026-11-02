#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Solves a quadratic equation.

import math


def main():
    a_str = input("Enter the value of a : ")
    b_str = input("Enter the value of b : ")
    c_str = input("Enter the value of c : ")

    try:
        a = int(a_str)
        try:
            b = int(b_str)
            try:
                c = int(c_str)
                choice = input(
                    "Is this your equation : {}x**2 + {}x + {} = 0 \n".format(a, b, c)
                )
                match choice:
                    case "yes":
                        discriminant = (b**2) - (4 * a * c)
                        if discriminant > 0 and b == 0 and c < 0:
                            x = math.sqrt(-1 * (c / a))
                            y = math.sqrt(-1 * (c / a))
                            print(
                                "The answers to your equation are -{} and +{}".format(
                                    x, y
                                )
                            )

                        elif discriminant > 0:
                            x = (-b + math.sqrt(discriminant)) / (2 * a)
                            y = (-b - math.sqrt(discriminant)) / (2 * a)
                            print(
                                "the answers to your equation are {} and {}".format(
                                    x, y
                                )
                            )

                        elif discriminant == 0:
                            x = -b / (2 * a)
                            print("The only answer to your equation is {}".format(x))

                        else:
                            print(
                                "Sorry, your equation has no real root according to math"
                                " since square root of negative number is"
                                " not in the set of integers."
                            )

                    case "no":
                        print("Please enter a new equation then.")

                    case _:
                        print("Again, please respond with either yes or no")

            except ValueError:
                print(
                    "Sorry, {} is not a valid integer. Please, enter a valid integer".format(
                        c_str
                    )
                )
        except ValueError:
            print(
                "Sorry, {} is not a valid integer. Please ,enter a valid one".format(
                    b_str
                )
            )
    except ValueError:
        print(
            "Sorry, {} is not a valid integer. Please, enter a valid one".format(a_str)
        )


if __name__ == "__main__":

    main()
