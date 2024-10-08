#Arrays will be in the OOP's concept


import streamlit as st
import streamlit_antd_components as sac
import pandas as pd

# Set page config
st.set_page_config(
    page_title="chin Tapak dam dam",
    page_icon=":book:",
    layout="wide",
)

#Tab Menu
selecteds = sac.tabs([
    sac.TabsItem(label='Home', tag=""),    
    sac.TabsItem(label='Python', icon=''),
    sac.TabsItem(label='C', icon=''),
    sac.TabsItem(label='C++', icon=''),
    sac.TabsItem(label='Java', icon=''),
    sac.TabsItem(label='',tag="IDE"),

], align='wide', size='lg' , color='grape', use_container_width=True, return_index=True)



#Home Section
if selecteds == 0:
    st.header("Welcome to Chin Tapak Dam Dam")
    st.subheader("Directly go the python for learning {others things are work in progress}")
    st.info("Preferred device are laptop, but if You are a Phone user so when You click on Python You will see a right facing arrow on the top left click to openup the menu. ")
    st.success("Thank You for visiting our web Appliction.")
           

if selecteds == 5:    
    import io
    import sys
    
    st.title("Code Compiler")
    
    # Create input and output text areas
    input_code: str = st.text_area("Enter your code:", height=300)
    output_area_placeholder = st.empty()
    
    # Create a button to compile and run the code
    run_button: bool = st.button("Run Code")
    
    # Define a function to compile and run the code
    def compile_and_run(code: str) -> None:
        try:
            # Redirect output to a string
            old_stdout: io.TextIOWrapper = sys.stdout
            new_stdout: io.StringIO = io.StringIO()
            sys.stdout = new_stdout
            exec(code)
            sys.stdout = old_stdout
            output: str = new_stdout.getvalue()
            output_area_placeholder.text_area("Output:", value=output.strip(), height=300)
        except Exception as e:
            st.error(f"Error: {e}")
    
    # Run the code when the button is clicked
    if run_button:
        compile_and_run(input_code)



