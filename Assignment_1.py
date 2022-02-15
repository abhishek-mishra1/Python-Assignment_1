#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
* 
'hello'
-87.8
- 
/ 
+	
6"""
print ("Ans:-  Values are 'hello',-87.8,6 and expressions are *, -,/,+.")


# In[14]:


#What is the difference between string and variable?
print ("String: String is a data type which can be created by single quote or double quote. It could be single word or sentence.")
print("Variable: Variable is a location or space where we can store data values. Variable can store different data types. It is used to hold values. We can store string or integer or any other data type values and any words and sentences also.")


# In[15]:


#4. What is an expression made up of? What do all expressions do?

print("Expression is a combination of values, variables, operators etc. Expression need to be evaluated if you ask python to print an expression the interpreter evaluates the expression and displays the results.")


# In[16]:


#5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
print("A statement is a instruction that the python interpreter can execute. When you type a statement in the command line python executes it and displays the result. Each and every line that we write in programming is called statement.")
print("Expression is a combination of values, variables, operators etc. Expression need to be evaluated if you ask python to print an expression the interpreter evaluates the expression and displays the results. Every statement can be expression.")


# In[17]:


""""6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
"""
bacon = 22
bacon+1


# In[18]:


bacon


# In[22]:


#7. What should the values of the following two terms be?
'spam' + 'spamspam'


# In[23]:


'spam'*3


# In[24]:


#8. Why is eggs a valid variable name while 100 is invalid?
print("Because a valid variable name does not supposed to start with numbers it’s either any alphabetic, alpha-numeric or string which start with “_” without space e.g. _a = 100.")


# In[30]:


#9. What three functions can be used to get the integer, floating-point number, or string version of a value?
print("Integer: - int()")
print("Floating-point number: - float()")
print("String: - str()")


# In[33]:


#10. Why does this expression cause an error? How can you fix it?
"""Ans: Because 99 is integer and rest other is string and only string can be concatenated. that’s why this expression cause error.
To fix this error there are many methods. All methods converting integer to string below"""
print('I have eaten ' + '99 '  + ' burritos.')


# In[34]:


'I have eaten 99 burritos.'


# In[35]:


'I have eaten ' + str( 99)  + ' burritos.'


# In[ ]:




