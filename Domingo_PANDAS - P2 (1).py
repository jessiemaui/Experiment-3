{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2093bbcb-bf22-435c-9fb6-ce469afb21e5",
   "metadata": {},
   "source": [
    "Problem 2. Letter a."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f32767d4-6065-46ac-92ab-56a44c9318c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            Model  cyl  hp    wt  vs  gear\n",
      "        Mazda RX4    6 110 2.620   0     4\n",
      "    Mazda RX4 Wag    6 110 2.875   0     4\n",
      "       Datsun 710    4  93 2.320   1     4\n",
      "   Hornet 4 Drive    6 110 3.215   1     3\n",
      "Hornet Sportabout    8 175 3.440   0     3\n"
     ]
    }
   ],
   "source": [
    "import pandas\n",
    "\n",
    "car = pandas.read_csv('cars.csv')\n",
    "odd_column = car. iloc [0:5, 0::2]\n",
    "\n",
    "print(odd_column.to_string(index=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c00f54f-02cd-4495-8f87-0893208a28e2",
   "metadata": {},
   "source": [
    "Problem 2. Letter b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8a111ad3-a47f-45d8-a47f-c43bbef759f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "         Model  mpg  cyl  disp  hp  drat    wt  qsec  vs  am  gear  carb\n",
      "    Mazda RX4 21.0    6 160.0 110   3.9 2.620 16.46   0   1     4     4\n",
      "Mazda RX4 Wag 21.0    6 160.0 110   3.9 2.875 17.02   0   1     4     4\n"
     ]
    }
   ],
   "source": [
    "import pandas\n",
    "\n",
    "car = pandas.read_csv('cars.csv')\n",
    "model = car[car['Model'].str.contains('Mazda RX4')]\n",
    "print(\"\\n\", model.to_string(index=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1ffdc25-df26-4200-afc3-05986e5d364c",
   "metadata": {},
   "source": [
    "Problem 2. Letter c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6b91eb9e-566e-46e5-8cb5-e65a06a5b233",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "The Camaro Z28 have 8 cylinders.\n"
     ]
    }
   ],
   "source": [
    "import pandas\n",
    "\n",
    "car = pandas.read_csv('cars.csv')\n",
    "model = car[car['Model'].str.contains('Camaro Z28')]\n",
    "print(\"\\nThe \" + model['Model'].to_string(index=False) + \" have \" + model['cyl'].to_string(index=False) + \" cylinders.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5ac1871-1518-4401-a5ef-47a20c79d63e",
   "metadata": {},
   "source": [
    "Problem 2. Letter d. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e71cd462-8caa-4156-ae72-460c9909a46e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "The Mazda RX4 Wag have 6 cylinders and 4 gears.\n",
      "The Ford Pantera L have 8 cylinders and 5 gears.\n",
      "The Honda Civic have 4 cylinders and 4 gears.\n"
     ]
    }
   ],
   "source": [
    "import pandas\n",
    "\n",
    "car = pandas.read_csv('cars.csv')\n",
    "output = \"\"\n",
    "\n",
    "model = car[car['Model'].str.contains('Mazda RX4 Wag')] \n",
    "output += (\"\\nThe \" + model['Model'].to_string(index=False) + \" have \" + model['cyl'].to_string(index=False) + \" cylinders and \" + model['gear'].to_string(index=False) + \" gears.\")\n",
    "model = car[car['Model'].str.contains('Ford Pantera L')] \n",
    "output += (\"\\nThe \" + model['Model'].to_string(index=False) + \" have \" + model ['cyl'].to_string(index=False) + \" cylinders and \" + model['gear'].to_string(index=False) + \" gears.\")\n",
    "model = car[car['Model'].str.contains('Honda Civic')]\n",
    "output += (\"\\nThe \" + model['Model'].to_string(index=False) + \" have \" + model['cyl'].to_string(index=False) + \" cylinders and \" + model['gear'].to_string(index=False) + \" gears.\")\n",
    "\n",
    "print(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1422f29d-521d-49a5-981a-997c721f47eb",
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
