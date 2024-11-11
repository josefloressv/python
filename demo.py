def solution(A):
    if len(A) >=1 and len(A) <= 100000:
        A=list(set(A))
        print(A)
        solution = max(A)+1
        previous=A[0]
        for x in A:
            if x >= -1000000 and x <= 1000000:
                if x == previous:
                    continue
                print("x=%d previos+1=%d" % (x, previous+1))
                if x == (previous+1):
                    previous=x
                else:
                    solution=previous+1
                    break
            else:
                solution=None
                break
        if solution<=0:
            solution=1
        return solution

print (solution([1, 3, 6, 4, 1, 2])) # prints 5
#print (solution([1, 2, 3])) # prints 4
#print (solution([-1, -2])) # prints 1
#print (solution([-1, -3])) # prints 1