import random


take = 5
see = 50
N = 100000


def main():

    V = {(1,1): 0}

    def value(left_to_take: int, left_to_see: int):

        if (left_to_take, left_to_see) in V:
            return V[left_to_take, left_to_see]
        elif left_to_take == left_to_see:
            V[(left_to_take, left_to_see)] = 0
            return 0
        else:
            if left_to_see <= 1:
                V_pass = 0
                V_take = 0
            else:
                V_pass = value(left_to_take, left_to_see - 1)
                if left_to_take <= 1:
                    V_take = 0
                else:
                    V_take = value(left_to_take - 1, left_to_see - 1)

            print(f"Calculating for {(left_to_take, left_to_see)}")
            print(f"len(V)={len(V)}")
            sample_sum = 0
            for i in range(N):
                sample_sum += max(random.gauss(0, 1) + V_take, V_pass)
            v = sample_sum / N
            V[(left_to_take, left_to_see)] = v
            return v

    print(f"V: {V}")
    print(f"Taking {take} out of {see}, the value is: {value(take, see)}")
    print(f"V: {V}")


if __name__ == '__main__':
    main()