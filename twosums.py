# two sums algo challenge on leetCode.com my solution
def twoSum(nums: list[int], target: int) -> list[int]:

    for i, j in enumerate(nums):
        x = 0
        for k ,l in enumerate(nums):

            if k == i:
                pass
            else:
                if j + l == target:
                    return [i, k]



if __name__ == "__main__":

    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))