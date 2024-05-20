if __name__ == '__main__':
    n = int(input())
    input_string = input()
    input_list = input_string.split()
    nums = [int(num) for num in input_list]
    
    first_max = max(nums)
    nums.sort()
    second_max = nums[0]
    for i in range(n):
        if nums[i] != first_max:
            second_max = max(second_max, nums[i])
    print(second_max)
