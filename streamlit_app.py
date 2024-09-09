import streamlit as st
import streamlit_antd_components as sac
import json

# Set page config
st.set_page_config(
    page_title="chik dabak dam dam",
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
    sac.TabsItem(label='G',tag="GPT"),

], align='wide', size='lg' , color='grape', use_container_width=True, return_index=True)



#Home Section
if selecteds == 0:
    st.header("Welcome to Chik Dabak Dam Dam")
    st.subheader("Directly go the python for learning {others things are work in progress}")
    st.info("Preferred device are laptop, but if You are a Phone user so when You click on Python You will see a right facing arrow on the top left click to openup the menu. ")
    st.success("Thank You for visiting our web Appliction.")
           
if selecteds == 5:
    

    
    # Create a code editor
    code = st.text_area("Code", height=500, key="code")
    
    # Create a CodeMirror instance
    html = """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.0/codemirror.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.0/mode/python/python.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.0/codemirror.min.css">
        <style>
            .CodeMirror {
                height: 500px;
            }
        </style>
        <textarea id="code" name="code">%s</textarea>
        <script>
            var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
                lineNumbers: true,
                mode: "python",
                theme: "monokai",
                value: '%s'
            });
            editor.on('change', function() {
                document.getElementById('streamlit-component').dispatchEvent(new CustomEvent('update', { detail: editor.getValue() }));
            });
        </script>
        """ % (code, code)
    
    # Display the CodeMirror instance
    st.components.v1.html(html, height=600, scrolling=True)
    
    # Update the code when the user types
    def update_code():
        global code
        code = st.session_state.code
    
    # Run the code when the user clicks the run button
    def run_code():
        try:
            output = eval(code)
            st.write("Output:")
            st.write(output)
        except Exception as e:
            st.error(f"Error: {e}")
    
    # Add a run button
    if st.button("Run"):
        run_code()
    
    # Update the code in the session state
    st.components.v1.html("""
        <script>
            document.addEventListener('update', function(event) {
                parent.postMessage(event.detail, '*');
            });
            window.addEventListener('message', function(event) {
                if (event.data) {
                    document.getElementById('code').value = event.data;
                    editor.setValue(event.data);
                    parent.postMessage(event.detail, '*');
                }
            });
        </script>
    """)
    
    # Update the code in the session state
    st.session_state.code = code
    
    

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
                sac.MenuItem('Data Types'),
                sac.MenuItem('Operators'),
                sac.MenuItem('Control Flow'),
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
        
        print(age)
        print(salary)
        print(name)
        """
        st.code(code, language="python")
        st.text("Output")
        st.success("45")
        st.success("1456.8")
        st.success("John")






    

    if selected == 6:
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
        * **Python Arrays**
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
Type of a:  <class 'int'>
Type of b:  <class 'float'>
Type of c:  <class 'complex'>
"""
        st.code(code5, language="python")

        
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
            For 
            Life'''
print("\nCreating a multiline String: ")
print(String1)
"""
        st.code(code, language="python")
        st.text("Output")
        code1 = """
        String with the use of Single Quotes: 
        Welcome to the Basics World
        String with the use of Double Quotes: 
        I'm a Basic
        <class 'str'>
        String with the use of Triple Quotes: 
        I'm a Basic and I live in a world of "Basics"
        <class 'str'>
        Creating a multiline String: 
                    Basics 
                    For 
                    Life
        """
        st.code(code1, language="python")
        st.subheader("Accessing elements of String")
        st.write("In Python programming , individual characters of a String can be accessed by using the method of Indexing. Negative Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on.")
        st.markdown("""
        **Example:** This Python code demonstrates how to work with a string named ‘ String1′ . It initializes the string with “GeeksForGeeks” and prints it. It then showcases how to access the first character ( “G” ) using an index of 0 and the last character ( “s” ) using a negative index of -1.
        """)
        st.text("Input")
        code2 = """
String1 = "Basicslearn"
print("Initial String: ")
print(String1)
print("\nFirst character of String is: ")
print(String1[0])
print("\nLast character of String is: ")
print(String1[-1])
"""
        st.code(code2 , language="python")
        st.text("output")
        code3 = """
        Initial String: 
        Basicslearn
        First character of String is: 
        B
        Last character of String is: 
        n
        """
        st.code(code3, language="python")

        st.subheader("List Data Type in Python")
        st.write("Lists are just like arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type.")
        st.markdown("""
        **Creating a List in Python**
        """)
        st.write("Lists in Python can be created by just placing the sequence inside the square brackets[].")
        
        




        
    
