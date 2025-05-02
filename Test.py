import turtle as t
import math



# main functions:
def main():
    choice = menu()
    while choice!= '0':
        if choice == '1':
            add_shape()
        elif choice == '2':
            modify_shape()
        elif choice == '3':
            delete_shape()
        elif choice == '4':
            display_all()
        elif choice == '5':
            display_specific()
        elif choice == '6':
            draw_shape()
        elif choice == '7':
            generate_statistics()
        else:
            print('\nInvalid choice.\n')
        choice = menu()

def menu():
        option = input("Turtle Shapes Application"
                +"\n\t[1] Add shape"
                +"\n\t[2] Update shape"
                +"\n\t[3] Delete shape"
                +"\n\t[4] List all shapes"
                +"\n\t[5] List by category"
                +"\n\t[6] Draw shape"
                +"\n\t[7] Statistics"
                +"\n"
                +"\n\t[0] Exit"
                +"\nEnter your choice: ")
        return option

def add_shape():
    print()
    invalid = False     # boolean to dermine if correct inputs were entered

    try:                # makes sure that non-integer inputs in integer variables don't crash the program
        invalid_type = True     # boolean to dermine if correct type was entered
        while invalid_type != False:
            type = input("Enter shape type: ").lower()    # converts shape type to lowercase
            if type == "rectangle" or type == "square" or type == "oval" or type == "circle" or type == "triangle":     # shape type should be one of these five only
                invalid_type = False
            else:
                print("Invalid type")
        
        fill_colour = input("Enter fill colour: ").lower()      # converts fill colour to lowercase
        border_colour = input("Enter border colour: ").lower()  # converts border colour to lowercase
        border_thickness = int(input("Enter border thickness: "))
        
        if type == "rectangle" or type == "oval":               # rectangles and ovals have lengths and widths but size is 0
            length = int(input("Enter length: "))
            width = int(input("Enter width: "))
            size = 0
        elif type == "square":                                  # squares have side length as length and width but size is 0
            length = int(input("Enter side length: "))
            width = length
            size = 0
        elif type == "triangle":                                # triangles have side length as size but 0 length and width
            size = int(input("Enter side length: "))
            length = 0
            width = 0
        elif type == "circle":                                  # circles have radius as size but 0 length and width
            size = int(input("Enter radius: "))
            length = 0
            width = 0
    
        x_position = int(input("Enter x position: "))
        y_position = int(input("Enter y position: "))
        description = int(input("Enter rotation: "))

        creation_time = enter_date()                            # stores date and time in format YYYY-MM-DD HH:MM

    except:
        print("Invalid inputs entered. Your shape was not added.")  # if non-integer values were entered in integer variables, handles exception and displays main menu again
        invalid = True

    if invalid != True:     # only adds shape if no exception was thrown
        shape_code = last_shape_id() +1
        
        shape_details = open("shapes.txt","a")
        shape_details.write(f"{type}|{fill_colour}|{border_colour}|{border_thickness}|{length}|{width}|{size}|({x_position},{y_position})|{description}|{shape_code}|{creation_time}\n")
        shape_details.close()           # opens shapes.txt, appends the new line and closes the file 
        print("\nYour shape has been added!")
        print(f"Your new shape's code is {shape_code}")
    
    print()

