Hint: Sort, then Group

Time Complexity: O(n * m * log(m))

```java

public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, ArrayList<String>> map = new HashMap<>();

    for(int i = 0; i < strs.length; i++) {
        String current = strs[i];

        // sort the string
        char charArray[] = current.toCharArray();
        Arrays.sort(charArray);
        String sortedString = new String(charArray);

        if(map.get(sortedString) == null) {
            ArrayList<String> list = new ArrayList<String>();
            list.add(current);
            map.put(sortedString, list);
        } else {
            map.get(sortedString).add(current);
        }
    }
    return map.values().stream().collect(Collectors.toList());
}
```