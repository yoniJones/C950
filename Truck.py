

v = [[1,1,1],[2,2],[3,3,3,3],[4]]
z = ["aa", 'bb', 'cc', 'dd']

b = [["d" for column in range(2)]
                      for row in range(5)]

c = [[[1,2,3,4,]for column in range(2)]
                      for row in range(5)]


graph = [[0 for column in range(v)]
                      for row in range(v)]




CM = [[0 for _ in range(3)]] * 10
n = 3
m = 4
a = [[for item in z] * m] * n
a[0][0] = 5
print(a)