def modify_shape():
    print()
    changes = 0         # counter to count the number of changes made
    selected_shape_id = input("Enter the shape code you want to edit: ")
    if find_shape(selected_shape_id) == None:       # uses the find_shape function to see if the shape code was found in the file
        print("Shape not found")
        print()
    else:

        all_shapes = shapes_as_2d_list()        # this will be a 2d list of all shapes in the shapes.txt file
            
        for shape in all_shapes:                # iterates over every shape
            if shape[-2] == selected_shape_id:
                option = 10                     # arbitrary value meant simply to initialise
                while option != 0:
                    option = input("\nWhich properties would you like to modify?"
                            +"\n\t[1] Type"
                            +"\n\t[2] Fill colour"
                            +"\n\t[3] Border colour"
                            +"\n\t[4] Border thickness"
                            +"\n\t[5] Length"
                            +"\n\t[6] Width"
                            +"\n\t[7] Size"
                            +"\n\t[8] Position"
                            +"\n\t[9] Description"
                            +"\n"
                            +"\n\t[0] Save and return to main menu"
                            +"\nEnter your choice: ")
                    try:    # makes sure that non-integer inputs in integer variables don't crash the program
                            # each option changes the selected property of the selected shape in the all_shapes list
                        if option == '1':
                            new_type = input("\nEnter new type: ").lower()              # converts shape type to lowercase
                            if new_type == shape[0]:                            # only edits if type is different
                                print("Entered type is already shape type")
                            else:
                                invalid = False
                                if new_type == "rectangle" or new_type == "oval":       # if new type is rectangle or oval it asks for new length and width and size is set to 0
                                    new_length = int(input("Enter new length: "))
                                    new_width = int(input("Enter new width: "))
                                    new_size = 0
                                elif new_type == "square":
                                    new_length = int(input("Enter new side length: "))
                                    new_width = new_length
                                    new_size = 0
                                elif new_type == "triangle":                            # if new type is square or triangle it asks for new size and length and width are set to 0
                                    new_size = int(input("Enter new side length: "))
                                    new_length = 0
                                    new_width = 0
                                elif new_type == "circle":                              # if new type is circle it asks for new size and length and width are set to 0 
                                    new_size = int(input("Enter new radius: "))
                                    new_length = 0
                                    new_width = 0
                                else:
                                    print("Invalid type.")
                                    invalid = True

                                if invalid != True:                 # if input was not invalid, it edits the all_shapes list
                                    shape[0] = new_type
                                    shape[4] = new_length
                                    shape[5] = new_width
                                    shape[6] = new_size
                                    changes+=4

                        elif option == '2':
                            new_colour = input("\nEnter new fill colour: ").lower()     # converts fill colour to lowercase
                            if new_colour == shape[1]:                          # only edits if colour is different
                                print("Entered colour is already shape colour")
                            else:
                                shape[1] = new_colour
                                changes+=1

                        elif option == '3':
                            new_border_colour = input("\nEnter new border colour: ").lower()    # converts border colour to lowercase
                            if new_border_colour == shape[2]:                           # only edits if border colour is different
                                print("Entered colour is already shape border colour")
                            else:
                                shape[2] = new_border_colour
                                changes+=1

                        elif option == '4':
                            new_border_thickness = int(input("\nEnter new border thickness: "))
                            if new_border_thickness == shape[3]:                  # only edits if border thickness is different
                                print("Entered thickness is already shape border thickness")
                            else:
                                shape[3] = new_border_thickness
                                changes+=1

                        elif option == '5':
                            if shape[0] == "rectangle" or shape[0] == "oval":   # only edits if shape is rectangle or oval
                                new_length = int(input("\nEnter new length: "))
                                if new_length == shape[4]:                  # only edits if length is different
                                    print("Entered length is already shape length")
                                else:
                                    shape[4] = new_length
                                    changes+=1
                            elif shape[0] == "square":
                                new_length = int(input("\nEnter new length: "))
                                if new_length == shape[4]:                  # only edits if length is different
                                    print("Entered length is already shape length")
                                else:
                                    shape[4] = new_length
                                    shape[5] = new_length                   # width is also changed with length
                                    changes+=2
                            else:
                                print("\nSelected shape does not have a length")

                        elif option == '6':
                            if shape[0] == "rectangle" or shape[0] == "oval":   # only edits if shape is rectangle or oval
                                new_width = int(input("\nEnter new width: "))
                                if new_width == shape[5]:                  # only edits if width is different
                                    print("Entered width is already shape width")
                                else:
                                    shape[5] = new_width
                                    changes+=1
                            elif shape[0] == "square":
                                new_length = int(input("\nEnter new width: "))
                                if new_length == shape[5]:                  # only edits if width is different
                                    print("Entered width is already shape widh")
                                else:
                                    shape[5] = new_width
                                    shape[4] = new_width                  # length is also changed with width
                                    changes+=2
                            else:
                                print("\nSelected shape does not have a width")

                        elif option == '7':
                            if shape[0] == "triangle":                       # edits side length if shape is triangle
                                new_side_length = int(input("\nEnter new side length: "))
                                if new_side_length == shape[6]:                  # only edits if side length is different
                                    print("Entered side length is already shape side length")
                                else:
                                    shape[6] = new_side_length
                                    changes+=1
                            elif shape[0] == "circle":                      # edits radius if shape is circle
                                new_radius = int(input("\nEnter new radius: "))
                                if new_radius == shape[6]:                  # only edits if radius is different
                                    print("Entered radius is already shape radius")
                                else:
                                    shape[6] = new_radius
                                    changes+=1
                            else:
                                print("\nSelected shape does not have a size")

                        elif option == '8':
                            x_pos = int(input("\nEnter new x position: "))
                            y_pos = int(input("Enter new y position: "))
                            if (f"({x_pos},{y_pos})") == shape[7]:                  # only edits if position is different
                                    print("Entered position is already shape position")
                            else:
                                shape[7] = (f"({x_pos},{y_pos})")
                                changes+=1

                        elif option == '9':
                            new_rotation = int(input("\nEnter new rotation: "))
                            if new_rotation == shape[8]:                  # only edits if rotation is different
                                    print("Entered rotation is already shape rotation")
                            else:
                                shape[8] = new_rotation
                                changes+=1

                        elif option == '0':
                            break
                        else:
                            print('\nInvalid choice.')
                    except:     # if non-integer values were entered in integer variables, handles exception and displays modify menu again
                        print("Invalid inputs entered. Your last change was not made.")
                break
        
        shapes_file = open("shapes.txt","w")    # shapes.txt file is overwritten in the same order with edited the shape
        shapes_file.write("Type|FillColor|BorderColor|BorderThickness|Length|Width|Size|Position|Description|ShapeCode|CreationTime\n")     # writes the header in the file
        for shape in all_shapes:                # iterates over every shape in all_shapes
            type,fill_col,border_col,border_thick,length,width,size,pos,desc,code,datetime = shape      # every item in shape list is stored in its own variable
            shapes_file.write(f"{type}|{fill_col}|{border_col}|{border_thick}|{length}|{width}|{size}|{pos}|{desc}|{code}|{datetime}\n")    # each shape is written in the file line by line
        shapes_file.close()
        
        if changes == 0:
            print("\nYou did not make any changes.")
        elif changes == 1:
            print("\nYour shape has been modified!"
                 +"\nYou made 1 change.")
        else:
            print("\nYour shape has been modified!"
                +f"\nYou made {changes} changes.")

    print()

def delete_shape():
    print()
    invalid = True
    while invalid != False:
        try:                                        # keeps asking for a shape code until a valid code is entered
            selected_shape_id = int(input("Enter the shape code you want to delete: "))
            invalid = False
        except:
            print("Invalid shape code\n")
    
    if find_shape(selected_shape_id) == None:       # uses the find_shape function to see if the shape code was found in the file
        print("Shape not found")
        print()
    else:
        all_shapes = shapes_as_2d_list()            # this will be a 2d list of all shapes in the shapes.txt file
        new_shapes_list = []
        for shape in all_shapes:                    # if the shape isnt the deleted shape, append to the file
            if shape[-2] != str(selected_shape_id):
                new_shapes_list.append(shape)
        
        shapes_file = open("shapes.txt","w")    # shapes.txt file is overwritten in the same order with edited the shape
        shapes_file.write("Type|FillColor|BorderColor|BorderThickness|Length|Width|Size|Position|Description|ShapeCode|CreationTime\n")     # writes the header in the file
        for shape in new_shapes_list:           # iterates over every shape in all_shapes
            type,fill_col,border_col,border_thick,length,width,size,pos,desc,code,datetime = shape      # every item in shape list is stored in its own variable
            shapes_file.write(f"{type}|{fill_col}|{border_col}|{border_thick}|{length}|{width}|{size}|{pos}|{desc}|{code}|{datetime}\n")    # each shape is written in the file line by line
        shapes_file.close()
        print("Your shape has been deleted!")
        print()

