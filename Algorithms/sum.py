def sum_cal(a):

    if a ==0:

        return 0

    else:

        return a + sum_cal(a-1)



print(sum_cal(8))