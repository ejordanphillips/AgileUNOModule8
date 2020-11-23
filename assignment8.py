"""
Jordan Phillips
Module 8 Assignment
"""

# 1. Import my_module and prettyprint
# Add breakpoint to test your data
# View the data in your variables to check 

import my_module 
import pprint

# 2. Use the greeting method from my_module to print your name
# Add breakpoint to test your data
# View the data in your variables to check 

my_module.greeting("Jordan")

breakpoint()

# 3. Use letter_text function to print a string
# Add breakpoint to test your data
# View the data in your variables to check 

kwargs = {
    'name': 'Jordan',
    'amount': '500',
    'denomination': 'dollars',
    }

my_module.letter_text(**kwargs)

breakpoint()

# 4. Import  my_json_data and print
# Add breakpoint to test your data 
# View the data in your variables to check 

from my_module import my_json_data
print(my_json_data)

breakpoint()

# 5. Import my_json_data as my_data and print using prettyprint
# Add breakpoint to test your data
# View the data in your variables to check 

from my_module import my_json_data as my_data
pp = pprint.PrettyPrinter(indent=3)
pp.pprint(my_data)

breakpoint()