def display_all():
    print()
    all_shapes = shapes_as_2d_list()        # this will be a 2d list of all shapes in the shapes.txt file
    
    print("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+")
    print("|    Type    | Fill Color  | Border Color | Border Thickness |   Length   |   Width   |    Size    |  Position  | Description | Shape Code |  Creation Time   |")
    print("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+")
    
    for shape in all_shapes:
        type,fill_col,border_col,border_thick,length,width,size,pos,desc,code,datetime = shape      # every item in shape list is stored in its own variable
        print(f"|{type:^12}|{fill_col:^13}|{border_col:^14}|{border_thick:^18}|{length:^12}|{width:^11}|{size:^12}|{pos:^12}|{desc:^13}|{code:^12}|{datetime:^18}|")    # each shape is printed line by line
        print("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+")
    print()

def display_specific():
    print()
    repeat = True                   # boolean varirable meant to determine if user wants to repeat search
    option = 11                     # arbitrary value meant simply to initialise
    while option != 0 and repeat == True:
        option = input("Which category would you like to filter by?"
                    +"\n\t[1] Type"
                    +"\n\t[2] Fill colour"
                    +"\n\t[3] Border colour"
                    +"\n\t[4] Border thickness"
                    +"\n\t[5] Length"
                    +"\n\t[6] Width"
                    +"\n\t[7] Size"
                    +"\n\t[8] Position"
                    +"\n\t[9] Description"
                    +"\n\t[10] Creation time"

                    +"\n"
                    +"\n\t[0] Return to main menu"
                    +"\nEnter your choice: ")
        print()
        try:    # makes sure that non-integer inputs in integer variables don't crash the program
            if option == '1':
                criteria = input("Enter shape type to filter by: ")
                filtered_shapes = filter_by(criteria.lower(), 0)    # converts category to lowercase before using in the function
            elif option == '2':
                criteria = input("Enter shape fill colour to filter by: ")
                filtered_shapes = filter_by(criteria.lower(), 1)    # converts category to lowercase before using in the function
            elif option == '3':
                criteria = input("Enter shape border colour to filter by: ")
                filtered_shapes = filter_by(criteria.lower(), 2)    # converts category to lowercase before using in the function
            elif option == '4':
                criteria = int(input("Enter shape border thickness to filter by: "))
                filtered_shapes = filter_by(criteria, 3)
            elif option == '5':
                criteria = int(input("Enter shape length to filter by: "))
                filtered_shapes = filter_by(criteria, 4)
            elif option == '6':
                criteria = int(input("Enter shape width to filter by: "))
                filtered_shapes = filter_by(criteria, 5)
            elif option == '7':
                criteria = int(input("Enter shape size to filter by: "))
                filtered_shapes = filter_by(criteria, 6)
            elif option == '8':
                x = int(input("Enter shape x position to filter by: "))
                y = int(input("Enter shape y position to filter by: "))
                criteria = (f"({x},{y})")                           # creates a formatted string of coordinates
                filtered_shapes = filter_by(criteria, 7)
            elif option == '9':
                criteria = int(input("Enter shape rotation to filter by: "))
                filtered_shapes = filter_by(criteria, 8)
            elif option == '10':
                print("Enter shape creation time to filter by: ")
                criteria = enter_date()
                filtered_shapes = filter_by(criteria, 10)
            elif option == '0':
                break
            else:
                print("Invalid choice\n")
            
            if len(filtered_shapes) == 0:
                print("No shape found.")
            else:
                print()
                print("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+")
                print("|    Type    | Fill Color  | Border Color | Border Thickness |   Length   |   Width   |    Size    |  Position  | Description | Shape Code |  Creation Time   |")
                print("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+")
                for shape in filtered_shapes:
                    type,fill_col,border_col,border_thick,length,width,size,pos,desc,code,datetime = shape      # every item in shape list is stored in its own variable
                    print(f"|{type:^12}|{fill_col:^13}|{border_col:^14}|{border_thick:^18}|{length:^12}|{width:^11}|{size:^12}|{pos:^12}|{desc:^13}|{code:^12}|{datetime:^18}|")    # each shape is printed line by line
                    print("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+")
            print()

            repeat_invalid = True               # boolean variable meant to determine if a valid value was entered
            while repeat_invalid != False:      # menu keeps repeating until a valid value is entered
                repeat_opt = input("Would you like to search again?"
                                +"\n\t[1] Yes, search again"
                                +"\n\t[0] No, return to main menu"
                                +"\nEnter your choice: ")
                if repeat_opt == '0':
                    repeat = False              # stops the main while loop from repeating
                    repeat_invalid = False      # stops the repeat menu from repeating
                    print()
                elif repeat_opt == '1':
                    repeat_invalid = False      # stops the repeat menu from repeating
                    print()
                else:
                    print("Invalid input.")     # repeat menu will repeat until valid input is entered
                    print()
        except:
            print("Invalid inputs entered. Returned to filter menu.\n")

