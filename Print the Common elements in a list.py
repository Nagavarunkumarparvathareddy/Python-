{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8d1de9d9-9bda-42c0-b615-1c7e6b627019",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 10 20 30 \n",
      " 10 2 3 4 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10]\n"
     ]
    }
   ],
   "source": [
    "lst1 = list(map(int,input().split()))\n",
    "lst2 = list(map(int,input().split()))\n",
    "common = []\n",
    "for ele in lst1:\n",
    "    if ele in lst2:\n",
    "        common.append(ele)\n",
    "print(list(set(common)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ced99436-c5e3-47bf-9303-b9da7c044629",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
