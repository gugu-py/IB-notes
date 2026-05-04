# CPU

### Components

Program Counter (PC)

Control Unit(CU)

ALU

Accumulators: general registers for storing temporary data during execution

Memory Address Register (MAR)

Memory Data Register (MDR)

Instruction Register (IR)

Data bus

Address bus

Control bus

### Execution Cycle

1. Fetch
	1. Program Counter points to next instruction's memory address to be carried out. Its value copied to MAR. PC increments by 1.
	2. Control bus sends READ signal; memory address bus sends the value in MAR to RAM; 
	3. Data is fetched to MDR via data bus
2. Decode
	1. Instruction is copied from MDR to IR
	2. Control unit's decoder decodes IR
3. Execute
	1. ALU carries out the instruction
4. Store (optional)
	1. Value to be stored copied to MDR; Memory address to store copied to MAR
	2. Control bus sends WRITE signal to memory via control bus
	3. Address (MAR) goes through address bus.
    4. Data (MDR) goes through data bus.
	5. Data is stored


# Operating System role

the function of OS in **primary memory management** is *allocation* of specific memory blocks to individual programs and *reallocation*

deadlock:

# Binary Operation

priority(precedence): NOT, AND , OR

## K-map

### ✅ **1. Set up the K-map**

- Choose the correct map size:
    
    - 2 variables → 2×2
        
    - 3 variables → 2×4
        
    - 4 variables → 4×4
        
- Label rows/columns in **Gray code order**, e.g.  
    `00, 01, 11, 10`.
    

---

### ✅ **2. Fill the K-map**

- If simplifying a Boolean expression:  
    Evaluate the expression for each input → place **1s** in the correct cells.
    
- If starting from a truth table:  
    Put **1s** where output is 1, **0s** where output is 0.  
    (You may also fill with **X** for don’t-cares.)
    

---

### ✅ **3. Group the 1s**

Rules for grouping:

- Groups must be **powers of 2**: 1, 2, 4, 8...
    
- Groups must be **rectangular**.
    
- Groups must be as **large as possible**.
    
- Groups can **wrap around** edges.
    
- Groups may **overlap** if helpful.
    

---

### ✅ **4. Write the simplified expression**

For each group:

- Look which variables **stay the same** inside the group → keep them.
    
- Variables that **change** within the group → eliminate them.
    

Examples:

- If A stays 1 → term includes `A`
    
- If B stays 0 → term includes `B'`
    
- If C changes → C gets eliminated
    

Combine all terms with OR (+).


## rules to simplify binary expressions


### **1. Identity Laws**

- $A + 0 = A$
    
- $A \cdot 1 = A$
    

### **2. Null (Dominance) Laws**

- $A + 1 = 1$
    
- $A \cdot 0 = 0$


### **3. Idempotent Laws**

- $A + A = A$
    
- $A \cdot A = A$
    

### **4. Complement Laws**

- $A + A' = 1$
    
- $A \cdot A' = 0$
    

### **5. Involution Law**

- $(A')' = A$
    

### **6. Absorption Laws**

These save you the **most** time.

- $A + AB = A$
    
- $A(A + B) = A$
    

### **7. Distributive Laws**

- $A(B + C) = AB + AC$
    
- $A + BC = (A + B)(A + C)$
    

### **8. De Morgan’s Laws**

- $(AB)' = A' + B'$
    
- $(A + B)' = A'B'$
    

### **9. Combining Terms**

- $AB + AB' = A$  
    (factor out $A$: $A(B + B') = A$)
    
- $A'B + AB = B$  
    (factor out $B$: $B(A' + A) = B$)
    

### **10. Consensus Theorem**

Very useful for removing extra terms.

- $AB + A'C + BC = AB + A'C$
    

The term $BC$ is redundant.

### **11. XOR Patterns**

- $A \oplus B = AB' + A'B$
    
- $A \oplus B = (A + B)(A' + B')$
    

### **12. XNOR Patterns**

- $A \odot B = AB + A'B'$  
    (“equal inputs give 1”)
    