def draw_shape():
    print()
    option = 11                     # arbitrary value meant simply to initialise
    while option != 0:
        option = input("Which category would you like to draw?"
                    +"\n\t[1] Type"
                    +"\n\t[2] Fill colour"
                    +"\n\t[3] Border colour"
                    +"\n\t[4] Border thickness"
                    +"\n\t[5] Length"
                    +"\n\t[6] Width"
                    +"\n\t[7] Size"
                    +"\n\t[8] Position"
                    +"\n\t[9] Description"
                    +"\n\t[10] Creation time"

                    +"\n"
                    +"\n\t[0] Return to main menu"
                    +"\nEnter your choice: ")
        print()
        try:    # makes sure that non-integer inputs in integer variables don't crash the program
                # category names are stored to be displayed later
            if option == '1':
                category_name = "Type"                              
                criteria = input("Enter shape type to draw by: ")
                filtered_shapes = filter_by(criteria.lower(), 0)    # converts category to lowercase before using in the function
            elif option == '2':
                category_name = "Fill colour"
                criteria = input("Enter shape fill colour to draw by: ")
                filtered_shapes = filter_by(criteria.lower(), 1)    # converts category to lowercase before using in the function
            elif option == '3':
                category_name = "Border colour"
                criteria = input("Enter shape border colour to draw by: ")
                filtered_shapes = filter_by(criteria.lower(), 2)    # converts category to lowercase before using in the function
            elif option == '4':
                category_name = "Border thickness"
                criteria = int(input("Enter shape border thickness to draw by: "))
                filtered_shapes = filter_by(criteria, 3)
            elif option == '5':
                category_name = "Length"
                criteria = int(input("Enter shape length to draw by: "))
                filtered_shapes = filter_by(criteria, 4)
            elif option == '6':
                category_name = "Width"
                criteria = int(input("Enter shape width to draw by: "))
                filtered_shapes = filter_by(criteria, 5)
            elif option == '7':
                category_name = "Size"
                criteria = int(input("Enter shape size to draw by: "))
                filtered_shapes = filter_by(criteria, 6)
            elif option == '8':
                category_name = "Position"
                x = int(input("Enter shape x position to draw by: "))
                y = int(input("Enter shape y position to draw by: "))
                criteria = (f"({x},{y})")         # creates a formatted string of coordinates
                filtered_shapes = filter_by(criteria, 7)
            elif option == '9':
                category_name = "Rotation"
                criteria = int(input("Enter shape rotation to draw by: "))
                filtered_shapes = filter_by(criteria, 8)
            elif option == '10':
                category_name = "Creation time"
                print("Enter shape creation time to draw by: ")
                criteria = enter_date()
                filtered_shapes = filter_by(criteria, 10)
            elif option == '0':
                break
            else:
                print("Invalid choice\n")
            
            if len(filtered_shapes) == 0:
                print("No shape found.")
            else:
                for shape in filtered_shapes:       # draws each shape in filtered_shapes using draw_single_shape function
                    draw_single_shape(shape[-2])    # shape code is used to draw the shapes
                
                records_file = open("records.txt","a")                  # opens records.txt in append mode
                records_file.write(f"Filter category: {category_name} = {criteria}\n")
                records_file.write("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+\n")
                records_file.write("|    Type    | Fill Color  | Border Color | Border Thickness |   Length   |   Width   |    Size    |  Position  | Description | Shape Code |  Creation Time   |\n")
                records_file.write("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+\n")
                for shape in filtered_shapes:
                    type,fill_col,border_col,border_thick,length,width,size,pos,desc,code,creationtime = shape      # every item in shape list is stored in its own variable
                    records_file.write(f"|{type:^12}|{fill_col:^13}|{border_col:^14}|{border_thick:^18}|{length:^12}|{width:^11}|{size:^12}|{pos:^12}|{desc:^13}|{code:^12}|{creationtime:^18}|\n")    # each shape is written line by line
                    records_file.write("+------------+-------------+--------------+------------------+------------+-----------+------------+------------+-------------+------------+------------------+\n")        
                records_file.write("\n")
                records_file.close()
            print()
        except:
            print("Invalid inputs entered. Returned to draw menu.\n")