#Python Tab Section
if selecteds == 1:
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Introduction', icon='house-fill'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Basics', icon='box-fill', children=[
                sac.MenuItem('First Program'),
                sac.MenuItem('Syntax & Basic'),           
                sac.MenuItem('Variable'),
                sac.MenuItem('Input and Output'),
                sac.MenuItem('Data Types'),
                sac.MenuItem('Operators'),
                sac.MenuItem('Conditional Statement'),
                sac.MenuItem('Loops'),
                sac.MenuItem('Function'),
            ]),
            sac.MenuItem('Cheatsheet', icon='table'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('Download Python', icon='download', description='Latest Version', href='https://www.python.org/downloads/'),
                sac.MenuItem('Download VS Code', icon='terminal', href='https://code.visualstudio.com/download'),
            ]),
        ], size='lg', variant='left-bar', color='grape', open_all=True, return_index=True)
    
    if selected == 0:
        st.header("Welcome to Python")
        # App title
        st.title("Python Overview")
        
        # Introduction
        st.markdown("""
        - Python was designed and implemented by Guido van Rossum. Its journey began as a hobby in the winter months of 1989.
        - Python is a high-level, general-purpose programming language known for its simplicity, readability, and versatility. It's widely used in various fields, including web development, data science, machine learning, and automation.
        - Python, known for its simplicity and versatility, is one of the most popular programming languages today. From developing dynamic web applications to driving machine learning algorithms and handling complex data analytics. Most of the tech giants like Google, Amazon, Facebook, and Instagram rely on Python to build and maintain their cutting-edge technology solutions.
        """)

        image_url = "https://d8it4huxumps7.cloudfront.net/uploads/images/65608f420c159_what_is_python_1.jpg?d=2000x2000"
        st.image(image_url, width=800)
        
        # Key features
        st.subheader("Key Features")
        st.write("- **Interpreted Language:** This implies that Python code is executed one line at a time, making it an interpreted language. Also, in comparison to other popular languages like C, C++, Java, etc., Python code does not require compilation, making it easier to debug. In fact, an immediate format called the Bytecode is created from Python's source code.")
        st.write("- **Cross-platform Language:** Python is compatible with many operating systems/ platforms, including Windows, macOS, Linux, etc. This feature allows Python code to be portable across platforms, further allowing programmers to write code once and run it indistinguishably on several platforms.")
        st.write("- **Free and Open Source:** The language is free to download and use. Users can download Python from the official website. In addition to that, the public can also see the source code since Python is open-source.")
        st.write("- **Object Oriented:** Python has object-oriented programming features, enabling the creation and use of classes, objects, and inheritance. It encourages modular and reusable code, making it easier to develop complex applications.")
        st.write("- **Broad Standard Library:** Python contains a huge standard library with a wide selection of modules and functions, so you don't need to write any of your own code. Regular expressions, unit testing, web browsers, and other tools are all part of Python's sizable library.")
        st.write("- **GUI Support:** It is possible to create/ develop graphical user interfaces in Python by using packages like PyQt5, PyQt4, wxPython, or Tk.")
        st.write("- **Easy to Use and Maintain:** Python is pretty easy to pick up compared to other languages like C, C#, Javascript, etc. Anyone can pick up the basics of the relatively easy programming language in even a few hours or days. These features have won Python the title of one of the most user-friendly programming languages out there.")
        st.write("- **Robust:** The robustness of Python is owed to its formidable error-management capabilities, which let programmers find and fix errors in their code effectively. These features include integrated exception handling and traceback information.")
        st.write("- **Dynamically Typed:** Python is a dynamically typed language, i.e., the variable type is decided at run time (for example, int, double, long, etc.). This feature eliminates the need for users to declare the type of a variable.")
        
        # Basic concepts
        st.subheader("Basic Concepts")
        st.markdown("""
        * **Variables:** Used to store data (e.g., numbers, text, lists).
        * **Data Types:** Different types of data, such as integers, floats, strings, lists, tuples, dictionaries.
        * **Operators:** Used to perform operations (e.g., arithmetic, comparison, logical).
        * **Control Flow:** Statements that determine the order in which code is executed (e.g., if-else, loops).
        * **Functions:** Reusable blocks of code that perform specific tasks.
        * **Modules:** Files containing Python code that can be imported into other programs.
        """)
        
        
        # Getting started
        st.subheader("Getting Started")
        st.markdown("""
        1. **Download and Install:** Visit the official Python website (python.org) and download the appropriate version for your operating system.
        2. **Write Code:** Use a text editor or integrated development environment (IDE) to write your Python code.
        3. **Run Code:** To execute your code, save it as a .py file and run it from the command line or your IDE.
        """)

        # Popular libraries
        st.subheader("Popular Libraries")
        st.write("- **NumPy:** For numerical computations and scientific computing.")
        st.write("- **Pandas:** For data manipulation and analysis.")
        st.write("- **Matplotlib:** For creating visualizations and plots.")
        st.write("- **Scikit-learn:** For machine learning tasks.")
        st.write("- **TensorFlow and PyTorch:** For deep learning.")


    if selected == 3:
        st.header("First Python Program to Learn Python Programming")
        st.write("There are two ways you can execute your Python program:")
        st.write("1. First, we write a program in a file and run it one time.")
        st.write("2. Second, run a code line by line.")

        st.text("Input")
        code = """
        # Python Program to print Hello World
        print("Hello World! I Don't Give a Bug")
        """
        st.code(code, language="python")
        st.text("Output")
        st.success("Hello World! I Don't Give a Bug")
        st.text("In this code we have used a [  print  ]function")
        code1 ="""
        #Syntax
        print()
        """
        st.code(code1, language="python")
               
        
    if selected == 4:
        st.subheader("Comments in Python")
        st.write("Comments in Python are the lines in the code that are ignored by the interpreter during the execution of the program. Also, Comments enhance the readability of the code and help the programmers to understand the code very carefully.")
        code = """
        # sample comment 
        # This is Python Comment
        """
        st.code(code, language="python")
        st.subheader("Indentation in Python")
        st.write("Python indentation refers to adding white space before a statement to a particular block of code. In other words, all the statements with the same space to the left, belong to the same code block.")
        code1 = """
        Statement                                           Code block 1 begins
        if condition:             How the interpreter       Code block 1 continues
            if condition:             visuallizes               Code block 2 
                Statement          =================>               Code block 3 begins
            else:                                               Code block 2 continues
                Statement                                           Code block 3 continues
        Statement                                           Code block 1 continues  
        """
        st.code(code1, language="python")
        st.info("Note: This will be more under standable in the Controll flow topic.")
        st.markdown("""
        * Statement (line 1), if condition (line 2), and statement (last line) belongs to the same block which means that after statement 1, if condition will be executed. and suppose the if condition becomes False then the Python will jump to the last statement for execution.
        * The nested if-else belongs to block 2 which means that if nested if becomes False, then Python will execute the statements inside the else condition.
        * Statements inside nested if-else belong to block 3 and only one statement will be executed depending on the if-else condition.
        """)

    if selected == 5:
        st.header("Python Variable")
        st.write("Python Variable is containers that store values. Python is not “statically typed”. An Example of a Variable in Python is a representational name that serves as a pointer to an object. Once an object is assigned to a variable, it can be referred to by that name.")
        st.markdown("""
        * **Rules for Python variables**
        * A Python variable name must start with a letter or the underscore character.
        * A Python variable name cannot start with a number.
        * A Python variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
        * Variable in Python names are case-sensitive (name, Name, and NAME are three different variables).
        * The reserved words(keywords) in Python cannot be used to name the variable in Python.
        """)
        st.text("Input")
        code = """
        # An integer assignment
        age = 45
        
        # A floating point
        salary = 1456.8
        
        # A string
        name = "John"
        
        print("age = ",age)
        print("salary =",salary)
        print("name =",name)
        """
        st.code(code, language="python")
        st.text("Output")
        hemlo = """
age = 45\n
salary = 1456.8\n
name = John
        """
        st.success(hemlo)






    

    if selected == 7:
        st.header("Python Data Types")
        st.write("Python data types offers, enabling you to manipulate and manage data with precision and flexibility. Additionally, we’ll delve into the dynamic world of data conversion with casting, and then move on to explore the versatile collections Python provides, including lists, tuples, sets, dictionaries, and arrays.")
        image_url="https://media.geeksforgeeks.org/wp-content/uploads/20191023173512/Python-data-structure.jpg"
        st.image(image_url, width=600)
        st.write("By the end of this section, you’ll not only grasp the essence of Python’s data types but also wield them proficiently to tackle a wide array of programming challenges with confidence.")
        st.markdown("""
        * **Numbers**
        * **Strings**
        * **Booleans**
        * **Python List**
        * **Python Tuples**
        * **Python Sets**
        * **Python Dictionary**
        * **Type Casting**
        """)
        st.subheader("1. Numeric Data Types in Python")
        st.write("The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, or even a complex number. These values are defined as Python int , Python float , and Python complex classes in Python .")
        st. markdown("""
        * **Integer-** This value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). In Python, there is no limit to how long an integer value can be
        * **Float-** This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
        * **Complex Numbers-** A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j . For example – 2+3j
        """)
        st.info("Note – type() function is used to determine the type of Python data type.")
        st.markdown("""
        **Example** This code demonstrates how to determine the data type of variables in Python using the type() function . It prints the data types of three variables : a (integer) , b (float) , and c (complex) . The output shows the respective data type Python for each variable.
        """)
        st.text("Input")
        code4 = """
        a = 5
print("Type of a: ", type(a))
        
b = 5.0
print("Type of b: ", type(b))
        
c = 2 + 4j
print("Type of c: ", type(c))
        """
        st.code(code4, language="python")
        st.text("Output")
        code5 = """
Type of a:  <class 'int'> \n
Type of b:  <class 'float'> \n
Type of c:  <class 'complex'>
"""
        st.success(code5)

        
        st.subheader("2. Strings Data Types in Python")
        st.write("Strings in Python are arrays of bytes representing Unicode characters. A string is a collection of one or more characters put in a single quote, double-quote, or triple-quote. In Python, there is no character data type Python, a character is a string of length one. It is represented by str class.")
        st.text("Creating String")
        st.write("Strings in Python can be created using single quotes, double quotes, or even triple quotes.")
        st.markdown("""
        * **Example:** This Python code showcases various string creation methods. It uses single quotes, double quotes, and triple quotes to create strings with different content and includes a multiline string. The code also demonstrates printing the strings and checking their data types.
        """)
        st.text("Input")
        code = """
String1 = 'Welcome to the Basics World'
print("String with the use of Single Quotes: ")
print(String1)
String1 = "I'm a Basic"
print("String with the use of Double Quotes: ")
print(String1)
print(type(String1))
String1 = '''I'm a Basic and I live in a world of "Basics"'''
print("String with the use of Triple Quotes: ")
print(String1)
print(type(String1))

String1 = '''Basics 
            And 
            Life'''
print("Creating a multiline String: ")
print(String1)
"""
        st.code(code, language="python")
        st.text("Output")
        code1 = """
String with the use of Single Quotes:\n
Welcome to the Basics World\n
String with the use of Double Quotes:\n 
I'm a Basic\n
<class 'str'>\n
String with the use of Triple Quotes:\n 
I'm a Basic and I live in a world of "Basics"\n
<class 'str'>\n
Creating a multiline String:\n \n
            Basics\n
            And\n
            Life\n
"""
        st.success(code1)
        st.subheader("Accessing elements of String")
        st.write("In Python programming , individual characters of a String can be accessed by using the method of Indexing. Negative Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on.")
        st.markdown("""
        **Example:** This Python code demonstrates how to work with a string named ‘ String1′ . It initializes the string with “Basicslearn” and prints it. It then showcases how to access the first character ( “G” ) using an index of 0 and the last character ( “s” ) using a negative index of -1.
        """)
        st.text("Input")
        code2 = """
String1 = "Basicslearn"
print("Initial String: ")
print(String1)
print("First character of String is: ")
print(String1[0])
print("Last character of String is: ")
print(String1[-1])
"""
        st.code(code2 , language="python")
        st.text("output")
        code3 = """
Initial String: \n
Basicslearn\n
First character of String is:\n 
B\n
Last character of String is:\n 
n\n
"""
        st.success(code3)

        st.subheader("3. List Data Type in Python")
        st.write("Lists are just like arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type.")
        st.markdown("""
        **Creating a List in Python**
        """)
        st.write("Lists in Python can be created by just placing the sequence inside the square brackets[].")
        st.markdown("""
        **Example:** This Python code demonstrates list creation and manipulation. It starts with an empty list and prints it. It creates a list containing a single string element and prints it. It creates a list with multiple string elements and prints selected elements from the list. It creates a multi-dimensional list (a list of lists) and prints it. The code showcases various ways to work with lists, including single and multi-dimensional lists.
        """)
        st.text("Input")
        code6 = """
List = []
print("Initial blank List: ")
print(List)
List = ['Basicslearn']
print("List with the use of String: ")
print(List)
List = ["Basics", "And", "Learn"]
print("List containing multiple values: ")
print(List[0])
print(List[2])
List = [['Basics', 'And'], ['Learn']]
print("Multi-Dimensional List: ")
print(List)
"""
        st.code(code6, language="python")
        st.text("Output")
        code7 = """
Initial blank List: \n
[]\n
List with the use of String: \n
['Basicslearn']\n
List containing multiple values: \n
basics\n
learn\n
Multi-Dimensional List: \n
[['Basics', 'And'], ['Learn']]\n
"""
        st.success(code7,)
        st.subheader("Access List Items")
        st.write("In order to access the list items refer to the index number. Use the index operator [ ] to access an item in a list. In Python, negative sequence indexes represent positions from the end of the array. Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.")
        st.text("Input")
        code8 = """
List = ["Basics", "And", "Learn"]
print("Accessing element from the list")
print(List[0])
print(List[2])
print("Accessing element using negative indexing")
print(List[-1])
print(List[-3])
"""
        st.code(code8, language="python")
        st.text("Output")
        code9 = """
Accessing element from the list\n
Basics\n
Learn\n
Accessing element using negative indexing\n
Learn\n
Basics\n
"""
        st.success(code9)
        st.subheader("4. Tuple Data Type in Python")
        st.write("Just like a list, a tuple is also an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable i.e. tuples cannot be modified after it is created. It is represented by a tuple class.")
        st.markdown("""
        **Creating a Tuple in Python**
        """)
        st.write("In Python Data Types, tuples are created by placing a sequence of values separated by a ‘comma’ with or without the use of parentheses for grouping the data sequence. Tuples can contain any number of elements and of any datatype (like strings, integers, lists, etc.). Note: Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.")
        st.markdown("""
        **Example:**  This Python code demonstrates different methods of creating and working with tuples. It starts with an empty tuple and prints it. It creates a tuple containing string elements and prints it. It converts a list into a tuple and prints the result. It creates a tuple from a string using the tuple() function. It forms a tuple with nested tuples and displays the result.
        """)
        st.text("Input")
        code10 = """
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)
Tuple1 = ('Basics', 'And')
print("Tuple with the use of String: ")
print(Tuple1)
list1 = [1, 2, 4, 5, 6]
print("Tuple using List: ")
print(tuple(list1))
Tuple1 = tuple('')
print("Tuple with the use of function: ")
print(Tuple1)
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'Basic')
Tuple3 = (Tuple1, Tuple2)
print("Tuple with nested tuples: ")
print(Tuple3)
"""
        st.code(code10, language="python")
        st.text("Output")
        code11 = """
Initial empty Tuple: \n
()\n
Tuple with the use of String:\n 
('Basics', 'And')\n
Tuple using List: \n
(1, 2, 4, 5, 6)\n
Tuple with the use of function:\n 
('G', 'e', 'e', 'k', 's')\n
Tuple with nested tuples: \n
((0, 1, 2, 3), ('python', 'Basic'))\n
"""
        st.success(code11)
        st.subheader("Access Tuple Items")
        st.write("In order to access the tuple items refer to the index number. Use the index operator [ ] to access an item in a tuple. The index must be an integer. Nested tuples are accessed using nested indexing.")
        st.write("The code creates a tuple named ‘ tuple1′ with five elements: 1, 2, 3, 4, and 5 . Then it prints the first, last, and third last elements of the tuple using indexing.")
        st.text("Input")
        code12 = """
tuple1 = tuple([1, 2, 3, 4, 5])
print("First element of tuple")
print(tuple1[0])
print("Last element of tuple")
print(tuple1[-1])
print("Third last element of tuple")
print(tuple1[-3])
"""
        st.code(code12, language="python")
        st.text("Output")
        code13 = """
First element of tuple\n
1\n
Last element of tuple\n
5\n
Third last element of tuple\n
3\n
"""
        st.success(code13)
        
        st.subheader("5. Boolean Data Type in Python")
        st.write("Python Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false). However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false. It is denoted by the class bool.")
        st.info("Note – True and False with capital ‘T’ and ‘F’ are valid booleans otherwise python will throw an error.")
        st.markdown("""
        **Example:** The first two lines will print the type of the boolean values True and False, which is <class ‘bool’>. The third line will cause an error, because true is not a valid keyword in Python. Python is case-sensitive, which means it distinguishes between uppercase and lowercase letters. You need to capitalize the first letter of true to make it a boolean value.
        """)
        st.text("Input")
        code14 = """
print(type(True))
print(type(False))
print(type(true))
"""
        st.code(code14, language="python")
        st.text("Output")
        code15 = """
<class 'bool'>\n
<class 'bool'>
""" 
        st.success(code15)
        eror = """
Traceback (most recent call last):\n
  File "/home/7e8862763fb66153d70824099d4f5fb7.py", line 8, in \n
    print(type(true))\n
NameError: name 'true' is not defined\n
"""
        st.error(eror)
        st.subheader("6. Set Data Type in Python")
        st.write("In Python Data Types, a Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.")
        st.markdown("""
**Create a Set in Python**
""")
        st.write("Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by a ‘comma’. The type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set.")
        st.markdown("""
**Example:** The code is an example of how to create sets using different types of values, such as strings , lists , and mixed values
""")
        st.text("Input")
        code16 = """
set1 = set()
print("Initial blank Set: ")
print(set1)
set1 = set("Basicslearn")
print("Set with the use of String: ")
print(set1)
set1 = set(["Basic", "And", "Learn"])
print("Set with the use of List: ")
print(set1)
set1 = set([1, 2, 'Basics', 4, 'And', 6, 'Learn'])
print("Set with the use of Mixed Values")
print(set1)
"""
        st.code(code16, language="python")
        st.text("Output")
        code17 = """
Initial blank Set: \n
set()\n
Set with the use of String: \n
{'e', 's', 'a', 'l', 'B', 'i', 'c', 'r', 'n'}\n
Set with the use of List: \n
{'And', 'Basic', 'Learn'}\n
Set with the use of Mixed Values\n
{1, 2, 4, 6, 'And', 'Basics', 'Learn'}
"""
        st.success(code17)
        st.subheader("Access Set Items")
        st.write("Set items cannot be accessed by referring to an index, since sets are unordered the items have no index. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in the keyword.")
        st.markdown("""
**Example:** This Python code creates a set named set1 with the values “Basics” , “And” and “Learn” .  The code then prints the initial set, the elements of the set in a loop, and checks if the value “Learne” is in the set using the ‘ in’ operator
""")
        st.text("Input")
        code18 = """
set1 = set(["Basics", "And", "Learn"])
print("Initial set")
print(set1)
print("Elements of set:")
for i in set1:
    print(i, end=" ")
print("\n","Basics" in set1)
"""
        st.code(code18, language="python")
        st.text("Output")
        code19 = """
Initial set\n
{'Basics', 'Learn', 'And'}\n

Elements of set:\n
Basics Learn And \n
 True
"""
        st.success(code19)
        st.subheader("7. Dictionary Data Type in Python")
        st.write("A dictionary in Python is an unordered collection of data values, used to store data values like a map, unlike other Python Data Types that hold only a single value as an element, a Dictionary holds a key: value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.")
        st.markdown("""
        **Create a Dictionary in Python**
        """)
        st.write("In Python, a Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable. The dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing it in curly braces{}. **Note –** Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly.")
        st.write(" **Example:** This code creates and prints a variety of dictionaries. The first dictionary is empty. The second dictionary has integer keys and string values. The third dictionary has mixed keys, with one string key and one integer key. The fourth dictionary is created using the dict() function, and the fifth dictionary is created using the [(key, value)] syntax")
        st.text("Input")
        code20 = """
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict = {1: 'Basics', 2: 'And', 3: 'Learn'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
Dict = {'Name': 'Basics', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
Dict = dict({1: 'Basics', 2: 'And', 3: 'Learn'})
print("\nDictionary with the use of dict(): ")
print(Dict)
Dict = dict([(1, 'Basics'), (2, 'And')])
print("\nDictionary with each item as a pair: ")
print(Dict)
"""
        st.code(code20, language="python")
        st.text("Output")
        code21 = """
Empty Dictionary: \n
{}\n

Dictionary with the use of Integer Keys: \n
{1: 'Basics', 2: 'And', 3: 'Learn'}\n

Dictionary with the use of Mixed Keys:\n 
{'Name': 'Basics', 1: [1, 2, 3, 4]}\n

Dictionary with the use of dict(): \n
{1: 'Basics', 2: 'And', 3: 'Learn'}\n

Dictionary with each item as a pair: \n
{1: 'Basics', 2: 'And'}\n
"""
        st.success(code21)
        st.subheader("Accessing Key-value in Dictionary")
        st.write("In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets. There is also a method called get() that will also help in accessing the element from a dictionary.")
        st.markdown("""
**Example:** The code in Python is used to access elements in a dictionary. Here’s what it does, It creates a dictionary Dict with keys and values as { 1: ‘Basics’, ‘name’: ‘And’, 3: ‘Learn’} . It prints the value of the element with the key ‘name’ , which is ‘And’ . It prints the value of the element with the key 3, which is ‘Learn’ .
""")
        st.text("Input")
        code22 = """
Dict = {1: 'Basics', 'name': 'And', 3: 'Learn'}
print("Accessing a element using key:")
print(Dict['name'])
print("Accessing a element using get:")
print(Dict.get(3))
"""
        st.code(code22, language="python")
        st.text("Output")
        code23 = """
Accessing a element using key:\n
And\n
Accessing a element using get:\n
Learn
"""
        st.success(code23)
        st.subheader("7. Type Casting in Python")
        st.markdown("""
Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users. In this article, we will see the various techniques for typecasting. There can be two types of 
Type Casting in Python:

* Python Implicit Type Conversion
* Python Explicit Type Conversion
""")
        st.subheader("Implicit Type Conversion in Python")
        st.write("In this, method, Python converts the datatype into another datatype automatically. Users don’t have to involve in this process.")
        st.text("Input")
        code24 = """
# Python program to demonstrate 
# implicit type Casting 

# Python automatically converts 
# a to int 
a = 7
print(type(a)) 

# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 

# Python automatically converts 
# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))

# Python automatically converts 
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))
"""
        st.code(code24, language="python")
        st.text("Output")
        code25 = """
<class 'int'>\n
<class 'float'>\n
10.0\n
<class 'float'>\n
21.0\n
<class 'float'>
"""
        st.success(code25)
        st.subheader("Explicit Type Conversion in Python")
        st.markdown("""
In this method, Python needs user involvement to convert the variable data type into the required data type. 

**Examples of Type Casting in Python**
Mainly type casting can be done with these data type functions:

* Int(): Python Int() function take float or string as an argument and returns int type object.
* float(): Python float() function take int or string as an argument and return float type object.
* str(): Python str() function takes float or int as an argument and returns string type object.

**Python Convert Int to Float**
Here, we are Converting Int to Float in Python with the float() function.
""")
        st.text("Input")
        code26 = """
# Python program to demonstrate 
# type Casting 

# int variable
a = 5

# typecast to float
n = float(a)

print(n)
print(type(n))
"""
        st.code(code26, language="python")
        st.text("Output")
        code27 = """
5.0\n
<class 'float'>
"""
        st.success(code27)
        st.markdown("""
**Python Convert Float to Int**

Here, we are Converting Float to int datatype in Python with int() function.
""")
        st.text("Input")
        code28 = """
# Python program to demonstrate 
# type Casting 

# int variable
a = 5.9

# typecast to int
n = int(a)

print(n)
print(type(n))
"""
        st.code(code28, language="python")
        st.text("Output")
        code29 = """
5\n
<class 'int'>
"""
        st.success(code29)
        st.markdown("""
**Python Convert int to String** 

Here, we are Converting int to String datatype in Python with str() function.
""")
        st.text("Input")
        code30 = """
# Python program to demonstrate 
# type Casting 

# int variable
a = 5

# typecast to str
n = str(a)

print(n)
print(type(n))
"""
        st.code(code30, language="python")
        st.text("Output")
        code31 = """
5\n
<class 'str'>
"""
        st.success(code31)
        st.markdown("""
**Python Convert String to float**

Here, we are casting string data type into float data type with float() function.
""")
        st.text("Input")
        code32 = """
# Python program to demonstrate 
# type Casting 

# string variable
a = "5.9"

# typecast to float
n = float(a)

print(n)
print(type(n))
"""
        st.code(code32, language="python")
        st.text("Output")
        code33 = """
5.9\n
<class 'float'>
"""
        st.success(code33)
        st.markdown("""
**Python Convert string to int**

Here, we are Converting string to int datatype in Python with int() function. If the given string is not number, then it will throw an error.
""")
        st.text("Input")
        code34 = """
# string variable
a = "5"
b = 't'

# typecast to int
n = int(a)

print(n)
print(type(n))

print(int(b))
print(type(b))
"""
        st.code(code34)
        st.text("Output")
        code35 = """
5\n
<class 'int'>
"""
        st.success(code35)
        st.text("Error")
        code36 = """
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

Cell In[3], line 14\n
    11 print(n)\n
    12 print(type(n))\n     
    14 print(int(b))  <----\n
    15 print(type(b)) \n    
ValueError: invalid literal for int() with base 10: 't'
"""
        st.error(code36)
        st.write(" **Addition of string and integer Using Explicit Conversion** ")
        st.text("Input")
        code36 = """
# integer variable
a = 5
# string variable
b = 't'

# typecast to int
n = a+b

print(n)
print(type(n))
"""
        st.code(code36)
        st.text("Output")
        code37 = """
TypeError         \t\t\t\t                        Traceback (most recent call last)
Cell In[5], line 10\n
    7 b = 't'\n
    9 # typecast to int\n
    10 n = a+b <----\n
    12 print(n)\n
    13 print(type(n))\n
"""
        st.error(code37)



    if selected == 6:
        st.header("Input and Output in Python")
        st.write("Understanding input and output operations is fundamental to Python programming. With the print() function, you can display output in various formats, while the input() function enables interaction with users by gathering input during program execution.")
        st.subheader("Python Basic Input and Output")
        st.write("In this introductory guide, we’ll explore the essentials of Python’s basic input and output functionalities, empowering you to efficiently interact with users and display information.")
        st.subheader("Print Output in Python")
        st.markdown("""
At its core, printing output in Python is straightforward, thanks to the print() function. This function allows us to display text, variables, and expressions on the console. Let’s begin with the basic usage of the print() function:

**How to Print Output in Python**

In this example, “Hello, World!” is a string literal enclosed within double quotes. When executed, this statement will output the text to the console.
""")
        code1 = """
print("Hello, World!")
"""
        st.text("Input")
        st.code(code1, language="python")
        st.text("Output")
        code2 = """
Hello, World!
"""
        st.success(code2)
        st.subheader("Print Single and Multiple variable in Python")
        st.write("The code assigns values to variables name and age, then prints them with labels.")
        st.text("Input")
        code3 = """
name = "Alice"
age = 30
print("Name:", name, "Age:", age)
"""
        st.code(code3, language="python")
        st.text("Output")
        code4 = """
Name: Alice Age: 30
"""
        st.success(code4)
        st.subheader("Format Output Handling in Python")
        st.write("Output formatting in Python with various techniques including the format() method, manipulation of the sep and end parameters, f-strings, and the versatile % operator. These methods enable precise control over how data is displayed, enhancing the readability and effectiveness of your Python programs.")
        st.write(" **Example 1:**  Using Format()")
        st.text("Input")
        code5 = """
amount = 150.75
print("Amount: ${:.2f}".format(amount))
"""
        st.code(code5, language="python")
        st.text("Output")
        code6 = """
Amount: $150.75
"""
        st.success(code6)
        st.write(" **Example 2:** Using sep and end parameter")
        code7 = """
# end Parameter with '@'
print("Python", end='@')
print("BasicsLearn")


# Seprating with Comma
print('B', 'A', 'L', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'Basicsandlearn', sep='@')
"""
        st.code(code7, language="python")
        st.text("Output")
        code8 = """
Python@BasicsLearn\n
BAL\n
09-12-2016\n
pratik@Basicsandlearn
"""
        st.success(code8)
        st.write(" **Example 3:** Using f-string")
        st.text("Input")
        code9 = """
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
"""
        st.code(code9, language="python")
        st.text("Output")
        code10 = """
Hello, My name is Tushar and I'm 23 years old.
"""
        st.success(code10)
        st.write(" **Example 4:** Using % Operator")
        st.markdown(""" 
We can use ‘%’ operator. % values are replaced with zero or more value of elements. The formatting using % is similar to that of ‘printf’ in the C programming language.
* %d –integer
* %f – float
* %s – string
* %x –hexadecimal
* %o – octal
""")
        st.text("Input")
        code11 = """
# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" %add)
"""
        st.code(code11, language="python")
        st.text("Output")
        code12 = """
Enter a value: 50The sum is 55
"""
        st.success(code12)
        st.write(" **Take Multiple Input in Python** ")
        st.write("The code takes input from the user in a single line, splitting the values entered by the user into separate variables for each value using the split() method. Then, it prints the values with corresponding labels, either two or three, based on the number of inputs provided by the user.")
        st.text("Input")
        code13 = """
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
"""
        st.code(code13, language="python")
        st.text("Output")
        code14 = """
Enter two values: 5 10\n
Number of boys:  5  \n
Number of girls:  10\n
Enter three values: 5 10 15\n
Total number of students:  5\n
Number of boys is :  10     \n
Number of girls is :  15  
"""
        st.success(code14)
        st.write(" **Take Conditional Input from user in Python** ")
        st.write("In this example, the program prompts the user to enter their age. The input is converted to an integer using the int() function. Then, the program uses conditional statements to check the age range and prints a message based on whether the user is a minor, an adult, or a senior citizen.")
        st.text("Input")
        code15 = """
# Prompting the user for input
age_input = input("Enter your age: ")

# Converting the input to an integer
age = int(age_input)

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
"""
        st.code(code15, language="python")
        st.text("output")
        code16 = """
Enter your age: 22\n
You are an adult.
"""
        st.success(code16)
        st.subheader("Taking input in Python")
        st.write(" **Python input() function** is used to take user input. By default, it returns the user input in form of a string.")
        st.info("Syntax: input(prompt)")
        st.write(" **How to Take Input in Python** ")
        st.write("The code prompts the user to input their name, stores it in the variable “name”, and then prints a greeting message addressing the user by their entered name.")
        st.text("Input")
        code17 = """
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
"""
        st.code(code17, language="python")
        st.text("Output")
        code18 = """
Enter your name: BasicsLearn\n
Hello, BasicsLearn ! Welcome!
"""
        st.success(code18)
        st.write(" **How to Change the Type of Input in Python** ")
        st.write("By default input() function helps in taking user input as string. If any user wants to take input as int or float, we just need to typecast it.")
        st.write(" **How to Print Names in Python** ")
        st.write("The code prompts the user to input a string (the color of a rose), assigns it to the variable color, and then prints the inputted color.")
        st.text("Input")
        code19 = """
# Taking input as string
color = input("What color is rose?: ")
print(color)
"""
        st.code(code19, language="python")
        st.text("output")
        code20 = """
What color is rose?: Red\n
Red
"""
        st.success(code20)
        st.write(" **How to Print Numbers in Python** ")
        st.write("The code prompts the user to input an integer representing the number of roses, converts the input to an integer using typecasting, and then prints the integer value.")
        st.text("Input")
        code21 = """
# Taking input as int
# Typecasting to int
n = int(input("How many roses?: "))
print(n)
"""
        st.code(code21, language="python")
        st.text("Output")
        code22 = """
How many roses?: 8\n
8
"""
        st.success(code22)
        st.write(" **How to Print Float/Decimal Number in Python** ")
        st.write("The code prompts the user to input the price of each rose as a floating-point number, converts the input to a float using typecasting, and then prints the price.")
        st.text("Input")     
        code23 = """
# Taking input as float
# Typecasting to float
price = float(input("Price of each rose?: "))
print(price)
"""
        st.code(code23, language="python")
        st.text("Output")
        code24 = """
Price of each rose?: 50.30\n
50.3
"""
        st.success(code24)
        st.write(" **Find DataType of Input in Python** ")
        st.write("In the given example, we are printing the type of variable x. We will determine the type of an object in Python.")
        st.text("Input")
        code25 = """
a = "Hello World"
b = 10
c = 11.22
d = ("Basics", "and", "Learn")
e = ["Basics", "and", "Learn"]
f = {"Basics": 1, "and":2, "Learn":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
"""
        st.code(code25, language="python")
        st.text("Output")
        code26 = """
<class 'str'>\n
<class 'int'>\n
<class 'float'>\n
<class 'tuple'>\n
<class 'list'>\n
<class 'dict'>\n
"""
        st.success(code26)
        

    if selected == 8:
        st.header("Python Operators")
        st.write("In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for logical and arithmetic operations. In this article, we will look into different types of Python operators.")
        st.markdown("""
* **OPERATORS:** These are the special symbols. Eg- + , * , /, etc.
* **OPERAND:** It is the value on which the operator is applied.
""")
        st.subheader("Types of Operators in Python")
        st.markdown("""
1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Identity Operators and Membership Operators
""")
        image_url = "https://media.geeksforgeeks.org/wp-content/uploads/20240430181610/Operators-in-python.webp"
        st.image(image_url, width=800)
        st.subheader("1. Arithmetic Operators in Python")
        st.write("Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication, and division.")
        st.write("In Python 3.x the result of division is a floating-point while in Python 2.x division of 2 integers was an integer. To obtain an integer result in Python 3.x floored (// integer) is used.")
        data = {'Operator': ['+', '-', '*', '/', '//', '%', '**'], 
                'Description': ['Addition: adds two operands', 'Subtraction: subtracts two operands', 'Multiplication: multiplies two operands', 'Division (float): divides the first operand by the second', 'Division (floor): divides the first operand by the second', 'Modulus: returns the remainder when the first operand is divided by the second', 'Power: Returns first raised to power second'], 
                'Syntax': ['x + y', 'x - y', 'x * y', 'x / y', 'x // y', 'x % y', 'x ** y']}
        df = pd.DataFrame(data)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.table(df)
            st.write("  **Example of Arithmetic Operators in Python** ")
            st.text("Input")
        code1 = """
a = 9
b = 4

#Operators
add = a + b

sub = a - b

mul = a * b

floatdiv = a / b

floordiv = a // b

mod = a % b

p = a ** b

#Execution
print(add)
print(sub)
print(mul)
print(floatdiv)
print(floordiv)
print(mod)
print(p)
"""
        st.code(code1, language="python")
        st.text("Output")
        code2 =  """
13\n
5\n
36\n
2.25\n
2\n
1\n
6561
"""
        st.success(code2)
        st.write(" **Precedence of Arithmetic Operators in Python**")
        st.markdown("""
The precedence of Arithmetic Operators in Python is as follows:

1. P – Parentheses
2. E – Exponentiation
3. M – Multiplication (Multiplication and division have the same precedence)
4. D – Division
5. A – Addition (Addition and subtraction have the same precedence)
6. S – Subtraction
""")
        st.subheader("2. Comparison of Python Operators")
        st.write("In Python Comparison of Relational operators compares the values. It either returns True or False according to the condition.")
        data1 = {'Operator': ['>', '<', '==', '!=', '>=', '<='], 
                'Description': ['Greater than: True if the left operand is greater than the right', 'Less than: True if the left operand is less than the right', 'Equal to: True if both operands are equal', 'Not equal to – True if operands are not equal', 'Greater than or equal to True if the left operand is greater than or equal to the right', 'Less than or equal to True if the left operand is less than or equal to the right'], 
                'Syntax': ['x > y', 'x < y', 'x == y', 'x != y', 'x >= y', 'x <= y']}
        df1 = pd.DataFrame(data1)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.table(df1)
        st.write(" **Example of Comparison Operators in Python** ")
        st.text("Input")
        code3 = """
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
"""
        st.code(code3, language="python")
        st.text("Output")
        code4 = """
False\n
True\n
False\n
True\n
False\n
True
"""
        st.success(code4)
        st.markdown("""
**Precedence of Comparison Operators in Python**

In Python, the comparison operators have lower precedence than the arithmetic operators. All the operators within comparison operators have the same precedence order.
""")
        st.subheader("3. Logical Operators in Python")
        st.write("Python Logical operators perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.")
        data2 = {'Operator': ['and', 'or', 'not'], 
                'Description': ['Logical AND: True if both the operands are true', 'Logical OR: True if either of the operands is true', 'Logical NOT: True if the operand is false'], 
                'Syntax': ['x and y', 'x or y', 'not x']}
        df2 = pd.DataFrame(data2)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.table(df2)
        st.write(" **Example of Logical Operators in Python** ")
        st.text("Input")
        code5 = """
a = True
b = False
print(a and b)
print(a or b)
print(not a)
"""
        st.code(code5, language="python")
        st.text("Output")
        code6 = """
False\n
True\n
False
"""
        st.success(code6)
        st.write(" **Precedence of Logical Operators in Python** ")
        st.markdown("""
The precedence of Logical Operators in Python is as follows:

1. Logical not
2. logical and
3. logical or
""")
        st.subheader("4. Bitwise Operators in Python")
        st.write("Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.")
        data3 = {'Operator': ['&', '|', '~', '^', '>>', '<<'], 
                'Description': ['Bitwise AND', 'Bitwise OR', 'Bitwise NOT', 'Bitwise XOR', 'Bitwise right shift', 'Bitwise left shift'], 
                'Syntax': ['x & y', 'x | y', '~x', 'x ^ y', 'x>>', 'x<<']}
        df3 = pd.DataFrame(data3)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.table(df3)
        st.write(" **Example of Bitwise Operators in Python** ")
        st.text("Input")
        code7 = """
a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
"""
        st.code(code7, language="python")
        st.text("Ouput")
        code8 = """
0\n
14\n
-11\n
14\n
2\n
40
"""
        st.success(code8)
        st.markdown("""
**Precedence of Bitwise Operators in Python**

The precedence of Bitwise Operators in Python is as follows:

1. Bitwise NOT
2. Bitwise Shift
3. Bitwise AND
4. Bitwise XOR
5. Bitwise OR)
""")
        st.subheader("5. Assignment Operators in Python")
        st.write("Python Assignment operators are used to assign values to the variables.")
        data4 = {'Operator': ['=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=' ,'^=' , '>>=', '<<='], 
                'Description': ['Assign the value of the right side of the expression to the left side operand', 'Add AND: Add right-side operand with left-side operand and then assign to left operand', 'Subtract AND: Subtract right operand from left operand and then assign to left operand', 'Multiply AND: Multiply right operand with left operand and then assign to left operand', 'Divide AND: Divide left operand with right operand and then assign to left operand', 'Modulus AND: Takes modulus using left and right operands and assign the result to left operand', 'Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand', 'Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand', 'Performs Bitwise AND on operands and assign value to left operand', 'Performs Bitwise OR on operands and assign value to left operand', 'Performs Bitwise xOR on operands and assign value to left operand', '	Performs Bitwise right shift on operands and assign value to left operand', 'Performs Bitwise left shift on operands and assign value to left operand'], 
                'Syntax': ['x = y + z', 'a+=b     a=a+b', 'a-=b     a=a-b', 'a*=b     a=a*b', 'a/=b     a=a/b', 'a%=b     a=a%b', 'a//=b     a=a//b', 'a**=b     a=a**b', 'a&=b     a=a&b', 'a|=b     a=a|b', 'a^=b     a=a^b', 'a>>=b     a=a>>b', 'a <<= b     a= a << b']}
        df4 = pd.DataFrame(data4)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.table(df4)
        st.write(" **Example of Assignment Operators in Python** ")
        st.text("Input")
        code9 = """
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)
"""
        st.code(code9, language='python')
        st.text("Output")
        code10 = """
10\n
20\n
10\n
100\n
102400
"""
        st.success(code10)
        st.subheader("6. Identity Operators in Python")
        st.write("In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical")
        code11 = """
is    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      #True if the operands are identical \n
is not    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  #True if the operands are not identical 
"""
        st.info(code11)
        st.write(" **Example of Identity Operators in Python** ")
        st.text("Input")
        code12 = """
a = 10
b = 20
c = a

print(a is not b)
print(a is c)
"""
        st.code(code12, language="python")
        st.text("Output")
        code13 = """
True\n
True
"""
        st.success(code13)
        st.subheader("Membership Operators in Python")
        st.write("In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.")
        code14 = """
in       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     #True if value is found in the sequence\n
not in    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    #True if value is not found in the sequence
"""
        st.info(code14)
        st.write(" **Example of Menbership Operators in Python** ")
        st.text("Input")
        code15 = """
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
"""
        st.code(code15, language="python")
        st.text("Output")
        code16 = """
x is NOT present in given list\n
y is present in given list
"""
        st.success(code16)
        st.subheader("Ternary Operator in Python")
        st.write("in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. ")
        st.write("It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.")
        st.info("Syntax :  [on_true] if [expression] else [on_false] ")
        st.write(" **Examples of Ternary Operator in Python** ")
        st.text("Input")
        code17 = """
a, b = 10, 20
min = a if a < b else b

print(min)
"""
        st.code(code17, language="python")
        st.text("Output")
        st.success("10")
        st.subheader("Precedence and Associativity of Operators in Python")
        st.write("In Python, Operator precedence and associativity determine the priorities of the operator.")
        st.write(" **Operator Precedence in Python** ")
        st.write("This is used in an expression with more than one operator with different precedence to determine which operation to perform first")
        st.write(" **Example:** The code first calculates and prints the value of the expression 10 + 20 * 30, which is 610. Then, it checks a condition based on the values of the ‘name’ and ‘age’ variables. Since the name is “Alex” and the condition is satisfied using the or operator, it prints “Hello! Welcome.” ")
        st.text("Input")
        code18 = """
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")
"""
        st.code(code18, language="python")
        st.text("Output")
        code19 = """
610\n
Hello! Welcome.
"""
        st.success(code19)
        st.write(" **Operator Associativity in Python** ")
        st.markdown("""
If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine. It can either be Left to Right or from Right to Left.

The following code shows how Operator Associativity in Python works:
""")
        data5 = {"Precedence": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                "Operators": ["()", "x[index], x[index:index]", "await x", "**", "+x, -x, ~x", "*, @, /, //, %", "+, –", "<<, >>", "&", "^", "|", "in, not in, is, is not, <, <=, >, >=, !=, =", "not x", "and", "or", "if-else", "lambda", ":="],
                "Description": ["Parentheses", "Subscription, slicing", "Await expression", "Exponentiation", "Positive, negative, bitwise NOT", "Multiplication, matrix, division, floor division, remainder", "Addition and subtraction", "Shifts", "Bitwise AND", "Bitwise XOR", "Bitwise OR", "Comparisons, membership tests, identity tests", "Boolean NOT", "Boolean AND", "Boolean OR", "Conditional expression", "Lambda expression", "Assignment expression (walrus operator)"],
                "Associativity": ["Left to right", "Left to right", "N/A", "Right to left", "Right to left", "Left to right", "Left to right", "Left to right", "Left to right", "Left to right", "Left to right", "Left to Right", "Right to left", "Left to right", "Left to right", "Right to left", "N/A", "Right to left"]}
        df5 = pd.DataFrame(data5)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.table(df5)
        st.markdown("""
**Example:** The code showcases various mathematical operations. It calculates and prints the results of division and multiplication, addition and subtraction, subtraction within parentheses, and exponentiation. The code illustrates different mathematical calculations and their outcomes.
""")
        st.text("Input")
        code20 = """
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)
"""
        st.code(code20, language="python")
        st.text("Output")
        code21 = """
100.0\n
6\n
0\n
512
"""
        st.success(code21)



    if selected == 9:
        st.header("Conditional Statements in Python")
        st.write("Conditional Statements are statements in Python that provide a choice for the control flow based on a condition. It means that the control flow of the Python program will be decided based on the outcome of the condition. Now let us see how Conditional Statements are implemented in Python.")
        st.markdown("""
Types of Conditional Statements in Python
1. If Conditional Statement in Python
2. If else Conditional Statements in Python
3. Nested if..else Conditional Statements in Python
4. If-elif-else Conditional Statements in Python
5. Ternary Expression Conditional Statements in Python
Best Practices for Using Conditional Statements
""")
        st.subheader("1. If Conditional Statement in Python")
        st.write("If the simple code of block is to be performed if the condition holds then the if statement is used. Here the condition mentioned holds then the code of the block runs otherwise not.")
        st.write(" **Syntax of If Statement:** ")
        code1 = """
if condition:\n
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Statements to execute if\n
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# condition is true
"""
        st.info(code1)
        st.text("Input")
        code2 = """
# if statement example
if 10 > 5:
    print("10 greater than 5")

print("Program ended")
"""
        st.code(code2, language="python")
        st.text("Output")
        code3 = """
10 greater than 5\n
Program ended
"""
        st.success(code3)
        st.subheader("2. If else Conditional Statements in Python")
        st.write("In a conditional if Statement the additional block of code is merged as an else statement which is performed when if condition is false.")
        st.write(" **Syntax of Python If-Else:** ")
        code4 = """
if (condition):\n
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Executes this block if\n
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# condition is true\n
else:\n
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Executes this block if\n
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# condition is false
"""
        st.info(code4)
        st.text("Input")
        code5 = """
# if..else statement example
x = 3
if x == 4:
    print("Yes")
else:
    print("No")
"""
        st.code(code5, language="python")
        st.text("Output")
        st.success("No")
        st.subheader("3. Nested if..else Conditional Statements in Python")
        st.write("Nested if..else means an if-else statement inside another if statement. Or in simple words first, there is an outer if statement, and inside it another if – else statement is present and such type of statement is known as nested if statement. We can use one if or else if statement inside another if or else if statements.")
        st.text("Input")
        code6 = """
# if..else chain statement
letter = "A"

if letter == "B":
    print("letter is B")

else:

    if letter == "C":
        print("letter is C")

    else:

        if letter == "A":
            print("letter is A")

        else:
            print("letter isn't A, B and C")
"""
        st.code(code6,language="python")
        st.text("Output")
        st.success("letter is A")
        st.subheader("4. If-elif-else Conditional Statements in Python")
        st.write("The if statements are executed from the top down. As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final “else” statement will be executed.")
        st.text("Input")
        code7 = """
# if-elif statement example
letter = "A"

if letter == "B":
    print("letter is B")

elif letter == "C":
    print("letter is C")

elif letter == "A":
    print("letter is A")

else:
    print("letter isn't A, B or C")
"""
        st.code(code7, language="python")
        st.success("letter is A")
        st.subheader("5. Ternary Expression Conditional Statements in Python")
        st.write("The Python ternary Expression determines if a condition is true or false and then returns the appropriate value in accordance with the result. The ternary Expression is useful in cases where we need to assign a value to a variable based on a simple condition, and we want to keep our code more concise — all in just one line of code.")
        st.write(" **Syntax of Ternary Expression** ")
        code8 = """
Syntax: [on_true] if [expression] else [on_false] \n
expression: conditional_expression | lambda_expr
"""
        st.info(code8)
        

















