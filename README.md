# CrackCodeInterviewAndLeetcode

Welcome! This is Dayuan Tan's notes about the book "Crack the code interview, 6th edition".

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

## VII.  [Technical questions](7technicalQuestions.md)

### **7.1 How to Prepare**
1. **Try to solve the problem on your own**. 
2. **Write the code on paper**. 
3. **Test your code-on paper**. 
4. **Type your paper code as-is into a computer**. 

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



#### 7.2.2 Powers of 2 Table


<img src="./img/powersof2.png">

#### 7.3 Walking throught a problem

(这一节还是很吃惊的，没想到这个步骤是这样！一定要记住！)

1. **Listen to all information**
2. **Draw an example. special? Big enough?**
3. **Get a *brute-force* solution as soon as possible. State a naive algorithm and its ***runtime***, then optimize from there.**
4. **Optimize**. 确保使用了所有信息，尝试新的例子，手动走一遍，手动走一遍错例，Make a time vs. space tradeoff. Precompute information (reorganize data to save time in the long run). **Hash tables** are especially useful!
5. **Walk Through before coding!**
6. **Implement. Write beautiful code.** 
7. **TEST**. 概念测试，特值测试，数学/空node测试，小样例大样例测试。
8. **Keep talking!**

#### 7.4 Optimize & Solve Technique 
 - 1: Look for BUD
 - 2: DIY (Do It Yourself)
 - 2: DIY (Do It Yourself)
 - 2: DIY (Do It Yourself)
 - 5: Data Structure Brainstorm

-----

## VIII. The offer and beyond



------


## IX.   [Interview questions (IQs)](./IQs/9interviewQuestions.md)

**IQs sub-Part 1: Data structures**
  -  [Chap 1: Array and Strings](./IQs/9.1arraystring.md)
  -  Chap 2: Linked Lists
  -  Chap 3: Stacks and Quenes
  -  Chap 4: Trees and Graphs

**IQs sub-Part 2: Concepts and algorithms**
  -  Chap 5: Bit manipulation
  -  Chap 6: Math and Logic puzzles
  -  Chap 7: Object-oriented design
  -  Chap 8: Recurison and Dynamic Programming
  -  Chap 9: System Design and Scalability
  -  Chap 10: Sorting and searching
  -  Chap 11: Testing

**IQs sub-Part 3: Knowledge based**
  -  Chap 12: C and C++
  -  Chap 13: JAVA
  -  Chap 14: Databases
  -  Chap 15: Threads and Locks

**IQs sub-Part 4: Additional Review Problems**
  -  Chap 16: Moderate
  -  CHap 17: Hard