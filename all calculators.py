print("choose from calculator")
print("========================================")
print("---------------claculator---------------")
print("========================================")
print("1-standard\n2-area\n3-premiter\n4-volume\n5-age\n6-data\n7-speed")

calc_choosen=int(input("please choose number of calculator: "))

# standard calculator
if   calc_choosen ==1:
    a = int(input("please enter 1st number: "))
    operation = input("please enter operation: ")
    b = int(input("please enter 2nd number: "))
    def sum(a,b,c):

        if operation=="+":
            f=a+b
            print(f)
        elif operation=="-":
            f=a-b
            print(f)
        elif operation=="*":
            f=a*b
            print(f)
        elif operation=="//":
            f=a//b
            print(f)
        elif operation=="**":
            f=a**b
            print(f)
        elif operation=="%":
            f=a%b
            print(f)    
        elif operation=="/":
            f=a/b
            print(f)
        else:
            print("please choose number from above")    
    sum(a,b,operation)
# area calculator
elif calc_choosen ==2:
    print("choose from menu")
    print("|==================|")
    print("|-------Menu-------|")
    print("|==================|")
    print("1-rectangle \n2-square\n3-circle\n4-triangle")

    area_choosen=input("please choose from menu: ")
    
    if area_choosen==1:
        rec_lenth=int(input("please enter lenth: "))
        rec_width=int(input("please enter width: "))
        a=rec_lenth*rec_width
        print(a)
    
    elif area_choosen==2:
        squ_side=int(input("please enter side lenth: "))
        a=squ_side*squ_side
        print(a)

    elif area_choosen==3:
        circle_radius=int(input("please enter radius: "))
        a=3.14*circle_radius*circle_radius
        print(a) 
    
    elif area_choosen==4:
        triangle_base=int(input("please enter triangle base: "))        
        triangle_height=int(input("please enter triangle height: "))
        a=0.5*triangle_base*triangle_height
        print(a)
    
    else:
        print("please choose number from above")
# premiter calculator
elif calc_choosen ==3:
    print("please choose from menu")
    print("|==================|")
    print("|-------Menu-------|")
    print("|==================|")
    print("1-rectangle \n2-square\n3-circle\n4-equilateral_triangle")

    choosen=input("please choose from menu: ")
    
    if choosen==1:
        rec_lenth=int(input("please enter lenth: "))
        rec_width=int(input("please enter width: "))
        d=2*(rec_lenth+rec_width)
        print("prmeiter =",d)
    
    elif choosen==2:
        squ_side=int(input("please enter side lenth: "))
        d=squ_side*4
        print("prmeiter =",d)

    elif choosen==3:
        circle_radius=int(input("please enter radius: "))
        d=3.14*circle_radius*circle_radius
        print("prmeiter =",d) 
    
    elif choosen==4:
        triangle_side=int(input("please enter triangle side: "))        
        d=triangle_side*3
        print("prmeiter =",d)
# volume calculator
elif calc_choosen ==4:
    print("please choose from menu")
    print("|==================|")
    print("|-------Menu-------|")
    print("|==================|")
    print("1-cube\n2-cuboid\n3-cylinder\n4-cone\n5-square pyramid")
    volume_choosen = int(input("please choose shape: "))

    if volume_choosen == 1:
        cube_side = int(input("please enter side: "))
        v = cube_side**3
        print(v)
    elif volume_choosen ==2:
        lenth_cuboid = int(input("please enter lenth: "))
        width_cuboid = int(input("please enter width: "))
        height_cuboid = int(input("please enter height: "))
        v = lenth_cuboid*width_cuboid*height_cuboid
        print(v)
    elif volume_choosen == 3:
        height_cylinder = int(input("please enter height: "))
        radius_cylinder = int(input("please enter radius: "))
        v = radius_cylinder**2 * height_cylinder * 3.14
        print(v)
    elif volume_choosen == 4:
        cone_radius = int(input("please enter radius: "))
        cone_height = int(input("please enter height: "))
        V = 3.14*(cone_radius**2)*(cone_height/3)
        print(V)
    elif volume_choosen == 5:
        base_edge = int(input("please enter base edge"))
        pyramid_height = int(input("please enter height"))
        v = base_edge**2*(pyramid_height/3)
        print(v)
