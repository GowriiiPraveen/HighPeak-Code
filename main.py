# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def soln(n, arr):
    arr.sort(key=lambda x: x[2], reverse=True)
    count = 0
    earns = 0
    end = 0
    #print(arr)
    for i in range(n):
        if arr[i][0] >= end:
            count += 1
            end = arr[i][1]
            #print(n,count,earns)
        else:
            earns += arr[i][2]

    return n - count, earns


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = int(input("Enter the number of Jobs: "))
    arr = []
    print('Enter job start time, end time, and earnings')
    for i in range(n):
        a=int(input())
        b=int(input())
        c=int(input())
        arr.append((a, b, c))

    result = soln(n, arr)
print("The number of tasks and earnings available for others")
print("Tasks:", result[0])
print("Earnings:", result[1])