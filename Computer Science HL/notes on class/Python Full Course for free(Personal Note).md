## Link to Video

https://uwccsc-my.sharepoint.com/:v:/g/personal/zxgu23_uwcchina_org/ETX4kw2AUBlCjx1jXHfqXOoBk-iUeaNY_rbnk9tK1sRbWQ?e=4gxsXg&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D

**key points explained**
- random number(function, variable, while loop, logical and maths operator, if statement, and many more)

**Project Overview**: 
- alarm clock(I hate pygame, use playsound instead. Need modification in source code)
- digital clock('the update method is quite different from the one I learnt before')
- stop watch(process and layout problem)
- Cake (Brand new tool, brand new exp)

**Personal Reflection**
- I learnt lots of new tools, its rewarding. But new tools get new bugs that I dont initially find solution, its challenging.
- In the future, I will implement Python to build websites using Flasks, Django, and FastAPI modules and connect them with my database. Also learn how to deploy the app on Google Cloud Run and learn about how the k8t works (roughly)


## Key Concepts explained

> Original tutorial link: https://www.youtube.com/watch?v=ix9cRaBkVe0&list=LL

**#1 Variables**: a container of a value, behaves as if the value it contains.

**#2 TypeCasting**: converting a variable from its datatype to another. Call init function does the job.

**#3 Userinput**: `input(<str: prompt, optional>)`, prompt user to enter data, return entered string.


**#6 Maths Operations**

`+-*` are all equivalent to reallife Maths. `/` produces decimal, while `//` produces integer. `%` means mod. `**` means power.

Add `=` after a basic operation operates itself. e.g. `a+=2` $\Leftrightarrow$ `a=a+2`. 

**Python does not support `a++`**, haha. Python doesn't support `a++` because it emphasizes simplicity and clarity. Instead, `a += 1` is used to avoid ambiguity, separating expressions from statements and aligning with its readable design philosophy. It really hates C++'s `++a++`. 

Use `math` lib to have more functions:
- consts: `math.e`, `math.pi`, etc.
- format: `.floor(x)`, `.ceil(x)`, round to nearest integer, or wanted decimal places(arg in second place)
- function: `.sqrt(x)`

Similar to `math.h` in C++.

**#7 `if` statement**: if the condition is true, then go into if; else go out.

**#11 logical operators**:

`or` = $\vee$

`and` = $\wedge$

`not` = $\neg$

**#12 conditional expression**

Also known as ternary operator. Its aim is to make your code shorter.

Syntax: `X if condition else Y`, similar to C++ `?condition X:Y`. Python seems more humane.

**#13 String Methods**

`.find(<target: string>)` return the index of the target(first occur) in the string, otherwise return `-1`

`.rfind(<target: string>)` return the index of the target(last occur) in the string, otherwise return `-1`

`.capitalize()` return capitalized

`.upper()` and `.lower()` uppercase or lowercase all chars.

`.isdigit()` return `True` if the string is a number, else return `False`

`.isalpha()` return `True` if the string is a word, else return `False`

`.count(<target: string>)` return the number of occur of target

`.replace(<target: string>, <result: string>)` return a string where targets are all replaced by result

other functions: `help(string)` to find more

**#14 Indexing**

syntax: `a[start:end:step length]`

`a` can be a string, list, or any indexable thing similar to list.

`start` and `end` are index, [start, end).

`step length` every n chars will be selected

indexes and step length can be negative, indicating from the opposite direction. e.g. `a[-1]` means the last element of `a`

**#15 formating**

Format specifiers in Python are used to control the way values are formatted and displayed. Similar to `C`'s `printf` methods. These are old fashion.

- **`:.Nf`**: Round to that many decimal places (fixed point)
  - Example: `:.2f` for two decimal places.
- **`:N`**: Allocate that many spaces
  - Example: `:5` to allocate 5 spaces.
- **`:0N`**: Allocate and zero pad that many spaces
  - Example: `:03` will pad with zeros up to 3 spaces.
- **`:<`**: Left justify
  - Example: `:<10` will left justify in a field 10 characters wide.