# age calculator
elif calc_choosen ==5:
    print("choose from menu")
    print("|==================|")
    print("|-------Menu-------|")
    print("|==================|")
    print("1-months\n2-days\n3-hours\n4-all")
    choosen_from_menu = int(input("please choose from menu: "))

    if choosen_from_menu==1:
        age = float(input("please enter your age: "))
        a = age*12
        print(" ")
        print("you lived "+ str(a) + " months")
    elif choosen_from_menu==2:
        age = float(input("please enter your age: "))
        a = age*12*30
        print(" ")
        print("you lived "+ str(a) + " days")
    elif choosen_from_menu==3:
        age = float(input("please enter your age: "))
        a = age*12*30*24
        print(" ")
        print("you lived "+ str(a) + " hours")

    elif choosen_from_menu==4:
        age = float(input("please enter your age: "))
        a = age*12
        print(" ")
        print("you lived "+ str(a) + " months")
        a = age*12*30
        print(" ")
        print("you lived "+ str(a) + " days")
        a = age*12*30*24
        print(" ")
        print("you lived "+ str(a) + " hours")  
# data calculator
elif calc_choosen ==6:
    print("Please Choose What You Want To Convert From")
    print("============================================================")
    print("------------------------convert from------------------------")
    print("============================================================")
    print("1-byte\n2-kilobyte\n3-megabyte\n4-gigabyte\n5-terabyte\n6-petabyte")

    convert_from = int(input("Please Choose What You Want To Convert From: "))

    if convert_from ==1:
        print("Please Choose What You Want To Convert To")
        print("============================================================")
        print("-------------------------convert to-------------------------")
        print("============================================================")
        print("1-kilobyte\n2-megabyte\n3-gigabyte\n4-terabyte\n5-petabyte")

        convert_to = int(input("Please Choose What You Want To Convert To: "))
        if convert_to == 1:
            to = int(input("Please Enter How Many Bytes: "))
            a = to/1024
            print(str(a)+"  Kilobytes")

        elif convert_to == 2:
            to = int(input("please enter how many bytes: "))
            a = to/1024/1024
            print(str(a)+"  megabytes")  

        elif convert_to == 3:
            to = int(input("please enter how many bytes: "))
            a = to/1024/1024/1024
            print(str(a)+"  gigabytes")

        elif convert_to == 4:
            to = int(input("please enter how many bytes: "))
            a = to/1024/1024/1024/1024
            print(str(a)+" terabytes")

        elif convert_to == 5:
            to = int(input("please enter how many bytes: "))
            a = to/1024/1024/1024/1024/1024
            print(str(a)+"  petabytes")

    elif convert_from ==2:
        print("please choose what you want to convert to")
        print("============================================================")
        print("-------------------------convert to-------------------------")
        print("============================================================")
        print("1-byte\n2-megabyte\n3-gigabyte\n4-terabyte\n5-petabyte")

        convert_to = int(input("please choose what you want to convert to: "))

        if convert_to == 1:
            to = int(input("please enter how many kilobytes: "))
            a = to*1024
            print(str(a)+" bytes")

        elif convert_to == 2:
            to = int(input("please enter how many kilobytes: "))
            a = to/1024
            print(str(a)+" megabytes")  

        elif convert_to == 3:
            to = int(input("please enter how many kilobytes: "))
            a = to/1024/1024
            print(str(a)+"  gigabytes")

        elif convert_to == 4:
            to = int(input("please enter how many kilobytes: "))
            a = to/1024/1024/1024
            print(str(a)+" terabytes")

        elif convert_to == 5:
            to = int(input("please enter how many kilobytes: "))
            a = to/1024/1024/1024/1024
            print(str(a)+"  petabytes")

    elif convert_from ==3:
        print("please choose what you want to convert to")
        print("============================================================")
        print("-------------------------convert to-------------------------")
        print("============================================================")
        print("1-byte\n2-kilobyte\n3-gigabyte\n4-terabyte\n5-petabyte")

        convert_to = int(input("please choose what you want to convert to: "))

        if convert_to == 1:
            to = int(input("please enter how many megabytes: "))
            a = to*1024*1024
            print(str(a)+" bytes")
            
        elif convert_to == 2:
            to = int(input("please enter how many megabytes: "))
            a = to*1024
            print(str(a)+" kilobytes")            

        elif convert_to == 3:
            to = int(input("please enter how many megabytes: "))
            a = to/1024
            print(str(a)+"  gigabytes")

        elif convert_to == 4:
            to = int(input("please enter how many megabytes: "))
            a = to/1024/1024
            print(str(a)+" terabytes")

        elif convert_to == 5:
            to = int(input("please enter how many megabytes: "))
            a = to/1024/1024/1024
            print(str(a)+"  petabytes")

    elif convert_from ==4:
        print("please choose what you want to convert to")
        print("============================================================")
        print("-------------------------convert to-------------------------")
        print("============================================================")
        print("1-byte\n2-kilobyte\n3-megabyte\n4-terabyte\n5-petabyte")

        convert_to = int(input("please choose what you want to convert to: "))

        if convert_to == 1:
            to = int(input("please enter how many gigabytes: "))
            a = to*1024*1024*1024
            print(str(a)+" bytes")

        elif convert_to == 2:
            to = int(input("please enter how many gigabytes: "))
            a = to*1024*1024
            print(str(a)+" kilobytes")            

        elif convert_to == 3:
            to = int(input("please enter how many gigabytes: "))
            a = to*1024
            print(str(a)+"  megabytes")

        elif convert_to == 4:
            to = int(input("please enter how many gigabytes: "))
            a = to/1024
            print(str(a)+" terabytes")

        elif convert_to == 5:
            to = int(input("please enter how many gigabytes: "))
            a = to/1024/1024
            print(str(a)+"  petabytes")

    elif convert_from ==5:
        print("please choose what you want to convert to")
        print("============================================================")
        print("-------------------------convert to-------------------------")
        print("============================================================")
        print("1-byte\n2-kilobyte\n3-megabyte\n4-gigabyte\n5-petabyte")

        convert_to = int(input("please choose what you want to convert to: "))

        if convert_to == 1:
            to = int(input("please enter how many terabytes: "))
            a = to*1024*1024*1024*1024
            print(str(a)+" bytes")

        elif convert_to == 2:
            to = int(input("please enter how many terabytes: "))
            a = to*1024*1024*1024
            print(str(a)+" kilobytes")      

        elif convert_to == 3:
            to = int(input("please enter how many terabytes: "))
            a = to*1024*1024
            print(str(a)+"  megabytes")

        elif convert_to == 4:
            to = int(input("please enter how many terabytes: "))
            a = to*1024
            print(str(a)+" gigabytes")

        elif convert_to == 5:
            to = int(input("please enter how many terabytes: "))
            a = to/1024
            print(str(a)+"  petabytes")

    elif convert_from ==6:
        print("please choose what you want to convert to")
        print("============================================================")
        print("-------------------------convert to-------------------------")
        print("============================================================")
        print("1-byte\n2-kilobyte\n3-megabyte\n4-gigabyte\n5-tera")

        convert_to = int(input("please choose what you want to convert to: "))

        if convert_to == 1:
            to = int(input("please enter how many petabytes: "))
            a = to*1024*1024*1024*1024*1024
            print(str(a)+" bytes")

        elif convert_to == 2:
            to = int(input("please enter how many petabytes: "))
            a = to*1024*1024*1024*1024
            print(str(a)+" kilobytes")      

        elif convert_to == 3:
            to = int(input("please enter how many petabytes: "))
            a = to*1024*1024*1024
            print(str(a)+"  megabytes")

        elif convert_to == 4:
            to = int(input("please enter how many petabytes: "))
            a = to*1024*1024
            print(str(a)+" gigabytes")

        elif convert_to == 5:
            to = int(input("please enter how many petabytes: "))
            a = to*1024
            print(str(a)+"  terabytes")
