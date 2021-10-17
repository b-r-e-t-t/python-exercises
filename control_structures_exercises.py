{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3b915792",
   "metadata": {},
   "source": [
    "1.\n",
    "a."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "30853dc5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What day is it? monday\n",
      "Looks like somebody's got a case of the Monday's\n"
     ]
    }
   ],
   "source": [
    "day_of_the_week = input(\"What day is it? \")\n",
    "\n",
    "if (day_of_the_week == \"Monday\" or day_of_the_week == \"monday\"):\n",
    "      print(\"Looks like somebody's got a case of the Monday's\")\n",
    "else:\n",
    "      print(\"Lucky for you it's not Monday!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41ab66fc",
   "metadata": {},
   "source": [
    "b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a910710e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What day is it? aklsdjf\n",
      "I don't know if you understand how this game works.\n"
     ]
    }
   ],
   "source": [
    "day_of_the_week = input(\"What day is it? \")\n",
    "\n",
    "if (day_of_the_week == \"Monday\" or day_of_the_week == \"monday\"\n",
    "    or day_of_the_week == \"Tuesday\" or day_of_the_week == \"tuesday\"\n",
    "    or day_of_the_week == \"Wednesday\" or day_of_the_week == \"wednesday\"\n",
    "    or day_of_the_week == \"Thursday\" or day_of_the_week == \"thursday\"\n",
    "    or day_of_the_week == \"Friday\" or day_of_the_week == \"friday\"):\n",
    "    print(\"A weekday?! How dreary\")\n",
    "elif (day_of_the_week == \"Saturday\" or day_of_the_week == \"saturday\" \n",
    "    or day_of_the_week == \"Sunday\" or day_of_the_week == \"sunday\"):\n",
    "    print(\"I am doing nothing but sitting and watching football all weekend\")\n",
    "else:\n",
    "    print(\"I don't know if you understand how this game works.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cbecb4c8",
   "metadata": {},
   "source": [
    "c. create variables and make up values for\n",
    "\n",
    "- the number of hours worked in one week\n",
    "- the hourly rate\n",
    "- how much the week's paycheck will be\n",
    "\n",
    "write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f4c5c07a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You will be paid: 5,000.00\n"
     ]
    }
   ],
   "source": [
    "hours_worked = 80.00\n",
    "hourly_rate = 50.00\n",
    "paycheck_total = 0\n",
    "\n",
    "if hours_worked <= 40:\n",
    "    paycheck_total = round((hours_worked * hourly_rate), 2)\n",
    "    print(\"You will be paid: {:,.2f}\".format(paycheck_total)) #Formatting options\n",
    "elif hours_worked > 40:\n",
    "    paycheck_total = (40 * hourly_rate) + ((hours_worked - 40) * (hourly_rate * 1.5))\n",
    "    print(\"You will be paid: {:,.2f}\".format(paycheck_total))\n",
    "else:\n",
    "    print(\"There is a glitch in the Matrix\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b09bfc8",
   "metadata": {},
   "source": [
    "2. Loop Basics\n",
    "\n",
    "    a. While\n",
    "       - Create an integer variable i with a value of 5.\n",
    "       - Create a while loop that runs so long as i is less than or equal to 15\n",
    "       - Each loop iteration, output the current value of i, then increment i by one."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4a04d3aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "while i <= 15:\n",
    "    print(i)\n",
    "    i += 1    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e80d2cb",
   "metadata": {},
   "source": [
    "    - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "751d7e66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "i = 0\n",
    "while i <= 100:\n",
    "    print(i)\n",
    "    i += 2   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5a14267d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n",
      "0\n",
      "-5\n",
      "-10\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "while i >= -10:\n",
    "    print(i)\n",
    "    i -= 5 "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e738310",
   "metadata": {},
   "source": [
    "    - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "738bc841",
   "metadata": {},
   "source": [
    "- Write a loop that uses print to create the output shown below. (100 down to 5 by 5s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "005aa56d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "i = 100\n",
    "while i >= 5:\n",
    "    print(i)\n",
    "    i -= 5 "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e77a61d",
   "metadata": {},
   "source": [
    "b. For Loops\n",
    "\n",
    "    i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "2cde6299",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 3245\n",
      "3245  x  1  =  3245\n",
      "3245  x  2  =  6490\n",
      "3245  x  3  =  9735\n",
      "3245  x  4  =  12980\n",
      "3245  x  5  =  16225\n",
      "3245  x  6  =  19470\n",
      "3245  x  7  =  22715\n",
      "3245  x  8  =  25960\n",
      "3245  x  9  =  29205\n",
      "3245  x  10  =  32450\n",
      "32450\n"
     ]
    }
   ],
   "source": [
    "user_number = int(input(\"Enter a number: \"))\n",
    "\n",
    "for i in range(1,11):\n",
    "    total = i * user_number\n",
    "    print(user_number, ' x ', i, ' = ', total)\n",
    "\n",
    "print(i * user_number)\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "2919ae2a",
   "metadata": {},
   "source": [
    "    ii. Create a for loop that uses print to create the output shown below.\n",
    "\n",
    "\n",
    "    1\n",
    "    22\n",
    "    333\n",
    "    4444\n",
    "    55555\n",
    "    666666\n",
    "    7777777\n",
    "    88888888\n",
    "    999999999"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9456cb24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n",
      "666666\n",
      "7777777\n",
      "88888888\n",
      "999999999\n"
     ]
    }
   ],
   "source": [
    "for num in range(1,10):\n",
    "    print(str(num) * num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a8921cf",
   "metadata": {},
   "source": [
    "c. break and continue\n",
    "\n",
    "    i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28232b4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    user_number = int(input(\"Enter an odd number between 1 and 50: \"))\n",
    "    if (user_number % 2 == 1) and (user_number > 0) and (user_number < 50):  #Validate user inputd as odd between 1 & 50\n",
    "        break\n",
    "    print(\"Apparently you don't understand how the game is played, please try again.\")\n",
    "\n",
    "print(\"Number to skip is\", user_number)\n",
    "for i in range(1,50,2):  #Loop through 1 to 50 counting by 2\n",
    "    if (i == user_number):\n",
    "        print(\"Yikes! Skipping number \", user_number)\n",
    "    else:\n",
    "        print(\"Here is an odd number: \", i)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73fb6fb2",
   "metadata": {},
   "source": [
    "d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "7e8bbf53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a positive integer:4\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "while 1 == 1:\n",
    "    user_input = int(input(\"Enter a positive integer:\"))\n",
    "    if (user_input > 0):\n",
    "        break\n",
    "    print(\"Apparently you don't understand how the game is played, please try again.\")\n",
    "\n",
    "for i in range(0, user_input + 1):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a43721be",
   "metadata": {},
   "source": [
    "e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "40d72552",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a positive integer:4\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "while 1 == 1:\n",
    "    user_input = int(input(\"Enter a positive integer:\"))\n",
    "    if (user_input > 0):\n",
    "        break\n",
    "    print(\"Apparently you don't understand how the game is played, please try again.\")\n",
    "\n",
    "#Counts down from the user input given\n",
    "for i in range(user_input, 0, -1):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bff246a0",
   "metadata": {},
   "source": [
    "3. Fizzbuzz\n",
    "\n",
    "One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.\n",
    "\n",
    "- Write a program that prints the numbers from 1 to 100.\n",
    "- For multiples of three print \"Fizz\" instead of the number\n",
    "- For the multiples of five print \"Buzz\".\n",
    "- For numbers which are multiples of both three and five print \"FizzBuzz\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "1051de67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "Buzz\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "Buzz\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "FizzBuzz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "Buzz\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "Buzz\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "FizzBuzz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "Buzz\n",
      "Fizz\n",
      "52\n",
      "53\n",
      "Fizz\n",
      "Buzz\n",
      "56\n",
      "Fizz\n",
      "58\n",
      "59\n",
      "FizzBuzz\n",
      "61\n",
      "62\n",
      "Fizz\n",
      "64\n",
      "Buzz\n",
      "Fizz\n",
      "67\n",
      "68\n",
      "Fizz\n",
      "Buzz\n",
      "71\n",
      "Fizz\n",
      "73\n",
      "74\n",
      "FizzBuzz\n",
      "76\n",
      "77\n",
      "Fizz\n",
      "79\n",
      "Buzz\n",
      "Fizz\n",
      "82\n",
      "83\n",
      "Fizz\n",
      "Buzz\n",
      "86\n",
      "Fizz\n",
      "88\n",
      "89\n",
      "FizzBuzz\n",
      "91\n",
      "92\n",
      "Fizz\n",
      "94\n",
      "Buzz\n",
      "Fizz\n",
      "97\n",
      "98\n",
      "Fizz\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,101):\n",
    "    if (i % 3 == 0) and (i % 5 == 0):\n",
    "        print(\"FizzBuzz\")\n",
    "    elif (i % 3 == 0):\n",
    "        print(\"Fizz\")\n",
    "    elif (i % 5 == 0):\n",
    "        print(\"Buzz\")\n",
    "    else:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74259ded",
   "metadata": {},
   "source": [
    "4. Display a table of powers.\n",
    "\n",
    "- Prompt the user to enter an integer.\n",
    "- Display a table of squares and cubes from 1 to the value entered.\n",
    "- Ask if the user wants to continue.\n",
    "- Assume that the user will enter valid data.\n",
    "- Only continue if the user agrees to."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "ce136817",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What would you like to go up to:5\n",
      "Here is your table!\n",
      "\n",
      "number | squared | cubed\n",
      "1  |  1  |  1\n",
      "2  |  4  |  8\n",
      "3  |  9  |  27\n",
      "4  |  16  |  64\n",
      "5  |  25  |  125\n",
      "Would you like to continue? y/n: n\n"
     ]
    }
   ],
   "source": [
    "while 1 == 1:\n",
    "    user_input = int(input(\"What would you like to go up to:\"))\n",
    "    print(\"Here is your table!\")\n",
    "    print(\"\")\n",
    "    print(\"number | squared | cubed\")\n",
    "    for i in range(1, user_input +1):\n",
    "        print(i, \" | \", i**2, \" | \", i**3)\n",
    "    go_again = input(\"Would you like to continue? y/n: \")\n",
    "    if go_again == 'n':\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29287f9c",
   "metadata": {},
   "source": [
    "5. Convert given number grades into letter grades.\n",
    "\n",
    " - Prompt the user for a numerical grade from 0 to 100.\n",
    " - Display the corresponding letter grade.\n",
    " - Prompt the user to continue.\n",
    " - Assume that the user will enter valid integers for the grades.\n",
    " - The application should only continue if the user agrees to.\n",
    " - Grade Ranges:\n",
    "\n",
    "     - A : 100 - 88\n",
    "     - B : 87 - 80\n",
    "     - C : 79 - 67\n",
    "     - D : 66 - 60\n",
    "     - F : 59 - 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "f5f20b04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter grade between 0 and 100: 5\n",
      "Your letter grade was an F.\n",
      "Would you like to continue? y/n: n\n"
     ]
    }
   ],
   "source": [
    "while 1 == 1:\n",
    "    while 1 == 1:\n",
    "        user_number = int(input(\"Enter grade between 0 and 100: \"))\n",
    "        if (user_number >= 0) and (user_number <= 100): #Validate user inputd as odd between ) & 100\n",
    "            break\n",
    "        print(\"Apparently you don't understand how the game is played, please try again.\")\n",
    "    if user_number <= 59:\n",
    "        print(\"Your letter grade was an F.\")\n",
    "    elif user_number <= 66:\n",
    "        print(\"Your letter grade was a D.\")\n",
    "    elif user_number <= 79:\n",
    "        print(\"Your letter grade was a C.\")\n",
    "    elif user_number <= 87: \n",
    "        print(\"Your letter grade was a B.\")\n",
    "    elif user_number <= 100:\n",
    "        print(\"Your letter grade was an A.\")\n",
    "    else:\n",
    "        print (\"There is a glitch in the Matrix.\")\n",
    "    go_again = input(\"Would you like to continue? y/n: \")\n",
    "    if go_again == 'n':\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5153c872",
   "metadata": {},
   "source": [
    "6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.\n",
    "\n",
    "- Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "ba3d2bfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "books = [\n",
    "    {\n",
    "        'title' : 'LikeWar',\n",
    "        'author' : 'PJ Singer',\n",
    "        'genre' : 'Non-fiction'\n",
    "    },\n",
    "    {\n",
    "        'title' : 'Seven Habits of Highly Effective People',\n",
    "        'author' : 'Stephen Covey',\n",
    "        'genre' : 'Non-fiction'\n",
    "    },\n",
    "    {\n",
    "        'title' : 'The Lucifer Principle',\n",
    "        'author' : 'Howard Bloom',\n",
    "        'genre' : 'Non-fiction'\n",
    "    },\n",
    "    {\n",
    "        'title' : 'Still Life with Crows',\n",
    "        'author' : 'Douglas Preston & Lincoln Child',\n",
    "        'genre' : 'Mystery'\n",
    "    },\n",
    "    {\n",
    "        'title' : 'The Memoirs of Sherlock Holmes',\n",
    "        'author' : 'Arthur Conan Doyle',\n",
    "        'genre' : 'Mystery'\n",
    "    },\n",
    "    {\n",
    "        'title' : 'Murder on the Orient Express',\n",
    "        'author' : 'Agatha Christie',\n",
    "        'genre' : 'Mystery'\n",
    "    }   \n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "9dc4bfd8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a Genre: Mystery\n",
      "The following books are available in Mystery\n",
      "Still Life with Crows\n",
      "The Memoirs of Sherlock Holmes\n",
      "Murder on the Orient Express\n"
     ]
    }
   ],
   "source": [
    "user_input = input('Enter a Genre: ')\n",
    "if user_input == 'Mystery' or user_input == 'Non-fiction':\n",
    "    print(\"The following books are available in\", user_input)\n",
    "    for x in books:\n",
    "        if user_input == x['genre']:\n",
    "            print(x['title'])\n",
    "else :\n",
    "    print('Invalid input entered')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83d1fa66",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
