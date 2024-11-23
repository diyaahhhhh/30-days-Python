# Day 8: Python 30 Days Coding Challenge - "Find the Largest of Three Numbers"

**Task**:  
Write a Python program to find the largest of three numbers entered by the user.

---

### Python Code:

```python
# Day 8: Find the Largest of Three Numbers

# Input: Three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")
