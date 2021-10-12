def pipes(arr,n):
    temp = arr[0]
    for i in range(1,n):
        if arr[i] > temp:
            print(arr[i],end = ' ', sep = '')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    pipes(arr,n)
