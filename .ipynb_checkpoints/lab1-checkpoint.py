{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1452   <class 'int'>\n",
      "11.23   <class 'float'>\n",
      "(1+2j)   <class 'complex'>\n",
      "True   <class 'bool'>\n",
      "University of Maryland   <class 'str'>\n",
      "(0, -1)   <class 'tuple'>\n",
      "[5, 12]   <class 'list'>\n",
      "{'class': '404', 'section': 'A'}   <class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "datalist = [1452, 11.23, 1+2j, True, 'University of Maryland', (0, -1), [5, 12], {\"class\":'404', \"section\":'A'}]\n",
    "\n",
    "for i in datalist:\n",
    "    print(i, \" \", type(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=int(input(\"Select operation: 1.ADD 2.Subtract 3.Multiply 4.Divide\"))\n",
    "if(x==1):\n",
    "    i=y+z\n",
    "    print(y, \" + \", z, \" = \", i)\n",
    "    \n",
    "elif(y==2):\n",
    "    i=y-z\n",
    "    print(y, \" - \", z, \" = \", i)\n",
    "\n",
    "elif(y==3):\n",
    "    i=y*z\n",
    "    print(y, \" * \", z, \" = \", i)\n",
    "\n",
    "elif(y==3):\n",
    "    i=y/z\n",
    "    print(y, \" / \", z, \" = \", i)    \n",
    "    \n",
    "else:\n",
    "    print(\"Enter a valid choice\")\n",
    "    \n",
    "y=int(input(\"Enter first number\"))\n",
    "z=int(input(\"Enter second number\"))    \n",
    "    "
   ]
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