- **`:>`**: Right justify
  - Example: `:>10` will right justify in a field 10 characters wide.
- **`:^`**: Center align
  - Example: `:^10` will center align within 10 spaces.
- **`:+`**: Use a plus sign to indicate positive values
  - Example: `:+d` will add a `+` sign before positive integers.
- **`:=`**: Place the sign to the leftmost position
  - Example: `:=10` will place any signs on the left.
- **`: `**: Insert a space before positive numbers
  - Example: `: d` will insert a space before positive numbers.
- **`:,`**: Add a comma separator for large numbers
  - Example: `:,` will format a number with commas as thousand separators.


**#16 while loop**: execute the code and quit in certain condition.

**#12 For Loops:** A loop that iterates over a sequence (like a list, tuple, or string) and executes code for each item. Syntax: 

```
for item in sequence:
    <code>
```

**#13 Nested Loops:** A loop inside another loop. The inner loop executes completely for each iteration of the outer loop.

**#14 Lists, Sets, and Tuples:** Data structures that store multiple items. Lists are ordered and mutable, sets are unordered and unique, and tuples are ordered and immutable. Elements in these data structures can be different, like `[1, 'a', 1.0, (1,2)]`. Python achieves this by storing the memory cursor instead of assign actual consecutive memory like `C艹`.

**#15 2D Collections:** A collection of data organized into two dimensions, such as a list of lists or a matrix.

**#16 Dictionaries:** A data structure that stores key-value pairs. Syntax: {key: value}. Example: my_dict = {"name": "Alice", "age": 25}. It does not have order. The basic algorithm to achieve this data structure is hash.

**#17 Random Numbers:** Used to generate random values. `import random`, and `random.randint(left_bound, right_bound)`.



**#18 Functions:** Blocks of reusable code that perform a specific task. Defined using `def <function_name>(): <code>`. It also makes recursive functions possible. The only thing to pay attention is the variable name scope.

**#19 Default Arguments:** Function arguments that have default values. If the argument is not provided, the default value is used. 

**#20 Keyword Arguments:** Arguments passed to a function by explicitly specifying the name of the parameter. Example: `my_function(arg1=val1, arg2=val2)`.

**#21 \*args & kwargs:** `*args` allows passing a variable number of positional arguments, and `**kwargs` allows passing a variable number of keyword arguments to a function.

**#22 Iterables:** Objects that can be looped over, such as lists, tuples, and strings. Iterables are used in for loops.

**#23 Membership Operators:** Operators like `in` and `not in` used to check if an element exists within a sequence.

**#24 List Comprehensions:** A concise way to create lists using a single line of code. Syntax: `[expression for item in iterable if condition]`.

**#25 Match-Case Statements:** Similar to switch statements in other languages. Allows matching a value against multiple possible patterns.

**#26 Modules:** External files or packages containing functions, variables, and classes that can be imported into a program.

**#27 Scope Resolution:** Refers to the scope in which a variable is declared. Python uses the LEGB rule: Local, Enclosing, Global, Built-in.

**#28 `if name == 'main':`:** A condition used to check if a Python script is being run directly or imported as a module. Similar to the `main` function in `C艹`.

**#33 Python Object-Oriented Programming:** A programming paradigm that uses objects and classes. It supports concepts like inheritance, polymorphism, and encapsulation, using syntax `class`.

**#34 Class Variables:** Variables that are shared across all instances of a class. They are defined within a class but outside any methods.

**#35 Inheritance:** A mechanism in object-oriented programming where a class can inherit attributes and methods from another class.

**#36 Multiple Inheritance:** A feature where a class can inherit from more than one parent class.
If the inherited classes have attributes (functions or variables) with the same name, the method resolution order (MRO) determines which attribute will be used. In the parent classes from left to right, based on the order in which they are inherited.


**#37 super():** A built-in function used to call methods from a parent class. Commonly used in class inheritance.

**#38 Polymorphism:** The ability to define a function in different forms or to use the same operation in different contexts.

**#39 Duck Typing:** A programming concept where an object's behavior determines its type rather than its explicit class.

