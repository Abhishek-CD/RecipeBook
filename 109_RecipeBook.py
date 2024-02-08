class Recipe :
    def __init__(self) :
        self.name = input('Enter Recipe Name : ').strip().title()
        self.ingredients = input('Enter Ingredients :')
        self.directions = input('Enter Cooking Directions : ')
    def VegRecipe(self) :
        vegList = [self.name,'\n','INGREDIENTS : ',self.ingredients,'\n','DIRECTIONS : ',self.directions,'\n']
        with open('C:\\Users\\Abhi\\Desktop\\python\\veg\\VegBook.txt','a') as v :
            v.writelines(vegList)
            with open('lofgfile.txt','a')as logFile :
                logFile.write(f'\n...New veg recipe {self.name} added...')

    def NonvegRecipe(self) :
        NonvegList = [self.name,'\n','INGREDIENTS : ',self.ingredients,'\n','DIRECTIONS : ',self.directions,'\n']
        with open('C:\\Users\\Abhi\\Desktop\\python\\nonveg\\NonVegBook.txt','a') as v :
            v.writelines(NonvegList)
            with open('lofgfile.txt','a')as logFile :
                logFile.write(f'\n...New nonveg recipe {self.name} added...')

def vegNonveg() :
    while True :
        vegOrNonveg = input('VEG OR NONVEG ??? : ').lower().strip()
        if vegOrNonveg == 'veg' or vegOrNonveg == 'nonveg' or vegOrNonveg == 'non veg' :
            return vegOrNonveg
        else :
            continue
def ShowVeg() :
    try :
        with open('C:\\Users\\Abhi\\Desktop\\python\\veg\\VegBook.txt','r') as v :
                veg = v.read()
                return veg
    except FileNotFoundError :
        print("No file named 'VegBook.txt'")
        raise SystemExit

def ShowNonVeg() :
    try:
        with open('C:\\Users\\Abhi\\Desktop\\python\\nonveg\\NonVegBook.txt','r') as v :
                nonveg = v.read()
                return nonveg
    except FileNotFoundError :
        print("No file named 'NonVegBook.txt'")
        raise SystemExit

def SearchVeg() :
    vegFood = ShowVeg()
    listVeg = vegFood.splitlines()
    search = input('Enter Recipe Name : ').strip().title()
    if search in listVeg :
        searchIndex = listVeg.index(search)
        print(f'RECIPE : {listVeg[searchIndex]}\n{listVeg[searchIndex + 1]}\n{listVeg[searchIndex + 2]}')
    else :
        print("RECIPE NOT FOUND!!!")
def searchNonveg() :
    nonvegFood = ShowNonVeg()
    listNonveg = nonvegFood.splitlines()
    search = input('Enter Recipe Name : ').strip().title()
    if search in listNonveg :
        searchIndex = listNonveg.index(search)
        print(f'RECIPE : {listNonveg[searchIndex]}\n{listNonveg[searchIndex + 1]}\n{listNonveg[searchIndex + 2]}')
    else :
        print("RECIPE NOT FOUND!!!")
def removeVeg() :
    vegFood = ShowVeg()
    listVeg = vegFood.splitlines()
    search = input('Enter Recipe Name : ').strip().title()
    if search in listVeg :
        searchIndex = listVeg.index(search)
        listVeg.pop(searchIndex)
        listVeg.pop(searchIndex)
        listVeg.pop(searchIndex)
        v = open('C:\\Users\\Abhi\\Desktop\\python\\veg\\VegBook.txt','w')
        for listElmnt in listVeg :
            v.write(listElmnt)
            v.write('\n')
        v.close()
        with open('lofgfile.txt','a')as logFile :
                logFile.write(f'\n...veg recipe {search} removed...')
        print(f'RECIPE {search} IS REMOVED')
    else :
        print("SEARCH RECIPE NOT FOUND!!!")

def removeNonVeg() :
    NonvegFood = ShowNonVeg()
    listNonveg = NonvegFood.splitlines()
    search = input('Enter Recipe Name : ').strip().title()
    if search in listNonveg :
        searchIndex = listNonveg.index(search)
        listNonveg.pop(searchIndex)
        listNonveg.pop(searchIndex)
        listNonveg.pop(searchIndex)
        nv = open('C:\\Users\\Abhi\\Desktop\\python\\nonveg\\NonVegBook.txt','w')
        for listElmnt in listNonveg :
            nv.write(listElmnt)
            nv.write('\n')
        nv.close()
        with open('lofgfile.txt','a')as logFile :
                logFile.write(f'\n...nonveg recipe {search} removed...')
        print(f'RECIPE {search} IS REMOVED')
    else :
        print("SEARCH RECIPE NOT FOUND!!!")

print('RECIPE BOOK')
while True :
    opt = int(input('\n1.SHOW RECIPES   \t2.ADD RECIPES   \t3.SEARCH RECIPES\t4.REMOVE RECIPE   \t5.BREAK\nENTER(1/2/3/4/5) : '))
    if opt == 1 :
        vegOrNonveg = vegNonveg()
        if vegOrNonveg == 'veg' :
            print(ShowVeg())
        else :
            print(ShowNonVeg())
    elif opt == 2 :
        vegOrNonveg = vegNonveg()
        NewRecipe = Recipe()
        if vegOrNonveg == 'veg' :
            NewRecipe.VegRecipe()
        else :
            NewRecipe.NonvegRecipe()
    elif opt == 3 :
        vegOrNonveg = vegNonveg()
        if vegOrNonveg == 'veg' :
            SearchVeg()
        else :
            searchNonveg()
    elif opt == 4 :
        vegOrNonveg = vegNonveg()
        if vegOrNonveg == 'veg' :
            removeVeg()
        else :
            removeNonVeg()
    elif opt == 5 :
        break
    else :
        print('ENTER VALID NUMBER!!!')
        continue