def generate_statistics():
    print()
    option = 11                     # arbitrary value meant simply to initialise
    while option != 0 :
        option = input("Which category would you like to filter by?"
                    +"\n\t[1] Type"
                    +"\n\t[2] Fill colour"
                    +"\n\t[3] Border colour"
                    +"\n\t[4] Border thickness"
                    +"\n\t[5] Length"
                    +"\n\t[6] Width"
                    +"\n\t[7] Size"
                    +"\n\t[8] Position"
                    +"\n\t[9] Description"
                    +"\n\t[10] Creation time"

                    +"\n"
                    +"\n\t[0] Return to main menu"
                    +"\nEnter your choice: ")
        print()
        try:    # makes sure that non-integer inputs in integer variables don't crash the program
                # each option changes the selected property of the selected shape in the all_shapes list
            filter_range = ""      # empty string that will be overwritten if option 4-10 are chosen
            if option == '1':
                category_name = "Type"
                criteria = input("Enter shape type to filter by: ")
                filtered_shapes = filter_by(criteria.lower(), 0)    # converts critera to lowercase before using in the function
            elif option == '2':
                category_name = "Fill Colour"
                criteria = input("Enter shape fill colour to filter by: ")
                filtered_shapes = filter_by(criteria.lower(), 1)    # converts critera to lowercase before using in the function
            elif option == '3':
                category_name = "Border Colour"
                criteria = input("Enter shape border colour to filter by: ")
                filtered_shapes = filter_by(criteria.lower(), 2)    # converts critera to lowercase before using in the function
            elif option == '4':
                category_name = "Border Thickness"
                filter = filter_by_range(3)
                filtered_shapes = filter[0]                         # this is the filtered shapes returned from filter_by_range
                filter_range = filter[1]                            # this is the filter range returned from filter_by_range
                criteria = filter[2]                                # this is the critera name returned from filter_by_range
            elif option == '5':
                category_name = "Length"
                filter = filter_by_range(4)
                filtered_shapes = filter[0]                         # this is the filtered shapes returned from filter_by_range
                filter_range = filter[1]                            # this is the filter range returned from filter_by_range
                criteria = filter[2]                                # this is the critera name returned from filter_by_range
            elif option == '6':
                category_name = "Width"
                filter = filter_by_range(5)
                filtered_shapes = filter[0]                         # this is the filtered shapes returned from filter_by_range
                filter_range = filter[1]                            # this is the filter range returned from filter_by_range
                criteria = filter[2]                                # this is the critera name returned from filter_by_range
            elif option == '7':
                category_name = "Size"
                filter = filter_by_range(6)
                filtered_shapes = filter[0]                         # this is the filtered shapes returned from filter_by_range
                filter_range = filter[1]                            # this is the filter range returned from filter_by_range
                criteria = filter[2]                                # this is the critera name returned from filter_by_range
            elif option == '8':
                category_name = "Position"
                filter = filter_by_position(7)
                filtered_shapes = filter[0]                         # this is the filtered shapes returned from filter_by_range
                filter_range = filter[1]                            # this is the filter range returned from filter_by_range
                criteria = filter[2]                                # this is the critera name returned from filter_by_range
            elif option == '9':
                category_name = "Description"
                filter = filter_by_range(8)
                filtered_shapes = filter[0]                         # this is the filtered shapes returned from filter_by_range
                filter_range = filter[1]                            # this is the filter range returned from filter_by_range
                criteria = filter[2]                                # this is the critera name returned from filter_by_range
            elif option == '10':
                category_name = "Creation Time"
                filter = filter_by_date(10)
                filtered_shapes = filter[0]                         # this is the filtered shapes returned from filter_by_range
                filter_range = filter[1]                            # this is the filter range returned from filter_by_range
                criteria = filter[2]                                # this is the critera name returned from filter_by_range
            elif option == '0':
                break
            else:
                print("Invalid choice\n")
            

            if len(filtered_shapes) == 0:
                print("No shapes found\n")
            else:
                no_of_shapes = len(filtered_shapes)
                max_size = 0
                min_size = 99999999999999999
                sum_of_areas = 0

                for shape in filtered_shapes:                   # iterates over every shape, calculates area, updates sum, min and max
                    area = calculate_area(shape)
                    sum_of_areas += area
                    if area > max_size:
                        max_size = area
                    if area < min_size:
                        min_size = area

                average_area = sum_of_areas/no_of_shapes

                colours_found = []
                for shape in filtered_shapes:
                    found = False                               # boolean to determine if colour is in colours_found or not
                    for i in range(len(colours_found)):
                        if colours_found[i][0] == shape[1]:     # if the color already exists, increment the count and set found as True
                            colours_found[i][1] += 1
                            found = True
                            break
                    if found != True:                           # if not found, add the new color with a count of 1
                        colours_found.append([shape[1], 1])

                colour_output = ("Distribution of Colours:\n")
                for colour in colours_found:                    # displays every colour and count one by one
                    colour_output += f"- {colour[0]}: {colour[1]}\n"

                if option == "2":                               # if user filtered by colour, it doesn't show colour distribution in output
                    output=(f"\nTotal number of shapes: {no_of_shapes}"
                        +f"\nAverage size: {average_area:.2f}"
                        +f"\nMinimum size: {min_size:.2f}"
                        +f"\nMaximum size: {max_size:.2f}\n")
                else:
                    output=(f"\nTotal number of shapes: {no_of_shapes}"
                        +f"\nAverage size: {average_area:.2f}"
                        +f"\nMinimum size: {min_size:.2f}"
                        +f"\nMaximum size: {max_size:.2f}\n"
                        +colour_output)
                    
                print(f"Statistics for Shapes of {category_name}{filter_range}: {criteria}")
                print(output)                
                
                repeat_invalid = True               # boolean variable meant to determine if a valid value was entered
                while repeat_invalid != False:      # menu keeps repeating until a valid value is entered
                    repeat_opt = input("Would you like to save these statistics?"
                                    +"\n\t[1] Yes, save to analysis.txt"
                                    +"\n\t[0] No, return to filter menu"
                                    +"\nEnter your choice: ")
                    if repeat_opt == '0':
                        repeat_invalid = False      # stops the repeat menu from repeating
                        print()
                    elif repeat_opt == '1':
                        repeat_invalid = False      # stops the repeat menu from repeating
                        if option == "2":           # if user filtered by colour, it doesn't write colour distribution in the analysis.txt file
                            analysis_file = open("analysis.txt","a")
                            analysis_file.write(f"Statistics for Shapes of {category_name}{filter_range}: {criteria}\n"
                                            +f"\nTotal Count: {no_of_shapes}\n"
                                            +f"\nAverage Size: {average_area:.2f}"
                                            +f"\nSmallest Size: {min_size:.2f}"
                                            +f"\nLargest Size: {max_size:.2f}\n\n"
                                            +"--------------------------------------------------------------------------------------------------------\n\n")
                            analysis_file.close()
                        else:
                            analysis_file = open("analysis.txt","a")
                            analysis_file.write(f"Statistics for Shapes of {category_name}{filter_range}: {criteria}\n"
                                            +f"\nTotal Count: {no_of_shapes}\n"
                                            +f"\n{colour_output}"
                                            +f"\nAverage Size: {average_area:.2f}"
                                            +f"\nSmallest Size: {min_size:.2f}"
                                            +f"\nLargest Size: {max_size:.2f}\n\n"
                                            +"--------------------------------------------------------------------------------------------------------\n\n")
                            analysis_file.close()

                        print()
                    else:
                        print("Invalid input.\n")   # repeat menu will repeat until valid input is entered

        except:
            print("Invalid inputs entered. Returned to filter menu.\n")



# helper functions:
def open_file(filename):
    file = open(filename)
    lines = file.readlines()    # "lines" is now a list of all lines
    file.close()
    return lines

def enter_date():
    invalid = True                      # boolean to dermine if correct inputs were entered
    while invalid != False:
        try:
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (MM): "))
            date = int(input("Enter date (DD): "))
            hour = int(input("Enter hour (HH): "))
            minute = int(input("Enter minute (MM): "))

            date = (f"{year:04d}-{month:02d}-{date:02d} {hour:02d}:{minute:02d}")   # formatted string of proper date
            invalid = False
            return date
        except:
            print("Invalid inputs, enter date again")

def shapes_as_2d_list():
    shapes = open_file("shapes.txt")
    all_shapes = []         # this will be a 2d list of all lines in the shapes.txt file
    for shape in shapes:
        shape_list = []     # temporary list containing all data of each shape
        type,fill_col,border_col,border_thick,length,width,size,pos,desc,code,datetime = shape.strip().split("|")
        shape_list.append(type)
        shape_list.append(fill_col)
        shape_list.append(border_col)
        shape_list.append(border_thick)
        shape_list.append(length)
        shape_list.append(width)
        shape_list.append(size)
        shape_list.append(pos)
        shape_list.append(desc)
        shape_list.append(code)
        shape_list.append(datetime)
        all_shapes.append(shape_list)       # add the list of each shape's data to the main list    
    
    shapes_list_without_header = []
    for shape in all_shapes:
        if shape[0] != "Type":              # removes only the header from the data, keeps every shape the same
                shapes_list_without_header.append(shape)

    return shapes_list_without_header