# speed calculator
elif calc_choosen ==7:
    def est(data_size) :
        answer = data_size / internet_speed
        print("   ")
        print(f" Estimated Time Is {answer / 3600:,} Hours\n {answer / 43200:,} Days\n {answer / 60:,} Minutes\n {answer} Seconds")

    print("==============================")
    print("-------------Menu-------------")
    print("==============================")
    print("   ")
    print("--Hint--")
    print("   ")
    print(" If Your Innternet Speed Less Than 1mb/sec Type {0.} Before Your Speed ")
    print("=" * 80)

    print(" 1-Internet Speed \n 2-Data Per Unit Time ")

    choosen = int(input(" Please Choose Number From Menu : "))

    if choosen == 1 :
        internet_speed = float(input(" What Is Your Internet Speed : "))

        min = internet_speed * 60
        hour = internet_speed * 3600
        day = internet_speed * 43200
        print("   ")
        print(f" You Will Download {min:,} Megabyte Per Minute or {min / 1000:,} Gigabyte Per Minute ")
        print(f" and {hour / 1000:,} Gigabyte Per Hour or {hour:,} Megabyte Per Hour ")
        print(f" and {day / 1000:,} Gigabyte Per Day or {day:,} Megabyte Per Day ")

    elif choosen == 2 :
        internet_speed = float(input(" What Is Your Internet Speed : "))
        data_size = float(input(" Type Your Data Size In Megabytes : "))
        est(data_size)
print(" ")