**#40 Static Methods:** Methods that belong to a class but do not require access to instance variables. Defined using `@staticmethod`.

**#41 Class Methods:** Methods that belong to the class itself and can modify class variables. Defined using `@classmethod`.

**#42 Magic Methods:** Special methods in Python with double underscores at the beginning and end, such as `__init__()` and `__str__()`. This is a kind of Overriding that is similar to overriding of operators in `C艹`. The name of this method is so confusing.

**#43 @property:** A decorator that allows defining methods as if they were attributes, providing a clean syntax for getter methods. This is a way that you can regulate the output/input/operation with the property variables. The name of the property method should be the same with the variable.

**#44 Decorators:** Functions that modify the behavior of other functions or methods. They are applied using the @ symbol.

**#45 Exception Handling:** The process of managing errors using try, except, and finally blocks to prevent crashes.

**#46 File Detection:** Methods to check if a file exists or detect its properties. Example: os.path.exists().

**#47 Writing Files:** Writing data to files using methods like open(), write(), and close().

**#48 Reading Files:** Reading data from files using methods like open(), read(), and readlines().

**#49 Dates & Times:** Managing date and time values using the datetime module, including formatting, arithmetic, and comparison.

**#51 threading**: create threads that run at the same time for multitasking

**#52 API**: Commonly used for fetching external data in real-time.

**#53 PyQt5 GUI Intro**: Introduction to building GUIs using PyQt5.

- **Syntax**: 
  ```python
  import sys
  from PyQt5.QtWidgets import QApplication, QWidget
  app = QApplication(sys.argv)
  window = QWidget()
  window.show()
  sys.exit(app.exec_())
  ```

**#54 PyQt5 Labels**: Creating and displaying text labels.

- **Syntax**:
  ```python
  from PyQt5.QtWidgets import QLabel
  label = QLabel('Hello, World!', parent)
  label.show()
  ```

**#55 PyQt5 Images**: Displaying images in the GUI.

- **Syntax**:
  ```python
  from PyQt5.QtGui import QPixmap
  image_label = QLabel(parent)
  pixmap = QPixmap('image.png')
  image_label.setPixmap(pixmap)
  image_label.show()
  ```

**56 PyQt5 Layout Managers**: Organizing widgets using layout managers.

- **Syntax**:
  ```python
  from PyQt5.QtWidgets import QVBoxLayout, QPushButton
  layout = QVBoxLayout()
  layout.addWidget(QPushButton('Button 1'))
  layout.addWidget(QPushButton('Button 2'))
  parent.setLayout(layout)
  ```

**#57 PyQt5 Buttons**: Creating buttons with click functionality.

- **Syntax**:
  ```python
  from PyQt5.QtWidgets import QPushButton
  button = QPushButton('Click Me', parent)
  button.clicked.connect(function_name)
  button.show()
  ```

**#58 PyQt5 Checkboxes**: Implementing checkboxes for user selection.

- **Syntax**:
  ```python
  from PyQt5.QtWidgets import QCheckBox
  checkbox = QCheckBox('Option', parent)
  checkbox.setChecked(True)
  checkbox.show()
  ```

**#59 PyQt5 Radio Buttons**: Using radio buttons for exclusive selection.

- **Syntax**:
  ```python
  from PyQt5.QtWidgets import QRadioButton
  radio_button = QRadioButton('Choice 1', parent)
  radio_button.setChecked(True)
  radio_button.show()
  ```

**#60 PyQt5 Line Edits**: Creating input fields for text entry.

- **Syntax**:
  ```python
  from PyQt5.QtWidgets import QLineEdit
  line_edit = QLineEdit(parent)
  line_edit.setPlaceholderText('Enter text...')
  line_edit.show()
  ```

**#61 PyQt5 CSS Styles**: Applying CSS styles to widgets.

- **Syntax**:
  ```python
  widget.setStyleSheet("background-color: lightblue; color: black;")
  ```

  > actually I dont really like pyqt5. It would be much better to use React.js to build very simple app with relatively better optimization. (Or even better to use Flask to build one with Database backend).