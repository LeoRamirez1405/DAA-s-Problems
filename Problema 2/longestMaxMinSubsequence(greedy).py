def better(value, position, answer):
    # Check if the value is better for the given position
    if position % 2 == 1:
        return value < answer[position]
    return value > answer[position]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])  # Number of test cases
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])  # Length of the array for this test case
        index += 1
        
        array = list(map(int, data[index:index + n]))  # Read the array
        index += n
        
        count = [0] * (max(array) + 1)  # Frequency count of each number in the array
        answer = [0] * n  # Array to store the resulting subsequence
        in_answer = [False] * (max(array) + 1)  # Boolean array to check if a number is in the answer
        pointer = 0  # Pointer to the current position in the answer array
        
        # Count the frequency of each number in the array
        for num in array:
            count[num] += 1
        
        # Process each number in the array
        for num in array:
            count[num] -= 1  # Decrease the count as we process the number
            
            if pointer == 0:
                # If the answer array is empty, add the number
                answer[pointer] = num
                pointer += 1
                in_answer[num] = True
            else:
                if in_answer[num]:
                    # If the number is already in the answer, skip it
                    continue
                
                # Check if the current number can replace elements in the answer to form a better subsequence
                while ((pointer and count[answer[pointer - 1]] and better(num, pointer - 1, answer)) or
                       (pointer >= 2 and count[answer[pointer - 1]] and count[answer[pointer - 2]] and better(num, pointer - 2, answer))):
                    
                    if pointer and count[answer[pointer - 1]] and better(num, pointer - 1, answer):
                        in_answer[answer[pointer - 1]] = False
                        pointer -= 1
                    else:
                        in_answer[answer[pointer - 1]] = False
                        pointer -= 1
                        in_answer[answer[pointer - 1]] = False
                        pointer -= 1
                
                # Add the current number to the answer
                answer[pointer] = num
                pointer += 1
                in_answer[num] = True
        
        # Store the result for this test case
        results.append(f"{pointer}\n{' '.join(map(str, answer[:pointer]))}")
        
        # Reset the count and in_answer arrays for the next test case
        for num in array:
            count[num] = 0
            in_answer[num] = False
        pointer = 0
    
    # Print all results
    print("\n".join(results))

if __name__ == "__main__":
    main()