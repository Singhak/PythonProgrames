MATRIX = [[0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]


def a_knows_b(a, b):
    return MATRIX[a][b]


def find_celebrity_stack(guestCount):
    # create a empty array which act as stack
    stack = []
    # push all guest in the stack (means all ids i.e 0 to guest count)
    for i in range(guestCount):
        stack.append(i)

    while len(stack) > 1:
        # now pick top two guest from stack
        guestA = stack.pop()
        guestB = stack.pop()
        # check guestA knows guestB
        # if guestA knows guestB then push back guestB into stack else push guestA
        if a_knows_b(guestA, guestB):
            stack.append(guestB)
        else:
            stack.append(guestA)

    if not len(MATRIX):
        return -1
    celebrity = stack.pop()

    # Now verify that last person in the stack is celebrity or not
    for i in range(guestCount):
        if i != celebrity and (a_knows_b(celebrity, i) or not a_knows_b(i, celebrity)):
            return -1

    return celebrity


def find_celebrity_graph(guestCount):
    # create two array for input and outpu of guests with initial value 0
    inputA = [0 for x in range(guestCount)]  # [0] * guestCount
    outputA = [0 for x in range(guestCount)]
    for i in range(guestCount):
        for j in range(guestCount):
            if a_knows_b(i, j):
                # if "a" knows "b" then value for "a" increement by 1 in inputA array
                # if "b" knows "a" then value for "a" increment by 1 in outputB array
                outputA[i] = outputA[i] + 1
                inputA[j] = inputA[j] + 1
    try:
        # if any index of inputA has value "guestCount - 1" then we will get index of that value
        # if at that index in outpuA array value should be "0" to qualify index as celebrity
        if inputA.count(guestCount - 1) == 1:
            # if (guestCount - 1) is more than 1 then there is no celebrity
            celebrity = inputA.index(guestCount - 1)
            if not outputA[celebrity]:
                return celebrity
        else:
            return -1
    except Exception as e:
        return -1


print(find_celebrity_graph(len(MATRIX)))
print(find_celebrity_stack(len(MATRIX)))
