import sys
input = sys.stdin.read
from math import inf

def solve(n, array):
    # Inicializar la matriz dp con infinito
    dp = [[inf] * (n + 1) for _ in range(n + 1)]
    
    # Establecer la diagonal principal en 0
    for i in range(n + 1):
        dp[i][i] = 0
    
    # Rellenar la matriz dp
    for length in range(1, n + 1):
        for left in range(n - length + 1):
            if array[left] % 2 != (left + 1) % 2:
                continue
            if array[left] > left + 1:
                continue
            v = (left + 1 - array[left]) // 2
            
            right = left + length
            for mid in range(left + 1, right, 2):
                if dp[left + 1][mid] <= v:
                    new_val = max(v, dp[mid + 1][right] - (mid - left + 1) // 2)
                    dp[left][right] = min(dp[left][right], new_val)
    
    # Inicializar el array dp2
    dp2 = [0] * (n + 1)
    for i in range(n):
        dp2[i + 1] = dp2[i]
        
        for j in range(i):
            if dp[j][i + 1] <= dp2[j]:
                dp2[i + 1] = max(dp2[i + 1], dp2[j] + (i - j + 1) // 2)
    
    # Imprimir el resultado final
    print(dp2[n])

def main():
    input_data = input().split()
    T = int(input_data[0])
    index = 1
    for _ in range(T):
        n = int(input_data[index])
        array = list(map(int, input_data[index + 1:index + 1 + n]))
        index += 1 + n
        solve(n, array)

if __name__ == "__main__":
    main()