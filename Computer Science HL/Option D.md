**String**: DO NOT USE `==` to see if two strings are equal. Use `.equals(<String>)` instead.
**Inheritance**: a sub class extends from a super class; variables and methods of super class are shared
- promotes code reuse, as parent class holds common data and action
- reduces maintenance overhead, only update parent

**Polymorphism**: method of the same name as parent class can have different implementation

**Overload**: different parameters (or signature) -> static polymorphism
**Override**: New method with same name as its parent class -> dynamic, run-time polymorphism

**Abstract**: define a class that does not nessasarily have concrete implementation methods or fields.
**Interface**: a blueprint of class that specify must-have methods and fields. Use `implements` to use from Interface when building a new class.
Both Abstract and Interface can be used for **Polymorphism**

**aggregation:** include objects in a class as field, 'has a' relationship
- bad: increases dependencies
- good: better code responsibility (methods and fields are defined where they belong)
- good: promote code reuse

**composition**: 'part of' relationship

**Arraylist**: similar as `vector` in C++, using `.add(new_element)`, declare using `Arraylist<dataType> variable_name = new Arraylist<>(length=0)`.

![[Pasted image 20250512203526.png]]

**encapsulation**:
- Encapsulation places all attributes and methods that relate to a particular object/entity together;  
	- For example, `Payment` class includes attributes such as the food and drink arrays and methods such as `calculateBill()`;  
	- This provides a clearer view/understanding of each section of the problem;  
	- Which can lead to more efficient programming (faster, less errors etc.);
- Encapsulation protects the values of the data stored within the object **by using getters and setters**
	- From (accidental) changes made by other classes;  
	- For example, quantity in the `FoodItem` class cannot be altered through another variable called quantity in another class;  
	- This allows programmers to select any variable names they wish/no restriction on choice of variable names;

## UML diagram

public: +
private: -
static: underline
field name: type
method name (arg name: type): return type

![[_resources/Pasted image 20260224181608.png|307]]



## Algorithm

describing advantage:
- performance: memory/time
- human: code reuse/maintenance/complexity

**Improve Bubble Sort**: ^795d09
1. Include a flag “swapped”;  That can help stop the outer loop if there is a pass through the inner loop with no swap;  
2. Limit the inner loop by deducting the outer loop counter;  So that the sorted elements are no longer compared;

"Faster/slower" explanation:
- big O notation
- worst scenario


## Data Structure

%% use preorder to store/restore a binary search tree, other two dont work %%

feature of ADT (Abstract Data Type):
- No implementation details are known; The actions/methods are standard;

## Patches

`super`: call the super class/parent class's XXX method

ADT features:
1. dynamic memory allocation
2. fixed methods and fields
3. methods implementation is hidden from the user

In linked list, talk about **node** instead of 'element'

Talking about relationship(Inheritance, Dependency, etc.):
- XXX inherits/uses/... XXX (Instead of just Inheritance, Dependence, etc.)
- if more points: include definition and specifics (size, number, etc.)

please use `this` in class

Default constructor:
- A default constructor instantiates an object of a class;
- with null or default values (for the instance variables/attributes);
- without using any parameter;

Adding a new field to a class:
- new constructor and field
- new getter and setter

Talking about **Ethics**
- state obligation(main point), amplification(what the programmer can do, such as encryption), reason


use of ArrayList: do not use it unless you have to use it, since usually asks for "array"

talk about algorithm without code: must explicitly reference class methods



```java
// new list

House[] wishList = new House[10];

public int pay(int hours){
	return super.pay(hours)+hours*2; // call parent class's original method

```

---

**Running Java**:

```bash
javac *.java
java <class name>
```