#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Solves a quadratic equation.

import math


def main():

    # Get a,b and c.
    a_str = input("Enter the value of a : ")
    b_str = input("Enter the value of b : ")
    c_str = input("Enter the value of c : ")

    # Checks if a,b and c are integers
    try:
        a = int(a_str)
        try:
            b = int(b_str)
            try:
                c = int(c_str)

                # Ask the user if the values are the one he wants
                choice = input(
                    "Is this your equation : {}x**2 + {}x + {} = 0 \n".format(a, b, c)
                )
                if choice == "yes":

                    # Calculates discriminant
                    discriminant = (b ** 2) - (4 * a * c)

                    # Checks various conditions including the discriminant
                    if discriminant > 0 and b == 0 and c < 0:
                        x = math.sqrt(-1 * (c / a))
                        y = math.sqrt(-1 * (c / a))
                        print(
                            "The answers to your equation are -{} and +{}".format(x, y)
                        )

                    elif discriminant > 0:
                        x = (-b + math.sqrt(discriminant)) / (2 * a)
                        y = (-b - math.sqrt(discriminant)) / (2 * a)
                        print("the answers to your equation are {} and {}".format(x, y))

                    elif discriminant == 0:
                        x = -b / (2 * a)
                        print("The only answer to your equation is {}".format(x))

                    else:
                        print(
                            "Sorry, your equation has no real root according to math"
                            " since square root of negative number is"
                            " not in the set of integers."
                        )

                elif choice == "no":
                    print("Please enter a new equation then.")

                else:
                    print("Again, please respond with either yes or no")

            # Returns error if either a, b or c are not valid integers.
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
