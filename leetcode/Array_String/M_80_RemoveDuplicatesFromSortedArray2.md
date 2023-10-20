
Hint: keep an index variable that points to the position where <mark>the next unique element should be placed</mark>.

Time Complexity: O(N)

```java
Java:

public int removeDuplicates(int[] nums) {
    if(nums.length <= 2)
        return nums.length;

    int index = 2;
    int i = 2;
    while(i < nums.length) {
        if(nums[i] != nums[index - 2]) {
            nums[index] = nums[i];
            index++;
        }
        i++;
    }
    return index;
}

Py:

def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) <= 2 :
        return len(nums)

    index = 2
    i = 2
    while i < len(nums) :
        if nums[i] != nums[index-2] :
            nums[index] = nums[i]
            index = index + 1
        i = i + 1
    return index
```