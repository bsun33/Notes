Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

```java 
            data    mins
push -2     -2      -2
push 0      0       -2
push -3     -3      -3
getMin              -3
pop         
getMin              -2

class MinStack {
    // keep track of a list of pushed elements
    private Stack<Integer> data;
    // for each element in data, keep track of min element so far
    private Stack<Integer> mins;

    public MinStack() {
        data = new Stack<Integer>();
        mins = new Stack<Integer>();
    }
    
    public void push(int val) {
        data.push(val);
        if (mins.isEmpty()) {
            mins.push(val);
        }
        else {
            mins.push(Math.min(val, mins.peek()));
        }
    }
    
    public void pop() {
        data.pop();
        mins.pop();
    }
    
    public int top() {
        return data.peek();
    }
    
    public int getMin() {
        return mins.peek();
    }
}
```

```java
用内部类定义一个Node(里面保存当前min)来实现Stack

class MinStack {
    class Node{
        int val;
        int min;
        Node next;
    
        Node(int val, int min, Node next){
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }
    
    private Node cur = null;
    
    public MinStack() {
    }
    
    public void push(int val) {
        if(cur == null)
            cur = new Node(val, val, null);
        else {
            Node newNode = new Node(val, Math.min(val, cur.min), cur);
            cur = newNode;
        }
    }
    
    public void pop() {
        cur = cur.next; 
    }
    
    public int top() {
        return cur != null ? cur.val : 0;
    }
    
    public int getMin() {
        return cur != null ? cur.min : 0;
    }
}
```