import multiprocessing

def square_list(mylist, result, square_sum):
    """
    worker function to square a given list

    inputs:
        mlist: []
        results: multiprocessing.Array()
        square_sum: multiprocessing.Value()

    """

    # append squares of mylist to result array
    for idx, num in enumerate(mylist):
        result[idx] = num*num

    # square_sum value
    square_sum.value = sum(result)

    # print result Array
    print("Result in child process: {}".format(result[:]))

    # print square_sum value
    print("Sum of squares in child process:{}".format(square_sum.value))

if __name__ == "__main__":
    # input_list
    mylist = [1,2,3,4]
    # creating Array of int data type with space for 4 integers
    result = multiprocessing.Array('i',4)

    #creating Value of int data type
    square_sum = multiprocessing.Value('i')

    # creating new process
    args_p1 = (mylist,result,square_sum)
    p1 = multiprocessing.Process(target=square_list, args = args_p1)

    #starting process
    p1.start()
    # wait until process is finished
    p1.join()

    print("\n-----------results in main-----------\n")
    # print result array
    print("Result in main process: {}".format(result[:]))

    # print square_sum value
    print("Sum of squares in main process: {}".format(square_sum.value))