def last_shape_id():
    shapes = open_file("shapes.txt")                # "shapes" is now a list of all shapes

    max_shape_id = 0

    for shape in shapes:                            # iterates over each item (line) in list shapes
        shape_id = shape.strip().split("|")[-2]     # removes extra whitespace, splits using the delimiter | and stores second last value in shape_id
        if shape_id == "ShapeCode":                 # the first line is the header so it doesn't count as a shape
            max_shape_id = 0
        elif shape_id == None:                      # when the end of the file is reached, it returns max_shape_id
            return int(max_shape_id)
        elif int(shape_id) > int(max_shape_id):     # if the shape's id is larger than the current largest id, it is replaced with the new one
            max_shape_id = shape_id
    
    return int(max_shape_id)

def find_shape(wanted_id):
    shapes = shapes_as_2d_list()            # "shapes" is now a 2d list of all shapes
    for shape in shapes:                    # iterates over each shapes in list shapes
        if shape[-2] == str(wanted_id):     # if it finds the wanted id in the shapes list, it returns that shape
            return shape
    return None                             # if shape is not found, returns None                      

def filter_by(criteria, category_index):
    all_shapes = shapes_as_2d_list()
    filtered_shapes = []
    for shape in all_shapes:
        if shape[category_index] == str(criteria):              # only adds shapes of specified category
                filtered_shapes.append(shape)

    return filtered_shapes

def draw_single_shape(id):
    shape = find_shape(id)                              # gets the desired shape in a list
    coordinates = shape[7].split(",")                   # splits the coordinates in the middle at the comma
    x_coordinates = int(coordinates[0].strip("("))      # strips out the "(" leaving the integer value of x axis
    y_coordinates = int(coordinates[1].strip(")"))      # strips out the ")" leaving the integer value of y axis
    
    t.speed(0)
    t.penup()
    t.goto(x_coordinates,y_coordinates)                 # takes the turtle to the desired position
    t.pensize(int(shape[3]))                            # sets the desired border size
    t.pencolor(shape[2])                                # sets the desired border colour
    t.fillcolor(shape[1])                               # sets the desired fill colour
    t.left(int(shape[8]))                               # sets the desired rotation

    if shape[0] == "rectangle":                         # draws a rectangle
        t.begin_fill()
        t.pendown()
        for i in range(2):                              # draws the length, rotates 90 degrees, draws width, rotates and repeats 2 times total
            t.forward(int(shape[4]))
            t.left(90)
            t.forward(int(shape[5]))
            t.left(90)
        
    elif shape[0] == "square":                          # draws a square
        t.begin_fill()
        t.pendown()
        for i in range(4):                              # draws the length, rotates 90 degrees and repeats 4 times total
            t.forward(int(shape[4]))
            t.left(90)

    elif shape[0] == "circle":                          # draws a circle
        t.begin_fill()
        t.pendown()
        t.circle(int(shape[6]))                         # uses the inbuilt circle function to draw circle of desired radius
        
    elif shape[0] == "triangle":                        # draws a triangle
        t.begin_fill()
        t.pendown()
        for i in range(3):                              # draws side length, rotates 120 degrees and repeats 3 times total
            t.forward(int(shape[6]))
            t.left(120)

    elif shape[0] == "oval":                            # draws an oval
        t.begin_fill()
        t.pendown()
        t.right(45)                                     # rotates 45 degrees otherwise oval will be drawn diagonally
        for i in range(2):                              # repeats 2 times total
            t.circle(int(shape[4]),90)                  # draws a circle using the length as radius but stops after 90 degrees
            t.circle(int(shape[5]),90)                  # continues the circle using width as radius but stops after 90 degrees
        t.left(45)                                      # rotates 45 degrees in the opposite direction to undo the temporary rotation
    
    t.right(int(shape[8]))                              # rotates turtle opposite to desired rotation so that next shapes aren't rotated unnecessarily
    t.end_fill()

def filter_by_range(category_index):
    try:
        choice = 8
        choice = input("What range would you like to filter by?"
                    +"\n\t[1] Less than"
                    +"\n\t[2] Less than or equal to"
                    +"\n\t[3] Greater than"
                    +"\n\t[4] Greater than or equal to"
                    +"\n\t[5] Equal to"
                    +"\n\t[6] Between"
                    +"\n\t[7] Between and including"
                    +"\nEnter your choice: ")
        if choice == '1':
            less_than = int(input("Less than: "))
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if int(shape[category_index]) < less_than:
                    filtered_shapes.append(shape)
            filter_range = " Less Than"                         # stores filter range to return at the end
            criteria = less_than                                # stores filter critera to return at the end
        elif choice == '2':
            less_than_equal_to = int(input("Less than or equal to: "))
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if int(shape[category_index]) <= less_than_equal_to:
                    filtered_shapes.append(shape)
            filter_range = " Less Than or Equal To"             # stores filter range to return at the end
            criteria = less_than_equal_to                       # stores filter critera to return at the end
        elif choice == '3':
            greater_than = int(input("Greater than: "))
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if int(shape[category_index]) > greater_than:
                    filtered_shapes.append(shape)
            filter_range = " Greater Than"                      # stores filter range to return at the end
            criteria = greater_than                             # stores filter critera to return at the end
        elif choice == '4':
            greater_than_equal_to = int(input("Greater than or equal to: "))
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if int(shape[category_index]) >= greater_than_equal_to:
                    filtered_shapes.append(shape)
            filter_range = " Greater Than or Equal To"          # stores filter range to return at the end
            criteria = greater_than_equal_to                    # stores filter critera to return at the end
        elif choice == '5':
            equal_to = int(input("Equal to: "))
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if int(shape[category_index]) == equal_to:
                    filtered_shapes.append(shape)
            filter_range = " Equal To"                          # stores filter range to return at the end
            criteria = equal_to                                 # stores filter critera to return at the end
        elif choice == '6':
            lower_bound = int(input("Lower bound: "))
            upper_bound = int(input("Upper bound: "))
            if lower_bound >= upper_bound:                      # checks if the selected range is valid
                print("Upper bound must be greater than lower bound")
            else:
                shapes = shapes_as_2d_list()
                filtered_shapes = []
                for shape in shapes:                            # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                    if int(shape[category_index]) > lower_bound and int(shape[category_index]) < upper_bound:
                        filtered_shapes.append(shape)
                filter_range = " Between"                           # stores filter range to return at the end
                criteria = f"{lower_bound} and {upper_bound}"       # stores filter critera to return at the end
        elif choice == '7':
            lower_bound = int(input("Lower bound (including): "))
            upper_bound = int(input("Upper bound (including): "))
            if lower_bound >= upper_bound:                          # checks if the selected range is valid
                print("Upper bound must be greater than lower bound")
            else:
                shapes = shapes_as_2d_list()
                filtered_shapes = []
                for shape in shapes:                            # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                    if int(shape[category_index]) >= lower_bound and int(shape[category_index]) <= upper_bound:
                        filtered_shapes.append(shape)
                filter_range = " Between and Including"             # stores filter range to return at the end
                criteria = f"{lower_bound} and {upper_bound}"       # stores filter critera to return at the end
        else:
            print("Invalid input")
        
        return [filtered_shapes,filter_range,criteria]
    except:
        print("Invalid inputs entered.")

