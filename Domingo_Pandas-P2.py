{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bccfe7dc-f59e-4485-af04-7b102b0c7442",
   "metadata": {},
   "source": [
    "Problem 2. Letter a."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7eb30c6a-5ef8-4cfb-8e7a-8279acf4a9b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              Model  cyl  hp    wt  vs  gear\n",
      "          Mazda RX4    6 110 2.620   0     4\n",
      "      Mazda RX4 Wag    6 110 2.875   0     4\n",
      "         Datsun 710    4  93 2.320   1     4\n",
      "     Hornet 4 Drive    6 110 3.215   1     3\n",
      "  Hornet Sportabout    8 175 3.440   0     3\n",
      "            Valiant    6 105 3.460   1     3\n",
      "         Duster 360    8 245 3.570   0     3\n",
      "          Merc 240D    4  62 3.190   1     4\n",
      "           Merc 230    4  95 3.150   1     4\n",
      "           Merc 280    6 123 3.440   1     4\n",
      "          Merc 280C    6 123 3.440   1     4\n",
      "         Merc 450SE    8 180 4.070   0     3\n",
      "         Merc 450SL    8 180 3.730   0     3\n",
      "        Merc 450SLC    8 180 3.780   0     3\n",
      " Cadillac Fleetwood    8 205 5.250   0     3\n",
      "Lincoln Continental    8 215 5.424   0     3\n",
      "  Chrysler Imperial    8 230 5.345   0     3\n",
      "           Fiat 128    4  66 2.200   1     4\n",
      "        Honda Civic    4  52 1.615   1     4\n",
      "     Toyota Corolla    4  65 1.835   1     4\n",
      "      Toyota Corona    4  97 2.465   1     3\n",
      "   Dodge Challenger    8 150 3.520   0     3\n",
      "        AMC Javelin    8 150 3.435   0     3\n",
      "         Camaro Z28    8 245 3.840   0     3\n",
      "   Pontiac Firebird    8 175 3.845   0     3\n",
      "          Fiat X1-9    4  66 1.935   1     4\n",
      "      Porsche 914-2    4  91 2.140   0     5\n",
      "       Lotus Europa    4 113 1.513   1     5\n",
      "     Ford Pantera L    8 264 3.170   0     5\n",
      "       Ferrari Dino    6 175 2.770   0     5\n",
      "      Maserati Bora    8 335 3.570   0     5\n",
      "         Volvo 142E    4 109 2.780   1     4\n"
     ]
    }
   ],
   "source": [
    "import pandas\n",
    "\n",
    "car = pandas.read_csv('cars.csv')\n",
    "odd_column = car.columns[0::2]\n",
    "car_list = car[odd_column]\n",
    "car_head_5 = car_list.head(5)\n",
    "\n",
    "print(car_list.to_string(index=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "95e4f2a7-fc96-49a1-917e-7a977578f57a",
   "metadata": {},
   "source": [
    "Problem 2. Letter b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fddd3c08-ed83-414b-a49b-40b2dce8b5c9",
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
   "id": "c7d4888f-9b9e-43f7-a5a1-e118f929956d",
   "metadata": {},
   "source": [
    "Problem 2. Letter c."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f71dd5c7-5798-4900-b526-cf024d0853d7",
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
   "id": "57fbf4d8-f154-4cb2-84d2-eda0d10ea8ec",
   "metadata": {},
   "source": [
    "Problem 3. Letter d."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a78ca17f-8089-43a2-9727-13d9a9cf02e9",
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
   "id": "b1582ff1-e081-40a5-a6c7-73e4b71283d7",
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
