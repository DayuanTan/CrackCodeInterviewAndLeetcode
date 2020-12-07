# Part I strStr and Rabin-Karp. 
# Part 2 String 的坑.
# Part 3 Greedy Alg.

---

# String
大家会发现，在字符串问题中，我们用到了一些语言内置的函数。同时在字符串问题中也有很多常见的问题，接下来我们就来看一下这部分必须要知道的基础知识。

如果你使用 **Java 语言**，那么你首先要知道，Java 的 String 是一个类（Class），你需要知道如下的一些基本知识：
- 如何判断两个字符串相等
- 取出第 i 个字符以及字符串的遍历
- null 和 "" 的区别


## 其他语言

C++ 的 string 是一个类。

Python 的字符串是一个类。

接下来我们来看一下 String 题目中的常见问题。

首先我们来看一下如何判断两个字符串是否相等
代码
先来看一段java代码
```java
public class StringTest {  
    public static void main(String[] args) {
        String H = "hello";  
        String H_1 = H;  
        String H_2 = "hel";  
        String H_3 = H_2 + "lo";  
        String H_4 = H_2.concat("lo");  
              
        System.out.println(H);            // hello
        System.out.println(H_1);          // hello
        System.out.println(H_2);          // hel
        System.out.println(H_3);          // hello
        System.out.println(H_4);          // hello
        
        //==等号测试  
        System.out.println(H == H_1);     // true
        System.out.println(H == H_3);     // false
        System.out.println(H == H_4);     // false
        System.out.println(H_3 == H_4);   // false
              
        //equals函数测试  
        System.out.println(H.equals(H_1));   // true
        System.out.println(H.equals(H_3));   // true
        System.out.println(H.equals(H_4));   // true
        System.out.println(H_3.equals(H_4)); // true
              
        //StringBuilder测试  
        StringBuilder helloBuilder = new StringBuilder("hel");  
        System.out.println(helloBuilder.equals(H_2));    // false
   }   
}  
```
代码中注释为对应的结果。

## 为什么Java中不能直接用 == 判等？

Java中String类型具有一个equals的方法可以用于判断两种字符串是否相等，但是这种相等又与运算符“==”所判断的“相等”有所不同。

使用“==”判断的相等时指相同的内存地址，也就是同一个对象实例。

使用equals方法判断的相等在不同的对象中实现不同，意义也不同。

Java中所有的对象都继承自Object 类，在Object类中实现的equals() 方法如下：
```java
public boolean equals(Object obj) {  
    return (this == obj);  
} 
```
也就是等同于“==”, 只有在内存一样的时候才返回true。

- String类重写了这个方法，重写后的方法首先判断内存地址是否一致，如果一致返回true，否则比较字符串的内容是否一致，如果内容一致也返回true。因此，使用String类的equals方法是比较内容是否一致，而使用“==”是比较实例是否是同一个实例。

- StringBuilder类并没有重写equals方法，因此使用equals比较时，需要时同一个实例才会返回true。否则返回false。

# Java创建字符串的过程

在我们使用“=”赋值时，如果内存中已经有这个字符串，就会直接将其地址给这个变量，不会产生新的字符串。

如上面代码中的“H”与“H_1”， 二者指向同一个实例。

当我们使用“+”或者“concat”方法拼接字符串的时候，会创建一个新的字符串，占用新的内存空间，因此使用“==”判断时返回false。

# Java 中String的引用方式
```java
public class Hello {
    public static void main(String argv[]) {
        String sa = "abc";
        String sb = "abc";
        if (sa == sb) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
```
上面这段代码的结果是Yes。

程序运行的过程是这样，先在内存中创建字符串“abc”, 然后将地址的引用给了变量sa， 随后又把这个地址的引用给了sb。因此sa和sb引用的是同一段内存。

由于String类是一个不可更改的类。字符串不可被更改，所以这样的方式并不会产生问题。

# Python中判断字符串相等的方式

Python可以直接使用==判断字符串是否相等:
```python
s = "Hello"
s1 = s
s2 = "He"
s3 = "llo"
s4 = s2+s3

print(s)   # "Hello"
print(s1)  # "Hello"
print(s2)  # "He"
print(s3)  # "llo"
print(s4)  #  "Hello"

print(s == s1)  # True
print(s == s2)  # False
print(s == s3)  # False
print(s == s4)  # True
```
代码中的注释为运行结果。

# C++中判断字符串相等的方式

跟Python类似，C++也可以直接使用==比较字符串是否相等。
```c++
string s = "Hello";
string s1 = s;
string s2 = "He";
string s3 = "llo";
string s4 = s2+s3;

cout << s  << endl;  // "Hello"
cout << s1 << endl;  // "Hello"
cout << s2 << endl;  // "He"
cout << s3 << endl;  // "llo"
cout << s4 << endl;  //  "Hello"

cout << (s == s1) << endl;  // 1
cout << (s == s2) << endl;  // 0
cout << (s == s3) << endl;  // 0
cout << (s == s4) << endl;  // 1
```