def filter_by_date(category_index):
    try:
        choice = 8
        choice = input("What range would you like to filter by?"
                    +"\n\t[1] Older than"
                    +"\n\t[2] Older than or equal to"
                    +"\n\t[3] Newer than"
                    +"\n\t[4] Newer than or equal to"
                    +"\n\t[5] Equal to"
                    +"\n\t[6] Between"
                    +"\n\t[7] Between and including"
                    +"\nEnter your choice: ")
        if choice == '1':
            print("Older than: ")
            older_than = enter_date()
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] < older_than:
                    filtered_shapes.append(shape)
            filter_range = " Older Than"                        # stores filter range to return at the end
            criteria = older_than                               # stores filter critera to return at the end
        elif choice == '2':
            print("Older than or equal to: ")
            older_than_equal_to = enter_date()
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] <= older_than_equal_to:
                    filtered_shapes.append(shape)
            filter_range = " Older Than or Equal To"            # stores filter range to return at the end
            criteria = older_than_equal_to                      # stores filter critera to return at the end
        elif choice == '3':
            print("Newer than: ")
            newer_than = enter_date()
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] > newer_than:
                    filtered_shapes.append(shape)
            filter_range = " Newer Than"                        # stores filter range to return at the end
            criteria = newer_than                               # stores filter critera to return at the end
        elif choice == '4':
            print("Newer than or equal to: ")
            newer_than_equal_to = enter_date()
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] >= newer_than_equal_to:
                    filtered_shapes.append(shape)
            filter_range = " Newer Than or Equal To"            # stores filter range to return at the end
            criteria = newer_than_equal_to                      # stores filter critera to return at the end
        elif choice == '5':
            print("Equal to: ")
            equal_to = enter_date()
            shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in shapes:                                # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] == equal_to:
                    filtered_shapes.append(shape)
            filter_range = " Equal To"                          # stores filter range to return at the end
            criteria = equal_to                                 # stores filter critera to return at the end
        elif choice == '6':
            print("Lower bound: ")
            lower_bound = enter_date()
            print("\nUpper bound: ")
            upper_bound = enter_date()
            if lower_bound >= upper_bound:                      # checks if the selected range is valid
                print("Upper bound must be greater than lower bound")   
            else:
                shapes = shapes_as_2d_list()
                filtered_shapes = []
                for shape in shapes:                            # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                    if shape[category_index] > lower_bound and shape[category_index] < upper_bound:
                        filtered_shapes.append(shape)
                filter_range = " Between"                       # stores filter range to return at the end
                criteria = f"{lower_bound} and {upper_bound}"   # stores filter critera to return at the end
        elif choice == '7':
            print("Lower bound (including): ")
            lower_bound = enter_date()
            print("\nUpper bound (including): ")
            upper_bound = enter_date()
            if lower_bound >= upper_bound:                      # checks if the selected range is valid
                print("Upper bound must be greater than lower bound")
            else:
                shapes = shapes_as_2d_list()
                filtered_shapes = []
                for shape in shapes:                            # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                    if shape[category_index] >= lower_bound and shape[category_index] <= upper_bound:
                        filtered_shapes.append(shape)
                filter_range = " Between and Including"         # stores filter range to return at the end
                criteria = f"{lower_bound} and {upper_bound}"   # stores filter critera to return at the end
        else:
            print("Invalid input")
        
        return [filtered_shapes,filter_range,criteria]          # returns filtered shapes and the selected range and critera
    except:
        print("Invalid inputs entered.")

