#The goal of this exercise is to observe how Python handles different built-in data
#structures by applying modifications that respect their intrinsic properties (mutability,
#immutability, ordering, and uniqueness).
#You must modify the existing objects using operations specific to their types (list
#method, set method, dictionary assignment, tuple concatenation), rather than recreating
#them or hardcoding the final values, in order to display the following greetings: "Hello
#World", "Hello «country of your campus»", "Hello «city of your campus»", "Hello «name
#of your campus»".*/

ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
ft_list.append("world")
ft_tuple = ("hello", "germany")
ft_set.remove("tutu!")
ft_set.add("Berlin")
ft_dict["Hello"] = "42berlin"
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)



#Expected output:
#$>python Hello.py | cat -e
#['Hello'
#,
#'World!']$
#('Hello'
#,
#'France!')$
#{'Hello'
#,
#'Paris!'}$
#{'Hello': '42Paris!'}$