---

## 接下来我们来看一下如何遍历字符串
# 如何遍历字符串

## Java:
```java
String s = new String("Hello");
for(int i = 0; i < s.length(); i++) {
    char c = s.charAt(i);
    // ....
}
```
使用上述方式来遍历Java中的字符串。

其中s.length() 获取字符串的长度。

String 不支持下标索引的方式访问，所以需要使用charAt(i)的方式访问对应位置的字符。同时也就没有办法使用下标的方式对String进行修改。

### **String是一种不可变类，字符串一但生成就不能被改变。** 
例如我们使用**‘+’进行字符串连接，会产生新的字符串，原串不会发生任何变化；使用replace()** 进行替换某些字符的时候也是产生新的字符串，不会更改原有字符串。

## Python:
```python
s = "Hello"
for i in range(len(s)):
    s[i].....
#另一种写法
for c in s:
    c......
```

使用上述方式来遍历python中的字符串。

其中len(s) 获取字符串的长度, 使用s[i]可以访问对应位置的字符。

### **Python中的字符串是不可变的，字符串一但生成就不能被改变，**
因此不能直接用s[i]=x的方式改变字符串。例如我们使用**‘+’进行字符串连接，会产生新的字符串，原串不会发生任何变化；使用replace()** 进行替换某些字符的时候也是产生新的字符串，不会更改原有字符串。

## C++:
```c++
string s = "Hello";
for (int i = 0; i < s.size(); ++i) {
    s[i] ...
}
// 或者
for (char c: s) {
    c...
}
// 跟上一种写法一样，但是此时改变c的值会同时改变原字符串
for (char& c: s) {
   c...
}
```

使用上述方式来遍历python中的字符串。

其中s.size() 获取字符串的长度, 使用s[i]可以访问对应位置的字符。


### **c++中的字符串是可变的，可以直接用s[i]=x的方式改变字符串。**

---

## 在字符串问题中，我们会看到null和"",但这两者有什么区别呢
# null和 "" 有什么区别

## null 表示空对象

Java中一切皆对象的思想，null用来表示空对象。我们不能对空对象做任何操作，除了"=" 和"=="。


java
```java
String s = null;
```
Python:
```python
s = None
```
C++:
```c++
string &p = *static_cast<string *>(nullptr);
```

## 空串
Java:
```java
String s = "";
```
Python:
```python
s = ""
s = str() # 等价于 s= ''
```
C++:
```c++
string s;
```
这个声明中，s不是空对象，是指向实实在在的堆内存的。只是这段内存中没有数据而已，s此时是个空串。
我们可以对s做所有字符串的操作。例如取长度、拼接、替换、查找字符等。

---
## 同时这里我总结了10个常见的字符串函数，也需要大家了解和掌握

## Java中
```java
String demo = "Hello,world!";
1.int length = demo.length(); //获取字符串的长度
2.boolean equals = demo.equals("Hello,world"); // 比较两个字符串相等
3.boolean contains = demo.contains("word"); // 是否包含子串
4.String replace = demo.replace("Hello,", "Yeah@"); // 将指定字符串(或正则表达式)替换，返回替换后的结果
5.char little = demo.charAt(5); // 查找字符串中索引为5的字符（索引从0开始）
6.String trim = demo.trim(); // 将字符串左右空格去除，返回去除空格后的结果
7.String concat = demo.concat("Great!"); // 拼接字符串，返回拼接结果
8.char[] charArray = demo.toCharArray(); // 返回该字符串组成的字符数组
9.String upperCase = demo.toUpperCase(); // 返回该字符串的大写形式
10.String lowerCase = demo.toLowerCase(); // 返回该字符串的小写形式
```

## Python中
```python
s = "Hello,World"
1.print(s[1]) # 'e', 取出某个位置的字符
2.print(s[1:6]) # 'ello,' ，字符串切片
3.print(len(s)) # 11, 返回字符串的长度
4.print("e" in s) # True, 返回字符是否在字符串中
5.print(s.lower()) # 'hello,world', 将字符串所有元素变为小写
6.print(s.upper()) # 'HELLO,WORLD', 将字符串所有元素变为大写
7.s += '...' # Hello,World... ，字符串拼接，在字符串后拼接另一个字符串
8.print(s.find('lo')) # 3, 返回第一次找到指定字符串的起始位置（从左往右找）
9.print(s.swapcase()) # hELLO,wORLD..., 将大小写互换
10.print(s.split(',')) # ['Hello', 'World...'], 将字符串根据目标字符分割
```

---

看完了以上的字符串问题，我们再来看一下一个很多同学提到的算法，贪心算法。我们究竟是否有必要专门练习贪心算法呢.

许多同学问我，为什么课程中没有包含贪心算法(Greedy)，是否可以将贪心算法列入教学计划中。每一次我总是苦口婆心的规劝他们：不要把时间浪费在贪心法上，学了根本没有用。

为什么学习贪心法没有用？这是一个值得讨论的问题。从我看来，有如下的三个方面的原因：

- 你能想到的贪心法都是错误的
- 面试基本不会考
- 没有通用性
- 
接下来，我来逐个给大家解释一下这三个原因。

1. 你想得到的贪心法，都是错的。
  
首先我们需要知道，什么是贪心法。贪心法就好比挑老公时，只看他当前是不是腰缠万贯，不看他未来是否飞黄腾达。而其他的一些算法如动态规划，就好比你通过仔细的调查，发现虽然他现在是一个穷小子，但是是因为身为富二代的他不愿意接受父亲安排，自己出来独自闯荡，但是未来终究要继承千亿家业。

因此，贪心法可以说，是一种目光短浅的算法。一般在算法问题中，可以使用贪心算法的问题，其贪心策略往往都比较复杂，一般人是想不到的。而你容易想到的那些贪心策略，往往都是错的。

举一个实际的例子：

求图中A点到B点的最短路径（点与点之间的距离是正整数）。

- 错误的贪心策略：

从A出发，选择里A最近的点X，走到X，然后选择离X最近的点Y，走到Y...

- 正确的贪心策略（Dijkstra算法）：

使用hashmap distance = {} 记录所有点到起点A的最短距离。一开始 distance = {A: 0}，代表目前只有A离起点的最短距离我们是确定知道的。然后在Distance中的点和非distance中的点中找到最小的一对X,Y, 使得 distance[X] + (X到Y的直接连接距离) 最小。其中X在distance里（已经被确认找到了最短距离），Y不在distance里（还没有被确认找到了最短距离）。然后将Y加入distance，并把距离设为 distance[X] + (X到Y的直接连接距离）。

怎么样，正确的贪心算法是不是非常复杂？

2. 面试基本不会考


贪心法的问题，面试基本不会考，因为等同于考智力题或者是背诵题。一个面试官想要自己凭空创造出一个面试题是使用贪心算法的，是非常困难的。（参见LintCode上的贪心算法的题目所占比例可知）。既然如此，如果面试中被问到了贪心算法，那么一定是一道经典的贪心问题，这类问题，我们可以称之为背诵题。因为大多数同学（除了智商很高，或者有算法竞赛经历的那一批），是不可能在面试的时候想得出解法的。

举几个例子：加油站问题 [Gas Station](https://www.lintcode.com/problem/gas-station/description)，这个题的做法是，从任意站点出发，走一圈，找到这一圈里剩余Gas最少的那一站，然后从这一站出发走一圈，如果在这一站出发可以顺利走完全程，那么就可以行，否则就不可行。像这样的算法，是需要进行数学证明来证明其正确性的，面试官是没有能力出这样的面试题的。

从另外一个角度来说，贪心算法的题，对于程序的实现能力要求并不高，也违背了公司通过算法题面试主要是希望考察大家的程序实现能力这一点。所以面试官和公司也都不倾向于将贪心算法作为面试的算法问题。

1. 没有通用性
   
二分法，动态规划算法，分治算法，搜索算法等等，很多的算法都是具有通用性的。也就是说，在题目A里，你用了这个算法，在其他的题目B里，你可能完全可以用一样的算法和思路去解决。

而贪心法，他不是“一个算法”，而是“一类算法”的统称，他更多的是一种高屋建瓴的算法思想，而不是具体实施的算法步骤。所以基本的情况就是，你在题目A里用了某个贪心算法解决了这个问题，然后这个题中用到的贪心法，永远也找不到第二个题用类似的方法来解决。

每个题是完全独立的且没有任何联系，这对于学习者来说，无非是背诵越多知道的越多。无法触类旁通，无法举一反三。因此将时间浪费在贪心法上的话，只能是吃力不讨好。

当然，面试中也不是说完全不可能碰到贪心算法，只是几率非常的小，你只需要“背诵”如下的一些几个题的贪心解法就好了：
http://www.jiuzhang.com/qa/2099/

已解决问题
几个必须“背诵”的贪心算法题:


http://www.lintcode.com/problem/majority-number/

http://www.lintcode.com/problem/create-maximum-number/

http://www.lintcode.com/problem/jump-game-ii/

http://www.lintcode.com/problem/jump-game/

http://www.lintcode.com/problem/gas-station/

http://www.lintcode.com/problem/delete-digits/

http://www.lintcode.com/problem/task-scheduler/