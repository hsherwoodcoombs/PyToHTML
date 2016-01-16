# def generate_comment automatically generates syntatical comments for a code
# takes a type (python/html/css), does (keyword function- class/object), name
def generate_comment(type, name, aComment):
	myComment = name + aComment
	if type is 'python':
		print '#' + myComment

# generates the automatic syntax for the html file header
def generate_HTML():
	html_head = '''
	<!DOCTYPE html>
	<html>
	<head>
	
		<title>Part 3</title> 
		<link rel="stylesheet" href="myStyle.css">

	</head>

	<body>
	
	'''
	html_nav = '''
	<div class="nav">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="unit1.html">Unit 1</a></li>
        <li><a href="unit2.html">Unit 2</a></li>
        <li><a href="unit3.html">Unit 3</a></li>
      </ul>
    </div>
	
	<h1>Lesson 3: Telling Computers what to Do</h1>
	'''
	full_html = html_head + html_nav
	return full_html

def generate_HTML_foot():
	html_footer = '''
	</body>
	</html>
	'''
	return html_footer

def generate_concept_HTML(lesson_title, lesson_description):
    html_text_1 = '''
<div class="concept">
    <div class="lesson-title"> <h2>
        ''' + lesson_title
    html_text_2 = ''' </h2>
    </div>
    <div class="lesson-description">
        ''' + lesson_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

myText = """TITLE: Introduction to Serious Programming
DESCRIPTION: It is a foolish assumption to think that computers are intelligent. It is actually the
engineers of these computers that are responsible for creating a series of programs to interpret human
commands. Python is a high level programming language- that is its code closer resembles a human language
as apposed to machine language. Python forms <b>backus naur form</b> where expressions may take the similar
form of a sentance: subject + verb + object. 
TITLE: Variables and Strings
DESCRIPTION: Variables enable a link between names and values to avoid repetition and avoiod confusion. 
Variables are assigned to values through an assigment: <br>
my_variable = 200 ---> you would read this as "my_variable gets 200". 
TITLE: Input --> Function --> Output 
DESCRIPTION: A function is something that may or may not take input, performs an action (or many), and produces a result. Functions
are defined by the keyword <b>'def():'</b>. Here are some examples:<br><br>
def hello(name):
	return "Hello " + name + "!"

	<i>Above we have defined the function Hello. Next, we will call function hello. </i>

print hello('world') 
	<i>The function should return: Hello world!</i>
<br>Hint: In python the characters ' and " can be used interchangeably 
<br><b>Why use functions?</b> Good question! Using functions are good programming practice. Functions reduce reptition and make
code more understandable to all members reading it. Functions are also the first stepping stones to object oriented programming. 
TITLE: Control Flow Loops
DESCRIPTION: Procedural thinking is an impportant mind set for a good programmer. It is impportant to think about repetition and 
decision making when desiging your code, procedural thinking helps exactly with this. A common way to tackle large programs is to 
implement loops like the 'if' and 'while' loops. <br> <br>
The common syntax for the <b>IF statement</b> is: <br>
if &lt;test expression&gt;: <br>
&lt;block&gt;

<br> The if statement is great in situations when you are testing if an expression meets a requirement. Where as, the <b>while</b> statement 
while continue executing until a condition failes. Below is the basic syntax: <br><br>
	While &lt;test expression&gt;:<br>
	&lt;block&gt;
TITLE: Debugging
DESCRIPTION: There are five strategies commonly used in debugging a programming: <br>
<ol>
	<li>Examine error messages when programs crash</li>
	<li>Work from example code </li>
	<li>Make sure examples work </li>
	<li>Check (print) intermediate results </li>
	<li>Keep and compare old versions </li>
</ol>
TITLE: Structured Data: Lists, Loops, and Strings
DESCRIPTION: A <b>string</b> is considered a type of structured data because it can be broke down into characters and operate
on sub-sequences among itself. Lists, in comparison, are more powerful. <b>Lists</b>, another type of structured data, can handle multiple
data types (characters, strings, numbers, even other lists). To declare a list you declare: <br><br>
myList = ['h','e','l','l','o','!'] <br> 
and to access a specific element you would write<br>
myList[0] <i> it is important to rember that lists begin with element 0</i>. So myList[0] would point to the letter 'h'. <br><br>
Lists are also considered <b>mutable</b> (lists are not). When someone says a list is mutable it means it can be mutated in 
various methods. As example we can change the variable of element 5 in our myList sequence: <br><br>
myList[5] =  '~' <br><br>
We can also get funky and nest lists!<br>
Example: <br><br>
inventory = [['apples', 2],
			['bananas',6],
			['oranges', 3]]
<br><br>
We can also perform a substantial number of <b>list operations</b> with our lists. <br>
<ol>
	<li>Append: The append method adds a new element to the end of a list. 
	The append method mutates the list that it is invoked on, it does not create a new list. </li>
	<li>Concatenation: The + operator can be used with lists and is very similar to how it is used to 
	concatenate strings. It produces a new list, it does not mutate either of the input lists. </li>
	<li>Len: The len operator can be used to find out the length of an object. The len operator works 
	for many things other than lists, it works for any object that is a collection of things 
	including strings. The output from len is the number of elements in its input. </li>
	<li>While: Since lists are collections of things, it is very useful to be able to go through a list 
	and do something with every element. </li>
	<li>Index: The index method is invoked on a list by passing in a value, and the output is the first 
	position where that value sits in the list. If the list that does not contain any occurrences of the 
	value you 17 pass in, index produces an error (this is different from the find method for strings 
	which we used in Unit 1, that returns a -1 when the target string is not found).</li>
</ol>
TITLE: How to Solve Problems
DESCRIPTION: Mastering procedural thinking and debugging are important for all programmers but successful 
programmers systematically aproach solving problems. Here are some steps to get started: <br>
<ol>
	<li>What are the inputs? <br> First make sure you understand the problem (even if you don't know how to 
		translate it to computer language)- what are the inputs and outputs. <br></li>
	<li>How are inputs/outputs represented? <br> What form is the form of the input(s) and output(s)? Does the input
	morph or change data types before being outputted? <br></li>
	<li>Solve the problem: <br> Its a good idea to first break your problem up into baby-steps even if you have succesfully
	completed all the aforementioned steps, consider writing pseudo-code to bring your ideas together. Another practice is to 
	work out some examples to test your methods. <br></li>
	<li>Consider systematically how a human solves the problem and dont optimize prematurely</li>
</ol>
"""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html

print generate_HTML()

print generate_all_html(myText)

print generate_HTML_foot()