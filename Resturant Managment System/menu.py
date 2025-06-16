
class Menu:
    def __init__(self):
        self.menu_list=[]

    def add_menu(self,itm):
        self.menu_list.append(itm)
    
    def find_menu(self,name):
        for itm in self.menu_list:
            if itm.name.lower() == name.lower():
                return itm
        return None 
    
    def remove_menu(self,name):
        get_itm=self.find_menu(name)
        if get_itm:
            self.menu_list.remove(get_itm)
            print(f"{name} removed Successfully")
        else:
            print(f"{name} Not in The list")
    
    def show_menu(self):
        if not self.menu_list:
            print("There is no itms on the Menu")
        else:
            print("\n \t --------Menus-------")
            print("\tName \tPrice \tQuantity")
            for itms in self.menu_list:
                print(f"\t{itms.name}\t{itms.price}\t{itms.quantity}")

