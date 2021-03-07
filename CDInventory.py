#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Eric Hoyle, 03-06-21, Added CD object class)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstofCDObjects = []  # list of lists to hold data
strFileName = 'cdInventory.txt'  # data storage file
objFile = None  # file object
cdData = None

# -- PROCESSING -- #
class CD:
    """Stores data about a CD:

    properties:
        index: (int) with CD ID
        title: (string) with the title of the CD
        artist: (string) with the artist of the CD
    methods:
        __str__(): formatted string of cd attributes for presentation of inventory  
        __file_export(): formatted string of cd attributes for exporting to .txt files
    """  
    #Constructor
    def __init__(self, cdData):
        self.__index = cdData[0]
        self.__title = cdData[1]
        self.__artist = cdData[2]
        
    #Poperties
    @property
    def index(self):
        return self.__index
    
    @index.setter
    def index(self,index):
        if type(index) is not int:
            raise Exception('Index must be an integer')        
        else:
            self.__index = index
    
    @property 
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if type(title) is not str:
            raise Exception('Tile must be entered as string')
        else:
            self.__title = title.title()
   
    @property 
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, artist):
        if type(artist) is not str:
            raise Exception('Tile must be entered as string')
        else:
            self.__artist = artist.title()
    #Methods
    def __str__(self):
        return '{:<6}{:30}{:30}'.format(self.index, self.title, self.artist).title()
    
    def file_export(self):
        return '{},{},{}\n'.format(self.index,self.title,self.artist).title()
     

class DataProcessor:
    """Processing data supplied by the user"""
   
    @staticmethod   
    def list_append(cd, table):
        """Appends new cd entry as dictionary to a list of dictionaries
        
        Args: 
            cdData: Information aboout the CD 
            table: The list that the new dictionary is appended to
        
        Returns: 
            List of dictionaries with new dictionary appended to the list
        
        """

        table.append(cd)
        return table

     
class FileIO:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of 
        dictionaries

        Reads the data from file identified by file_name into a listt of objects
        one line in the file is converted to a CD object and appended to the list. 
        

        Args:
            file_name (string): name of file used to read the data from
            table (lstofCDObjects): 2D data structure (llstofCDObjects) that holds
            the data during runtime

        Returns:
            None.
        """
        try:     
            table.clear()  # this clears existing data and allows to load data from file
            with open(file_name, 'r') as objFile:
                for cdline in objFile:
                    cdinput = cdline.strip().split(',')
                    cd = CD(cdinput)
                    table.append(cd)
                    table.sort(key=lambda x:x.index, reverse=False)
        except FileNotFoundError as e:
            print('\n{:*^66}'.format((e.__doc__).upper()),
                  '\n{:^66}'.format(' WARNING: Data not loaded').upper())

    @staticmethod
    def write_file(file_name, table):
        """Function to manage data output from a list of objects to a file 

        Writes the data from a 2D table (lstofCDObjects) to a file identified by 
        file_name, as string data one cd at a time.
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of cd objects): 2D data structure (lstofCDObjects) that holds the 
            data during runtime

        Returns:
            None.
        """
        try:
            with open(file_name, 'w') as objFile:
                for cd in table:
                    objFile.write(cd.file_export())
                   
        except FileNotFoundError as e:
            print('\n{:*^66}'.format((e.__doc__).upper()),
                  '\n{:^66}'.format(' WARNING: Data not saved').upper())

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('\n\n')
        print('{:-^66}'.format(' Menu '),'\n{:<}'.format('[l] Load Inventory from'),strFileName,
             '\n{:<30}'.format('[a] Add CD'),'\n{:<30}'.format('[i] Display Current Inventory'),
             '\n{:<}'.format('[s] Save Inventory to'),strFileName,
             '\n{:<30}'.format('[x] Exit'),
             '\n{:-^66}'.format('-'))    
 
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s, or x]: ').lower().strip()
        print()  
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('\n\n')
        print('{:=^66}'.format(' The Current Inventory '))
        print('{:<6}{:30}{:30}'.format('ID','Title','Artist'))
        print('{:-^66}'.format('-'))
        for cd in table:
            print(cd)
        print('{:=^66}'.format('='))
        
    @staticmethod
    def add_cd():
        """Ask user for new ID, CD Title and Artist
        
        Args: 
            None.
            
        Returns:
            list of information (ID, Title, and Artist) for a new CD entry"""
        
        cdID = ''
        n=3
        while cdID == '':
            try:
                cdID = int(input('Enter ID: ').strip())
            except ValueError:
                print('\n* Don\'t be a dummy! ID must be a number. Please try again *\n'.upper())
                n-=1
                if n==0:
                    input('You seem to be pretty dense. Let\'s get you back to the main menu.')
                    break
                continue
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
            cdData =[cdID, strTitle, strArtist]
        return cdData
            
# 1. When program starts, read in the currently saved Inventory
FileIO.read_file(strFileName, lstofCDObjects)
IO.show_inventory(lstofCDObjects)
# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    try:
        if strChoice == 'x':# 3.1 process exit first
            break
        # 3.2 process load inventory
        if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('Type \'yes\' to continue and reload from {}. \nPress any key to cancel: '.format(strFileName))
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileIO.read_file(strFileName, lstofCDObjects)
                IO.show_inventory(lstofCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstofCDObjects)
            continue
        # 3.3 process add a CD
        elif strChoice == 'a':
            cdData = IO.add_cd()
            cd=CD(cdData)
            DataProcessor.list_append(cd,lstofCDObjects)
            continue  
        # 3.4 process display current inventory
        elif strChoice == 'i':
            IO.show_inventory(lstofCDObjects)
            continue
        # 3.6 process save inventory to file
        elif strChoice == 's':
            # 3.6.1 Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstofCDObjects)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # 3.6.2 Process choice
            if strYesNo == 'y':
                # 3.6.2.1 save data
                FileIO.write_file(strFileName, lstofCDObjects)
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue
        # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
        else:
            print('General Error')
    except Exception as e: #Exception for exceptions the propogate beyong function level
        print(e.__doc__)