def filter_by_position(category_index):
    try:
        choice = 8
        choice = input("What range would you like to filter by?"
                    +"\n\t[1] Less than"
                    +"\n\t[2] Less than or equal to"
                    +"\n\t[3] Greater than"
                    +"\n\t[4] Greater than or equal to"
                    +"\n\t[5] Equal to"
                    +"\n\t[6] Between"
                    +"\n\t[7] Between and including"
                    +"\nEnter your choice: ")
        if choice == '1':
            x_less_than = int(input("x Less than: "))
            y_less_than = int(input("y Less than: "))
            all_shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in all_shapes:                                        # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] == "Position":
                    pass
                else:
                    position = shape[category_index]
                    coordinates = position.split(",")
                    x_coords = int(coordinates[0].strip("("))
                    y_coords = int(coordinates[1].strip(")"))
                    if x_coords < x_less_than and y_coords < y_less_than:
                        filtered_shapes.append(shape)
            filter_range = " Less Than"                                     # stores filter range to return at the end
            criteria = f"({x_less_than},{y_less_than})"                     # stores filter critera to return at the end
        elif choice == '2':
            x_less_than_equal_to = int(input("x Less than or equal to: "))
            y_less_than_equal_to = int(input("y Less than or equal to: "))
            all_shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in all_shapes:                                        # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] == "Position":
                    pass
                else:
                    position = shape[category_index]
                    coordinates = position.split(",")
                    x_coords = int(coordinates[0].strip("("))
                    y_coords = int(coordinates[1].strip(")"))
                    if x_coords <= x_less_than_equal_to and y_coords <= y_less_than_equal_to:
                        filtered_shapes.append(shape)
            filter_range = " Less Than or Equal To"                         # stores filter range to return at the end
            criteria = f"({x_less_than_equal_to},{y_less_than_equal_to})"   # stores filter critera to return at the end
        elif choice == '3':
            x_greater_than = int(input("x Greater than: "))
            y_greater_than = int(input("y Greater than: "))
            all_shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in all_shapes:                                        # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] == "Position":
                    pass
                else:
                    position = shape[category_index]
                    coordinates = position.split(",")
                    x_coords = int(coordinates[0].strip("("))
                    y_coords = int(coordinates[1].strip(")"))
                    if x_coords > x_greater_than and y_coords > y_greater_than:
                        filtered_shapes.append(shape)
            filter_range = " Greater Than"                                  # stores filter range to return at the end
            criteria = f"({x_greater_than},{y_greater_than})"               # stores filter critera to return at the end
        elif choice == '4':
            x_greater_than_equal_to = int(input("x Greater than or equal to: "))
            y_greater_than_equal_to = int(input("y Greater than or equal to: "))
            all_shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in all_shapes:                                        # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] == "Position":
                    pass
                else:
                    position = shape[category_index]
                    coordinates = position.split(",")
                    x_coords = int(coordinates[0].strip("("))
                    y_coords = int(coordinates[1].strip(")"))
                    if x_coords >= x_greater_than_equal_to and y_coords >= y_greater_than_equal_to:
                        filtered_shapes.append(shape)
            filter_range = " Greater Than or Equal To"                      # stores filter range to return at the end
            criteria = f"({x_greater_than_equal_to},{y_greater_than_equal_to})" # stores filter critera to return at the end
        elif choice == '5':
            x_equal_to = int(input("x Equal to: "))
            y_equal_to = int(input("y Equal to: "))
            all_shapes = shapes_as_2d_list()
            filtered_shapes = []
            for shape in all_shapes:                                        # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                if shape[category_index] == "Position":
                    pass
                else:
                    position = shape[category_index]
                    coordinates = position.split(",")
                    x_coords = int(coordinates[0].strip("("))
                    y_coords = int(coordinates[1].strip(")"))
                    if x_coords == x_equal_to and y_coords == y_equal_to:
                        filtered_shapes.append(shape)
            filter_range = " Equal To"                                      # stores filter range to return at the end
            criteria = f"({x_equal_to},{y_equal_to})"                       # stores filter critera to return at the end
        elif choice == '6':
            x_lower = int(input("x Lower bound: "))
            y_lower = int(input("y Lower bound: "))
            x_upper = int(input("\nx Upper bound: "))
            y_upper = int(input("y Upper bound: "))
            all_shapes = shapes_as_2d_list()
            if x_lower >= x_upper or y_lower >= y_upper:                    # checks if the selected range is valid
                print("Upper bound must be greater than lower bound")
            else:
                filtered_shapes = []
                for shape in all_shapes:                                    # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                    if shape[category_index] == "Position":
                        pass
                    else:
                        position = shape[category_index]
                        coordinates = position.split(",")
                        x_coords = int(coordinates[0].strip("("))
                        y_coords = int(coordinates[1].strip(")"))
                        if x_coords > x_lower and x_coords < x_upper and y_coords > y_lower and y_coords < y_upper:
                            filtered_shapes.append(shape)
            filter_range = " Between"                                       # stores filter range to return at the end
            criteria = f"({x_lower},{y_lower}) and ({x_upper},{y_upper})"   # stores filter critera to return at the end
        elif choice == '7':
            x_lower = int(input("x Lower bound (including): "))
            y_lower = int(input("y Lower bound (including): "))
            x_upper = int(input("\nx Upper bound (including): "))
            y_upper = int(input("y Upper bound (including): "))
            all_shapes = shapes_as_2d_list()
            if x_lower >= x_upper or y_lower >= y_upper:                    # checks if the selected range is valid
                print("Upper bound must be greater than lower bound")
            else:
                filtered_shapes = []
                for shape in all_shapes:                                    # iterates over every shape, and if it fulfils the criteria it adds it to filtered_shapes
                    if shape[category_index] == "Position":
                        pass
                    else:
                        position = shape[category_index]
                        coordinates = position.split(",")
                        x_coords = int(coordinates[0].strip("("))
                        y_coords = int(coordinates[1].strip(")"))
                        if x_coords >= x_lower and x_coords <= x_upper and y_coords >= y_lower and y_coords <= y_upper:
                            filtered_shapes.append(shape)
            filter_range = " Between and Including"                         # stores filter range to return at the end
            criteria = f"({x_lower},{y_lower}) and ({x_upper},{y_upper})"   # stores filter critera to return at the end
        else:
            print("Invalid input")
        
        return [filtered_shapes,filter_range,criteria]                      # returns filtered shapes and the selected range and critera
    except:
        print("Invalid inputs entered.")

def calculate_area(shape):
    if shape[0] == "rectangle" or shape[0] == "square":                 # if shape is square or rectangle, multiply the height and width
        area = int(shape[4]) * int(shape[5])
    elif shape[0] == "triangle":                                        # if shape is triangle, use (sqrt3)/4*a^2
        area = ((math.sqrt(3)) / 4) * int(shape[6])*int(shape[6])
    elif shape[0] == "circle":                                          # if shape is circle, use pi*r^2
        area = math.pi*int(shape[6])*int(shape[6])
    elif shape[0] == "oval":                                            # if shape is oval, use pi*a*b
        area = math.pi*int(shape[4])*int(shape[5])
    return area



main()