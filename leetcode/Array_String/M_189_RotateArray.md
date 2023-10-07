Org: 1  2  3    4 5  6  7 8 9 10 11 12 13 14   k = 3

Res: 12 13 14   1 2  3  4 5 6  7 8  9  10 11

Pattern :
- reverse original
- reverse first [0 ~ k - 1]
- reverse second [k, size - 1]

Time Complexity: O(N)

```java

public void rotate(int[] nums, int k) {
    int size = nums.length;
    //k can be larger than size
    int steps = k % size;   

    reverse(0, size - 1, nums);
    reverse(0, steps - 1, nums);
    reverse(steps, size - 1, nums);
    
}

private void reverse(int i, int j, int[] nums) {
    while(i < j) {
        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;
        i++;
        j--;
    }
}

```


