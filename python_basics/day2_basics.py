# Step 3: variables and print

name = "Shine"
age = 30
is_engineer = True

print(name)
print(age)
print(is_engineer)

message=f"My name is {name}, I am {age} years old."
print(message)


# Step 5: if / elif / else

score = 85

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Fail")


fruits=["apple","banana","orange"]
fruits.append("grape")
fruits.remove("banana")

print(fruits)


user={"name": "shine", 
      "age": "30", 
      "email": "xxx@xxx"}

print(user["name"])
print(user.get("email"))


#step 9: function 

def greet(name: str) -> str:
    return f"hello, {name}"

result = greet("shine")
print(result)



#step 10: file I/O

with open("test.txt", "w") as f:
     f.write("hello python")

with open("test.txt", "r") as f:
     content=f.read()

print(content)	
