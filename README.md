# CrackCodeInterviewAndLeetcode

The book PDF is available [here](./book/Cracking%20the%20Coding%20Interview%206th%20Edition%20189%20Programming%20Questions%20and%20Solutions.pdf). Please buy it from Amazon or other bookstores if you like it.

Ref: Official [github](https://github.com/DayuanTan/CtCI-6th-Edition).

------
I split this book into 2 parts. 

**Part 1** includes:
- Introduction
- I.    The interview process
- II.   Behind the scenes
- III.  Special Situations
- IV.   Before the interview
- V.    Behavioral questions
- VI.   Big O
- VII.  Technical questions
- VIII. The offer and beyond

**Part 2** includes:
- IX.   Interview questions (IQs)
  -  **IQs sub-Part 1: Data structures**
  -  Chap 1: Array and Strings
  -  Chap 2: Linked Lists
  -  Chap 3: Stacks and Quenes
  -  Chap 4: Trees and Graphs
  -  **IQs sub-Part 2: Concepts and algorithms**
  -  Chap 5: Bit manipulation
  -  Chap 6: Math and Logic puzzles
  -  Chap 7: Object-oriented design
  -  Chap 8: Recurison and Dynamic Programming
  -  Chap 9: System Design and Scalability
  -  Chap 10: Sorting and searching
  -  Chap 11: Testing
  -  **IQs sub-Part 3: Knowledge based**
  -  Chap 12: C and C++
  -  Chap 13: JAVA
  -  Chap 14: Databases
  -  Chap 15: Threads and Locks
  -  **IQs sub-Part 4: Additional Review Problems**
  -  Chap 16: Moderate
  -  CHap 17: Hard
- X.    Solutions
- XI.   Advanced Topics
- XII.  Code Library  
- XIII. Hints

-----

# Notes:

## I.    The interview process

### 1.1 Few points I think it's worth paying attention to
1. Algorithm and coding problems form the largest component of the interview process. Usually you get through 1 question.

2. You **should** do your best to **talk out loud** throughout the problem and **explain** your thought process. 
    
   - Your interviewer might jump in sometimes to help you; let them. It's normal and doesn't really mean that you're doing poorly. (That said, of course not needing hints is even better.)

3. Need to do few hard problems, so can be good at developing optimation problems.

4. Basic data structure and algorithm knowledge is important.

5. Practice writing code using whiteborad and speak more and explain their thought process.
6. Your interviewer develops a feel for your performance by **comparing** you to other people.


### 1.2 Assessment

Rather, your interviewer will make an **assessment of your performanc**e, usually based on the following:

- **Analytical skills:** Did you need much help solving the problem? How optimal was your solution? How long did it take you to arrive at a solution? If you had to design/architect a new solution, did you structure the problem well and think through the tradeoffs of different decisions?

- **Coding skills:** Were you able to successfully translate your algorithm to reasonable code? Was it clean and well-organized? Did you think about potential errors? Did you use good style?

- **Technical knowledge / Computer Science fundamentals:** Do you have a strong foundation in computer science and the relevant technologies?

- **Experience**: Have you made good technical decisions in the past? Have you built interesting, challenging projects? Have you shown drive, initiative, and other important factors?

- **Culture fit / Communication skills:** Do your personality and values fit with the company and team? Did you communicate well with your interviewer?

------

## II.    Behind the scenes

### 1.1 Few points I think it's worth paying attention to
1. The "screening" interview often involves coding and algorithms questions, and the bar can be just as high as it is for in-person interviews.
2. If you're unsure whether or not the interview will be technical, ask your recruiting coordinator what position your interviewer holds (or what the interview might cover). An engineer will usually perform a technical interview.
3. Methods can be:
   - online synchronized document editors
   - write code on paper and read it back over the phone
   - "homework" to solve after you hang up the phone
   - email them the code you wrote
4. Usually 1 or 2 screening interviews before on-site.
5. In an **on-site** interview round, you usually have **3 to 6 in-person** interviews. One of these is often over lunch. The lunch interview is usually not technical, and the interviewer may not even submit feedback. This is a good person to discuss your interests with and to ask about the company culture. Your other interviews will be mostly technical and will involve a combination of coding, algorithm, design/architecture, and behavioral/experience questions.

This chapter also includes specific suggestions for interviews of 
- Microsoft
- Amazon
- Google 
- Apple
- Facebook
- Palantir
  
So make sure check them before your interviews.

------

## III.  Special Situations

------


## VI.   Big O

Very important! Big O time is the language and metric we use to describe the efficiency of algorithms.

------

## VII.  Technical questions

### **7.1 How to Prepare**

Many candidates just read through problems and solutions. That's like trying to learn calculus by reading a problem and its answer. You need to practice solving problems. Memorizing solutions won't help you much.

For each problem in this book (and any other problem you might encounter), do the following:

1. **Try to solve the problem on your own**. Hints are provided at the back of this book, but push yourself to develop a solution with as little help as possible. Many questions are designed to be tough-that's okay! When you're solving a problem, make sure to think about the space and time efficiency.

2. **Write the code on paper**. Coding on a computer offers luxuries such as syntax highlighting, code completion, and quick debugging. Coding on paper does not. Get used to this-and to how slow it is to write and edit code-by coding on paper.

3. **Test your code-on paper**. This means testing the general cases, base cases, error cases, and so on. You'll need to do this during your interview, so it's best to practice this in advance.

4. **Type your paper code as-is into a computer**. You will probably make a bunch of mistakes. Start a list of all the errors you make so that you can keep these in mind during the actual interview.

In addition, try to do as many mock interviews as possible. You and a friend can take turns giving each other mock interviews. Though your friend may not be an expert interviewer, he or she may still be able to walk you through a coding or algorithm problem. You'll also learn a lot by experiencing what it's like to be an interviewer.

### **7.2 Baseline of knowledge**

#### 7.2.1 Core Data Structures, Algorithms, and Concepts

A list of the absolute, **must-have** knowledge:

|Data Structures|Algorithms|Concepts|
|-|-|-|
||
|Linked Lists|Breadth-First Search|Bit Manipunation|
|Trees, Tries & Graphs|Depth-First Search|Memory (Stack vs. Heap)|
|Stacks & Queues|Binary Search|Recursion|
|Heaps|Merge Sort|Dynamic Programming|
|Vectors / ArrayLists|Quick sort|Big O Time & Space|
|**Hash Tables**|||
||

For each of these topics, make sure you understand how to use and implement them and, where applicable, the space and time complexity.

In particular, **hash tables** are an extremely important topic. Make sure you are very comfortable with this data structure.

#### 7.2.2 Powers of 2 Table

The table below is useful for many questions involving **scalability** or any sort of **memory limitation**. Memorizing this table isn't strictly required, but it can be useful. You should at least be comfortable deriving it.

<img src="./img/powersof2.png">

#### 7.2.3 Walking throught a problem

(这一节还是很吃惊的，没想到这个步骤是这样！一定要记住！)

1. **Listen to all information**
   - Mentally recorded any unique information in the problem.
   - If you stuck, ask yourself if use all information.
2. **Draw an example. special? Big enough?**
    You want to create an example that is:
   - Specific. It should use real numbers or strings (if applicable to the problem).
   - Sufficiently large. Most examples are too small, by about 50%.
   - Not a special case. Be careful. It's very easy to inadvertently draw a special case. If there's any way your example is a special case (even if you think it probably won't be a big deal), you should fix it.
3. **Get a *brute-force* solution as soon as possible. State a naive algorithm and its ***runtime***, then optimize from there.**
4. **Optimize**. 确保使用了所有信息，尝试新的例子，手动走一遍，手动走一遍错例，Make a time vs. space tradeoff. Precompute information (reorganize data to save time in the long run). **Hash tables** are especially useful!
5. **Walk Through before coding!**
   - Make sure that you get it as close to "perfect" in the beginning as possible.
6. **Implement. Write beautiful code.** 
   Beautiful code means:
   - Modularized code. Just pretend you have a function initIncrementalMatrix (int size). Fill in the details later if you need to.
   - Error checks. Add a todo and then just explain out loud what you'd like to test.
   - Use other classeslstructs where appropriate. Return a StartEndPair (or possibly Range) objects instead of a 2-dimentional array.Just pretend it exists and deal with the details later if you have time.
   - Good variable names.
   - If you see something you can refactor later on, then explain this to your interviewer and decide whether or not it's worth the time to do so.
   - If you get confused (which is common), go back to your example and walk through it again.
7. **TEST**. 概念测试，特值测试，数学/空node测试，小样例大样例测试。
   - Start with a "conceptual" test. A conceptual test means just reading and analyzing what each line of code does. Think about it like you're explaining the lines of code for a code reviewer. Does the code do what you think it should do?
   - Weird looking code. Double check that line of code that says x = length - 2. Investigate that for loop that starts at i = 1. While you undoubtedly did this for a reason, it's really easy to get it just slightly wrong.
   - Hot spots. You've coded long enough to know what things are likely to cause problems. Base cases in recursive code. Integer division. Null nodes in binary trees. The start and end of iteration through a linked list. Double check that stuff.
   - Small test cases. This is the first time we use an actual, specific test case to test the code. Don't use that nice, big 8-element array from the algorithm part. Instead, use a 3 or 4 element array. 1t'lIlikely discover the same bugs, but it will be much faster to do so.
5. Special cases. Test your code against null or single element values, the extreme cases, and other special cases.
8. **Keep talking!**

