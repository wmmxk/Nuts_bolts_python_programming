"""
In this example, we try to print contents of global list, result, at two places:

    In the work function, square_list, Since, this function is called by process p1, result list is changed in memory space of process p1 only.

"""

import multiprocessing

result = []

def square_list(mylist):
    """
    worker function to square a given list
    """
    global result
    for i in mylist:
        result.append(i*i)
    print("Result in child process: {}".format(result))

if __name__=="__main__":
    #input list
    mylist = [1,2,3,4]

    #creating new process
    p1 = multiprocessing.Process(target=square_list, args=(mylist,))

    # starting process
    p1.start()

    #wait until process p1 is finished
    p1.join()

    print("Result in main program: {}".format(result))



