## Introduction to Compilers and Phases

**Introduction**

*   **What is a Compiler?** A compiler is a program that translates source code (written in a high-level language like C++, Java, etc.) into a different form, typically machine code or assembly language, that a computer can directly execute. It's essentially a language processor.
*   **Language Processors:**  Compilers are a type of language processor.
*   **Translation:** Compilers translate source code into target code. The target code can be in a lower-level representation (machine code or assembly language) for direct execution, or it can be an intermediate representation for further processing.

**Aho, Lam, Sethi and Ullman, “Compilers-Principles, Techniques & Tools”** – *Reference Book*

**Objectives:**

*   Understand and apply the principles of compiler design.
*   Develop system software tools & applications.

---

### The Structure of a Compiler

*   **Two Parts:** A compiler is divided into two main parts:
    *   **Analysis Part / Front-End:** Responsible for breaking down the source program into its constituent parts, checking for errors, and creating an intermediate representation.
    *   **Synthesis Part / Back-End:** Responsible for generating the target code based on the intermediate representation.
*   **Phases:** Compiler construction is typically divided into distinct phases.

---

### Phases of a Compiler

A pass reads an input file, processes it, and writes an output file. It can involve several phases.

**1. Lexical Analysis / Scanning:**

*   **Purpose:** Breaks down the source program into meaningful sequences called *lexemes*.
*   **Output:** Produces *tokens* – abstract symbols representing keywords, identifiers, operators, etc.
*   **Token Attributes:** Each token has an *attribute-value*, which often points to an entry in the symbol table.
*   **Example:** The source code `x = 10 + y;` would be tokenized into:  `identifier(x)`, `assign`, `number(10)`, `operator(+)`, `identifier(y)`, `separators(;)`

**2. Syntax Analysis / Parsing:**

*   **Purpose:** Determines if the syntax (structure) of the program is correct according to the language's grammar.
*   **Input:** Token stream from the lexical analyzer.
*   **Output:** A *parse tree* (or syntax tree) that represents the grammatical structure of the program.
*   **Example:** The parse tree for `x = 10 + y;` would show the assignment operation and its operands.

**3. Semantic Analysis:**

*   **Purpose:** Checks the source program for semantic consistency (meaningful relationships) – type checking, variable declarations, etc.
*   **Input:** Parse tree.
*   **Output:** Annotated parse tree or symbol table with type information.
*   **Type Checking:**  Ensures that operators are applied to compatible data types (e.g., you can't add a number to a string without a conversion).

**4. Intermediate Code Generation:**

*   **Purpose:** Creates a low-level, platform-independent representation of the program.
*   **Input:** Annotated parse tree.
*   **Output:** Intermediate Code (IC) – typically three-address code (TAC).
*   **Three-Address Code (TAC):** Uses instructions with three operands (e.g., `x = y op z`).

**5. Code Optimization:**

*   **Purpose:** Improves the intermediate code to generate more efficient target code.
*   **Input:** Intermediate Code.
*   **Output:** Optimized Intermediate Code.
*   **Types of Optimization:**
    *   *M/C Independent Optimization:*  Performed on the intermediate code, independent of the target machine.
    *   *M/C Dependent Optimization:* Performed on the intermediate code, considering the specific target machine's architecture.

**6. Code Generation:**

*   **Purpose:** Generates the target code (machine code or assembly language) from the optimized intermediate code.
*   **Input:** Optimized Intermediate Code.
*   **Output:** Target code.
*   **Process:** Involves register allocation and memory management.

---

### Grouping of Phases into Passes

*   A pass reads an input file, processes it, and writes an output file.
*   It can involve several phases.
*   **Front-End Phases:** Combined into a single pass.
*   **Code Optimization:** Optional pass.
*   **Back-End Phase:** Made into a pass.

---

### Symbol Table

*   **What is it?**  A data structure that stores information about identifiers (variables, constants, functions) used in the program.
*   **Accessed in Every Phase:** The symbol table is accessed by all phases of the compiler.
*   **Contents:** Attributes of variables (name, type, scope, etc.). Hash tables are often used for efficient lookup.

**Example Attributes:**

| Identifier | Name     | Type    | Scope   |
| ---------- | -------- | ------- | ------- |
| x          | variable | int     | global  |
| name       | variable | string | local  |
| pi         | constant | double  | global  |

---

### Error Detection and Reporting

*   **Done at Every Phase:**  Each phase checks for errors and reports them.
*   **Types of Errors:**
    *   *Lexical Error:* Misspelling an identifier or keyword (e.g., `Fi` instead of `if`).
    *   *Syntax Error:* An arithmetic expression with unbalanced parentheses (e.g., `(1 + 2`).
    *   *Semantic Error:*  Operator applied to incompatible operand types (e.g., `1 + "hello"`).
    *   *Logical Error:* Infinite recursive call.

---

### Differences Between Compiler and Interpreter

| Feature           | Compiler                               | Interpreter                            |
| ----------------- | -------------------------------------- | -------------------------------------- |
| Target Program     | Generates target program                | Does not generate target program       |
| Execution         | Executes the target program             | Executes operations specified by source |
| Error Handling    | Reports errors during compilation       | Reports errors during runtime          |
| Speed             | Generally faster                       | Generally slower                      |

---

### Intermediate Code (IC) Generation

*   **IC:** Low-level or machine-like intermediate representation.
*   **Purpose:**  To facilitate translation to the final target code.
*   **Properties:** Easy to produce, easy to translate into the target machine.

---

### References

*   Aho, Lam, Sethi and Ullman, “Compilers-Principles, Techniques & Tools”, Pearson/Addison-Wesley, Second Edition, 2013.
*   **Example:** *Generate the target machine code for the given expression*.

---

###  Text Book Reading:

*   Chapter 1
*   Section 1.1, 1.2

### Materials cover text book ch1 sections1.1and1.2

---

**Note:** Elakkiya, AP/CS – *Author*
## Rules

*   Use Markdown formatting.
*   Break the content into topics.
*   Whenever a new concept or idea appears, create a new heading.
*   Explain every concept clearly, using short definitions, examples, key points, and bullet lists.
*   Keep it concise but complete.
*   Add important formulas, definitions, and steps wherever necessary.
*   Use subheadings, bullets, and tables for clarity.

---

**Thank You**
