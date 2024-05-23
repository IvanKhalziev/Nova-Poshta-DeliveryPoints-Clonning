# Online Store Delivery Integration with Nova Poshta API

[Українська](#українська) | [English](#english)

---

## Українська

При написанні онлайн магазину майже завжди треба створювати вибір способу доставки для клієнта. **Нова Пошта** - це *маст хев* для сучасних проектів. У Нової Пошти також є *апі* для розробників, і там дуже багато корисної інформації. Сьогодні поговоримо тільки про **Пункти видачі замовлень** і усю інформацію до них. 

Тут ви знайдете інформацію про те, як саме усе ж таки взаємодіяти з *API* НП, та витягти інформацію. Нам треба три речі - **Області** -> **населені пункти** -> **пункти видачі**. Саме така послідовність. Без одного не зможеш отримати інформацію про інше. 

Я робив повне клонування **БД** на *джанго*, тому тут будуть також скрипти, якими я робив *фікстури* для моєї **БД**. 

### Папка з Областями
Тут є вже готовий файл з інформацією (*areas.json*). А також скрипт та файл з *фікстурами* для *джанго*. 

### Папка з Містами
Нам потрібен файл з областями (*areas_sorted.json*), а саме їх назви, адже по них ми будемо робити запити. 
- *City.py* - скрипт з реквестами і записом даних у файл (*city.json*). 
- *Filter.py* - скрипт для видалення клонів з даних, які ми отримали. Дані записуються у (*city_filtered.json*). 
- *City_fixture.py* - скрипт для створення фікстур. 

### Папка з Відділеннями
Нам, як і минулого разу, треба файл з містами (*city_filtered.json*) задля запитів саме за цими населеними пунктами. 
- *Warehouse.py* - файл з запитами, який записує дані у (*warehouse.json*). 
Далі за схемою робимо фікстури, якщо потрібні. 

Усім удачі і успіхів!

---

## English

When developing an online store, it's almost always necessary to provide a choice of delivery method for the customer. **Nova Poshta** is a must-have for modern projects. Nova Poshta also provides an *API* for developers, which contains a lot of useful information. Today, we'll focus solely on **Order Pickup Points** and all the information related to them. 

Here you'll find information on how to interact with the **NP API** and retrieve information. We need three things - **Regions** -> **Settlements** -> **Pickup Points**. That's the sequence. Without one, you won't be able to get information about the other. 

I've done a complete clone of the **DB** in *Django*, so here you'll also find scripts I used to create *fixtures* for my **DB**. 

### Folder with Regions
Here's a ready-made file with information (*areas.json*). Also, there's a script and a file with *fixtures* for *Django*.

### Folder with Cities
We need a file with regions (*areas_sorted.json*), specifically their names, as we'll be making requests based on them. 
- *City.py* - script with requests and data writing to a file (*city.json*). 
- *Filter.py* - script for removing duplicates from the data we received. Data is written to (*city_filtered.json*). 
- *City_fixture.py* - file for creating fixtures. 

### Folder with Branches
Just like last time, we need a file with cities (*city_filtered.json*) for queries specifically for these settlements. 
- *Warehouse.py* - file with queries that write data to (*warehouse.json*). 
Then, according to the scheme, we create fixtures if needed. 

Best of luck to everyone!
