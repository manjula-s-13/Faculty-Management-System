def viewfac():
    def  submitview():
        try:
            fname=fnameviewentry.get()
            fid=fidviewentry.get()

            strr='select fid from basic_details where fid=%s and fname=%s'
            mycursor.execute(strr,(fid,fname))
            check= mycursor.fetchall()                   #.............................................(to make sure fid n fname belongs to same faculty)
            if(check==()):
                messagebox.showerror('Error','Data entered is incorrect... Try again')
                viewroot.destroy()
            else:
                submitviewroot=Tk()
                submitviewroot.title("View Details")
                submitviewroot.geometry('1360x730')
                submitviewroot.config(bg='firebrick')
                submitviewroot.resizable(0,0)
                viewroot.destroy()

            
        except:
            viewroot.destroy()
            messagebox.showerror('Error','Something went wrong... Try again')

 #..........................................................................................................................................
        fidval=StringVar()
        fnameval=StringVar()
        mnameval=StringVar()
        lnameval=StringVar()
        yr_joinedval=StringVar()
        subval=StringVar()
        salval=StringVar()
        prvs_expval=StringVar()
        domainval=StringVar()
        
        degval=StringVar()
        marksval=StringVar()
        yr_passval=StringVar()
        clg_stdval=StringVar()
        clgcityval=StringVar()
        ofcval=StringVar()
        postval=StringVar()
        cityval=StringVar()
        yr_wrkdval=StringVar()

        phnoval=StringVar()
        emailval=StringVar()
        addval=StringVar()
        dobval=StringVar()
        bldgrpval=StringVar()
        hobval=StringVar()
        marval=StringVar()
        extraval=StringVar()

#......................................................................................................................BASIC DETAILS

        basiclabel=Label(submitviewroot,text="Basic Details*",font=('Times New Roman Bold Italic',20),bg='firebrick')
        basiclabel.place(x=10,y=5)

        fidlabel=Label(submitviewroot,text='Faculty ID : ',font=('Times New Roman Italic',15),bg='firebrick')
        fidlabel.place(x=25,y=50)
        strr='select fid from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        fidval= mycursor.fetchall()
        fidentry=Label(submitviewroot,font=('Times New Roman',15),text=fidval,relief=RIDGE,borderwidth=2)
        fidentry.place(x=200,y=50,width=450,height=25)

        fnamelabel=Label(submitviewroot,text='First Name : ',font=('Times New Roman Italic',15),bg='firebrick')
        fnamelabel.place(x=25,y=90)
        strr='select fname from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        fnameval= mycursor.fetchall()
        fnameentry=Label(submitviewroot,font=('Times New Roman',15),text=fnameval,relief=RIDGE,borderwidth=2)
        fnameentry.place(x=200,y=90,width=450,height=25)

        mnamelabel=Label(submitviewroot,text='Middle Name : ',font=('Times New Roman Italic',15),bg='firebrick')
        mnamelabel.place(x=25,y=130)
        strr='select mname from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        mnameval= mycursor.fetchall()
        mnameentry=Label(submitviewroot,font=('Times New Roman',15),text=mnameval,relief=RIDGE,borderwidth=2)
        mnameentry.place(x=200,y=130,width=450,height=25)

        lnamelabel=Label(submitviewroot,text='Last Name : ',font=('Times New Roman Italic',15),bg='firebrick')
        lnamelabel.place(x=25,y=170)
        strr='select lname from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        lnameval= mycursor.fetchall()
        lnameentry=Label(submitviewroot,font=('Times New Roman',15),text=lnameval,relief=RIDGE,borderwidth=2)
        lnameentry.place(x=200,y=170,width=450,height=25)

        yrjoinedlabel=Label(submitviewroot,text='Year Joined : ',font=('Times New Roman Italic',15),bg='firebrick')
        yrjoinedlabel.place(x=25,y=210)
        strr='select yr_joined from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        yr_joinedval= mycursor.fetchall()
        yrjoinedentry=Label(submitviewroot,font=('Times New Roman',15),text=yr_joinedval,relief=RIDGE,borderwidth=2)
        yrjoinedentry.place(x=200,y=210,width=450,height=25)

#......................................................................................................................OFFICIAL    
        officiallabel=Label(submitviewroot,text="Official*",font=('Times New Roman Bold Italic',20),bg='firebrick')
        officiallabel.place(x=10,y=260)
        
        subjectlabel=Label(submitviewroot,text='Subject : ',font=('Times New Roman Italic',15),bg='firebrick')
        subjectlabel.place(x=25,y=305)
        strr='select subject from official where fid=%s'
        mycursor.execute(strr,(fid))
        subval= mycursor.fetchall()
        subjectentry=Label(submitviewroot,font=('Times New Roman',15),text=subval,relief=RIDGE,borderwidth=2)
        subjectentry.place(x=200,y=305,width=450,height=25)

        salarylabel=Label(submitviewroot,text='Salary : ',font=('Times New Roman Italic',15),bg='firebrick')
        salarylabel.place(x=25,y=345)
        strr='select salary from official where fid=%s'
        mycursor.execute(strr,(fid))
        salval= mycursor.fetchall()
        salaryentry=Label(submitviewroot,font=('Times New Roman',15),text=salval,relief=RIDGE,borderwidth=2)
        salaryentry.place(x=200,y=345,width=450,height=25)

        prvsyrexplabel=Label(submitviewroot,text='''Previous Years
of Experience : ''',font=('Times New Roman Italic',15),bg='firebrick')
        prvsyrexplabel.place(x=23,y=375)
        strr='select yr_exp from official where fid=%s'
        mycursor.execute(strr,(fid))
        prvs_expval= mycursor.fetchall()
        prvsyrexpentry=Label(submitviewroot,font=('Times New Roman',15),text=prvs_expval,relief=RIDGE,borderwidth=2)
        prvsyrexpentry.place(x=200,y=385,width=450,height=25)

        domainlabel=Label(submitviewroot,text='Domain ID : ',font=('Times New Roman Italic',15),bg='firebrick')
        domainlabel.place(x=25,y=435)
        strr='select domain_id from official where fid=%s'
        mycursor.execute(strr,(fid))
        domainval= mycursor.fetchall()
        domainentry=Label(submitviewroot,font=('Times New Roman',15),text=domainval,relief=RIDGE,borderwidth=2)
        domainentry.place(x=200,y=435,width=450,height=25)

#........................................................................................................................EDUCATION
        educationlabel=Label(submitviewroot,text="Education*",font=('Times New Roman Bold Italic',20),bg='firebrick')
        educationlabel.place(x=10,y=485)
        
        degreelabel=Label(submitviewroot,text='Degree : ',font=('Times New Roman Italic',15),bg='firebrick')
        degreelabel.place(x=25,y=530)
        strr='select degree from education where fid=%s'
        mycursor.execute(strr,(fid))
        degval= mycursor.fetchall()
        degreeentry=Label(submitviewroot,font=('Times New Roman',15),text=degval,relief=RIDGE,borderwidth=2)
        degreeentry.place(x=200,y=530,width=450,height=25)

        marksobtlabel=Label(submitviewroot,text='Marks Obtained : ',font=('Times New Roman Italic',15),bg='firebrick')
        marksobtlabel.place(x=25,y=570)
        strr='select marks_obt from education where fid=%s'
        mycursor.execute(strr,(fid))
        marksval= mycursor.fetchall()
        marksobtentry=Label(submitviewroot,font=('Times New Roman',15),text=marksval,relief=RIDGE,borderwidth=2)
        marksobtentry.place(x=200,y=570,width=450,height=25)

        yrofpasslabel=Label(submitviewroot,text='Year of Passing : ',font=('Times New Roman Italic',15),bg='firebrick')
        yrofpasslabel.place(x=25,y=610)
        strr='select yr_of_pass from education where fid=%s'
        mycursor.execute(strr,(fid))
        yr_passval= mycursor.fetchall()
        yrofpassentry=Label(submitviewroot,font=('Times New Roman',15),text=yr_passval,relief=RIDGE,borderwidth=2)
        yrofpassentry.place(x=200,y=610,width=450,height=25)

        collegelabel=Label(submitviewroot,text='College Studied : ',font=('Times New Roman Italic',15),bg='firebrick')
        collegelabel.place(x=25,y=650)
        strr='select college from education where fid=%s'
        mycursor.execute(strr,(fid))
        clg_stdval= mycursor.fetchall()
        collegeentry=Label(submitviewroot,font=('Times New Roman',15),text=clg_stdval,relief=RIDGE,borderwidth=2)
        collegeentry.place(x=200,y=650,width=450,height=25)

        clgcitylabel=Label(submitviewroot,text='City : ',font=('Times New Roman Italic',15),bg='firebrick')
        clgcitylabel.place(x=25,y=690)
        strr='select clg_city from education where fid=%s'
        mycursor.execute(strr,(fid))
        clgcityval= mycursor.fetchall()
        clgcityentry=Label(submitviewroot,font=('Times New Roman',15),text=clgcityval,relief=RIDGE,borderwidth=2)
        clgcityentry.place(x=200,y=690,width=450,height=25)
#..................................................................................................................................

#....................................................................................................................................LEFT

#........................................................................................................................................PRVS EXP
        prvsexplabel=Label(submitviewroot,text="Previous Experience (if any)",font=('Times New Roman Bold Italic',20),bg='firebrick')
        prvsexplabel.place(x=700,y=5)
        
        orgofficelabel=Label(submitviewroot,text='Institution/Office : ',font=('Times New Roman Italic',15),bg='firebrick')
        orgofficelabel.place(x=715,y=50)
        strr='select org_office from prvs_exp where fid=%s'
        mycursor.execute(strr,(fid))
        ofcval= mycursor.fetchall()
        orgofficeentry=Label(submitviewroot,font=('Times New Roman',15),text=ofcval,relief=RIDGE,borderwidth=2)
        orgofficeentry.place(x=890,y=50,width=450,height=25)

        postlabel=Label(submitviewroot,text='Post : ',font=('Times New Roman Italic',15),bg='firebrick')
        postlabel.place(x=715,y=90)
        strr='select post from prvs_exp where fid=%s'
        mycursor.execute(strr,(fid))
        postval= mycursor.fetchall()
        postentry=Label(submitviewroot,font=('Times New Roman',15),text=postval,relief=RIDGE,borderwidth=2)
        postentry.place(x=890,y=90,width=450,height=25)

        citylabel=Label(submitviewroot,text='City : ',font=('Times New Roman Italic',15),bg='firebrick')
        citylabel.place(x=715,y=130)
        strr='select city from prvs_exp where fid=%s'
        mycursor.execute(strr,(fid))
        cityval= mycursor.fetchall()
        cityentry=Label(submitviewroot,font=('Times New Roman',15),text=cityval,relief=RIDGE,borderwidth=2)
        cityentry.place(x=890,y=130,width=450,height=25)

        noofyrworkedlabel=Label(submitviewroot,text='No. of Years Worked : ',font=('Times New Roman Italic',15),bg='firebrick')
        noofyrworkedlabel.place(x=715,y=170)
        strr='select yrs_workd from prvs_exp where fid=%s'
        mycursor.execute(strr,(fid))
        yr_wrkdval= mycursor.fetchall()
        noofyrworkedentry=Label(submitviewroot,font=('Times New Roman',15),text=yr_wrkdval,relief=RIDGE,borderwidth=2)
        noofyrworkedentry.place(x=890,y=170,width=450,height=25)

#...........................................................................................................................PERSONAL   
        personallabel=Label(submitviewroot,text="Personal*",font=('Times New Roman Bold Italic',20),bg='firebrick')
        personallabel.place(x=700,y=220)
        
        phnolabel=Label(submitviewroot,text='Phone Number : ',font=('Times New Roman Italic',15),bg='firebrick')
        phnolabel.place(x=715,y=265)
        strr='select phno from personal where fid=%s'
        mycursor.execute(strr,(fid))
        phnoval= mycursor.fetchall()
        phnoentry=Label(submitviewroot,font=('Times New Roman',15),text=phnoval,relief=RIDGE,borderwidth=2)
        phnoentry.place(x=890,y=265,width=450,height=25)

        emaillabel=Label(submitviewroot,text='E-mail : ',font=('Times New Roman Italic',15),bg='firebrick')
        emaillabel.place(x=715,y=305)
        strr='select email from personal where fid=%s'
        mycursor.execute(strr,(fid))
        emailval= mycursor.fetchall()
        emailentry=Label(submitviewroot,font=('Times New Roman',15),text=emailval,relief=RIDGE,borderwidth=2)
        emailentry.place(x=890,y=305,width=450,height=25)

        addresslabel=Label(submitviewroot,text='Address : ',font=('Times New Roman Italic',15),bg='firebrick')
        addresslabel.place(x=715,y=345)
        strr='select address from personal where fid=%s'
        mycursor.execute(strr,(fid))
        addval= mycursor.fetchall()
        addressentry=Label(submitviewroot,font=('Times New Roman',15),text=addval,relief=RIDGE,borderwidth=2)
        addressentry.place(x=890,y=345,width=450,height=25)

        doblabel=Label(submitviewroot,text='DOB : ',font=('Times New Roman Italic',15),bg='firebrick')
        doblabel.place(x=715,y=385)
        strr='select dob from personal where fid=%s'
        mycursor.execute(strr,(fid))
        dobval= mycursor.fetchall()
        dobentry=Label(submitviewroot,font=('Times New Roman',15),text=dobval,relief=RIDGE,borderwidth=2)
        dobentry.place(x=890,y=385,width=450,height=25)

        bldgrplabel=Label(submitviewroot,text='Blood Group : ',font=('Times New Roman Italic',15),bg='firebrick')
        bldgrplabel.place(x=715,y=425)
        strr='select bld_grp from personal where fid=%s'
        mycursor.execute(strr,(fid))
        bldgrpval= mycursor.fetchall()
        bldgrpentry=Label(submitviewroot,font=('Times New Roman',15),text=bldgrpval,relief=RIDGE,borderwidth=2)
        bldgrpentry.place(x=890,y=425,width=450,height=25)

#........................................................................................................................OTHERS
        otherslabel=Label(submitviewroot,text="Others",font=('Times New Roman Bold Italic',20),bg='firebrick')
        otherslabel.place(x=700,y=475)
        
        hobbieslabel=Label(submitviewroot,text='Hobbies : ',font=('Times New Roman Italic',15),bg='firebrick')
        hobbieslabel.place(x=715,y=520)
        strr='select hobbies from others where fid=%s'
        mycursor.execute(strr,(fid))
        hobval= mycursor.fetchall()
        hobbiesentry=Label(submitviewroot,font=('Times New Roman',15),text=hobval,relief=RIDGE,borderwidth=2)
        hobbiesentry.place(x=890,y=520,width=450,height=25)

        maritalstatuslabel=Label(submitviewroot,text='Marital Status : ',font=('Times New Roman Italic',15),bg='firebrick')
        maritalstatuslabel.place(x=715,y=560)
        strr='select marital_status from others where fid=%s'
        mycursor.execute(strr,(fid))
        marval= mycursor.fetchall()
        maritalstatusentry=Label(submitviewroot,font=('Times New Roman',15),text=marval,relief=RIDGE,borderwidth=2)
        maritalstatusentry.place(x=890,y=560,width=450,height=25)

        extradeglabel=Label(submitviewroot,text='Extra Degree : ',font=('Times New Roman Italic',15),bg='firebrick')
        extradeglabel.place(x=715,y=600)
        strr='select extra_deg from others where fid=%s'
        mycursor.execute(strr,(fid))
        extraval= mycursor.fetchall()
        extradegentry=Label(submitviewroot,font=('Times New Roman',15),text=extraval,relief=RIDGE,borderwidth=2)
        extradegentry.place(x=890,y=600,width=450,height=25)
        
        submitviewroot.mainloop()
#............................................................................................................................................        

    viewroot=Tk()
    viewroot.title("View Details")
    viewroot.grab_set()
    viewroot.geometry('450x300+30+260')
    viewroot.resizable(0,0)
    viewroot.configure(bg='hotpink')
    #.....................................labels for view.....................

    fnamelabel=Label(viewroot, text='Faculty Name :',font=('Times New Roman',20),bg='hotpink')
    fnamelabel.place(x=15,y=45)

    fidlabel=Label(viewroot, text='Faculty ID :',font=('Times New Roman',20),bg='hotpink')
    fidlabel.place(x=15,y=145)

    #.....................................entry for view.............................

    fnameviewentry=Entry(viewroot,font=('Times New Roman',20),relief=RIDGE,borderwidth=2)
    fnameviewentry.place(x=220,y=47,width=200,height=30)

    fidviewentry=Entry(viewroot,font=('Times New Roman',20),relief=RIDGE,borderwidth=2)
    fidviewentry.place(x=220,y=147,width=200,height=30)

    #......................................view button...............................

    submitbtn=Button(viewroot, text='Submit',font=('times new roman',15),bg='palevioletred',borderwidth=5,command=submitview).place(x=180,y=230) 

    viewroot.mainloop()
############################################################################################################################################################################
########################################################################################## EDIT ###################################################################################
########################################################################################## EDIT ##############################################################################
########################################################################################## EDIT ###################################################################################
    
def editfac():
    def  submitedit():
        def submitentryedit():
            fid1 = fidentry1.get()
            fname1 = fnameentry1.get()
            mname1 = mnameentry1.get()
            lname1 = lnameentry1.get()
            yr_joined1 = yrjoinedentry1.get()   #.........basic
            subject1 = subjectentry1.get()
            salary1 = salaryentry1.get()
            yr_exp1 = prvsyrexpentry1.get()
            domain_id1 = domainentry1.get()     #.......official
            degree1 = degreeentry1.get()
            marks_obt1 = marksobtentry1.get()
            yr_of_pass1 = yrofpassentry1.get()
            college1 = collegeentry1.get()
            clg_city1 = clgcityentry1.get()    #......education
            org_office1 = orgofficeentry1.get()
            post1 = postentry1.get()
            city1 = cityentry1.get()
            yrs_workd1 = noofyrworkedentry1.get()   #......prvs exp
            phno1 = phnoentry1.get()
            email1 = emailentry1.get()
            address1 = addressentry1.get()
            dob1 = dobentry1.get()
            bld_grp1 = bldgrpentry1.get()    #.......personal
            hobbies1 = hobbiesentry1.get()
            marital_status1 = maritalstatusentry1.get()
            extra_deg1 = extradegentry1.get()     #......others

            try:
                strr='update basic_details set fname=%s,mname=%s,lname=%s,yr_joined=%s where fid=%s'
                mycursor.execute(strr,(fname1,mname1,lname1,yr_joined1,fid1))
                strr='update education set degree=%s,marks_obt=%s,yr_of_pass=%s,college=%s,clg_city=%s where fid=%s'
                mycursor.execute(strr,(degree1,marks_obt1,yr_of_pass1,college1,clg_city1,fid1))
                strr='update official set subject=%s,salary=%s,yr_exp=%s,domain_id=%s where fid=%s'
                mycursor.execute(strr,(subject1,salary1,yr_exp1,domain_id1,fid1))
                strr='update personal set phno=%s,email=%s,address=%s,dob=%s,bld_grp=%s where fid=%s'
                mycursor.execute(strr,(phno1,email1,address1,dob1,bld_grp1,fid1))
                strr='update prvs_exp set org_office=%s,post=%s,city=%s,yrs_workd=%s where fid=%s'
                mycursor.execute(strr,(org_office1,post1,city1,yrs_workd1,fid1))
                strr='update others set hobbies=%s,marital_status=%s,extra_deg=%s where fid=%s'
                mycursor.execute(strr,(hobbies1,marital_status1,extra_deg1,fid1))
                con.commit()
                messagebox.showinfo('Notification','Editing successful',parent=submiteditroot)
                strr='select fname,fid from basic_details'
                mycursor.execute(strr)
                datas=mycursor.fetchall()
                facultytable.delete(*facultytable.get_children())
                for i in datas:
                    vv=[i[0],i[1]]
                    facultytable.insert('',END,values=vv)
                submiteditroot.destroy()
            except:
                messagebox.showerror('Error','Something went wrong... Try again')

            
        try:
            fname=fnameeditentry.get()
            fid=fideditentry.get()

            strr='select fid from basic_details where fid=%s and fname=%s'
            mycursor.execute(strr,(fid,fname))
            check= mycursor.fetchall()                  #.................................................. (to make sure fid n fname belongs to same faculty)
            if(check==()):
                messagebox.showerror('Error','Data entered is incorrect... Try again')
                editroot.destroy()
            else:
                submiteditroot=Tk()
                submiteditroot.title("Edit Details")
                submiteditroot.geometry('1360x730')
                submiteditroot.config(bg='darkturquoise')
                submiteditroot.resizable(0,0)
                editroot.destroy()

            
        except:
            editroot.destroy()
            messagebox.showerror('Error','Something went wrong... Try again')

 #..........................................................................................................................................
        fidval=StringVar()
        fnameval=StringVar()
        mnameval=StringVar()
        lnameval=StringVar()
        yr_joinedval=StringVar()
        subval=StringVar()
        salval=StringVar()
        prvs_expval=StringVar()
        domainval=StringVar()
        
        degval=StringVar()
        marksval=StringVar()
        yr_passval=StringVar()
        clg_stdval=StringVar()
        clgcityval=StringVar()
        ofcval=StringVar()
        postval=StringVar()
        cityval=StringVar()
        yr_wrkdval=StringVar()

        phnoval=StringVar()
        emailval=StringVar()
        addval=StringVar()
        dobval=StringVar()
        bldgrpval=StringVar()
        hobval=StringVar()
        marval=StringVar()
        extraval=StringVar()

#......................................................................................................................BASIC DETAILS

        basiclabel=Label(submiteditroot,text="Basic Details*",font=('Times New Roman Bold Italic',20),bg='darkturquoise')
        basiclabel.place(x=10,y=5)

        fidlabel1=Label(submiteditroot,text='Faculty ID : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        fidlabel1.place(x=25,y=50)
        strr='select fid from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        fidval= mycursor.fetchall()
        fidentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        fidentry1.insert(0,fidval)
        fidentry1.place(x=200,y=50,width=450,height=25)

        fnamelabel1=Label(submiteditroot,text='First Name : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        fnamelabel1.place(x=25,y=90)
        strr='select fname from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        fnameval= mycursor.fetchall()
        fnameentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        fnameentry1.insert(0,fnameval)
        fnameentry1.place(x=200,y=90,width=450,height=25)

        mnamelabel1=Label(submiteditroot,text='Middle Name : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        mnamelabel1.place(x=25,y=130)
        strr='select mname from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        mnameval= mycursor.fetchall()
        mnameentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        mnameentry1.insert(0,mnameval)
        mnameentry1.place(x=200,y=130,width=450,height=25)

        lnamelabel1=Label(submiteditroot,text='Last Name : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        lnamelabel1.place(x=25,y=170)
        strr='select lname from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        lnameval= mycursor.fetchall()
        lnameentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        lnameentry1.insert(0,lnameval)
        lnameentry1.place(x=200,y=170,width=450,height=25)

        yrjoinedlabel1=Label(submiteditroot,text='Year Joined : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        yrjoinedlabel1.place(x=25,y=210)
        strr='select yr_joined from basic_details where fid=%s'
        mycursor.execute(strr,(fid))
        yr_joinedval= mycursor.fetchall()
        yrjoinedentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        yrjoinedentry1.insert(0,yr_joinedval)
        yrjoinedentry1.place(x=200,y=210,width=450,height=25)

#......................................................................................................................OFFICIAL    
        officiallabel=Label(submiteditroot,text="Official*",font=('Times New Roman Bold Italic',20),bg='darkturquoise')
        officiallabel.place(x=10,y=260)
        
        subjectlabel1=Label(submiteditroot,text='Subject : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        subjectlabel1.place(x=25,y=305)
        strr='select subject from official where fid=%s'
        mycursor.execute(strr,(fid))
        subval= mycursor.fetchall()
        subjectentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        subjectentry1.insert(0,subval)
        subjectentry1.place(x=200,y=305,width=450,height=25)

        salarylabel1=Label(submiteditroot,text='Salary : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        salarylabel1.place(x=25,y=345)
        strr='select salary from official where fid=%s'
        mycursor.execute(strr,(fid))
        salval= mycursor.fetchall()
        salaryentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        salaryentry1.insert(0,salval)
        salaryentry1.place(x=200,y=345,width=450,height=25)

        prvsyrexplabel1=Label(submiteditroot,text='''Previous Years
of Experience : ''',font=('Times New Roman Italic',15),bg='darkturquoise')
        prvsyrexplabel1.place(x=23,y=375)
        strr='select yr_exp from official where fid=%s'
        mycursor.execute(strr,(fid))
        prvs_expval= mycursor.fetchall()
        prvsyrexpentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        prvsyrexpentry1.insert(0,prvs_expval)
        prvsyrexpentry1.place(x=200,y=385,width=450,height=25)

        domainlabel1=Label(submiteditroot,text='Domain ID : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        domainlabel1.place(x=25,y=435)
        strr='select domain_id from official where fid=%s'
        mycursor.execute(strr,(fid))
        domainval= mycursor.fetchall()
        domainentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        domainentry1.insert(0,domainval)
        domainentry1.place(x=200,y=435,width=450,height=25)

#........................................................................................................................EDUCATION
        educationlabel=Label(submiteditroot,text="Education*",font=('Times New Roman Bold Italic',20),bg='darkturquoise')
        educationlabel.place(x=10,y=485)
        
        degreelabel1=Label(submiteditroot,text='Degree : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        degreelabel1.place(x=25,y=530)
        strr='select degree from education where fid=%s'
        mycursor.execute(strr,(fid))
        degval= mycursor.fetchall()
        degreeentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        degreeentry1.insert(0,degval)
        degreeentry1.place(x=200,y=530,width=450,height=25)

        marksobtlabel1=Label(submiteditroot,text='Marks Obtained : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        marksobtlabel1.place(x=25,y=570)
        strr='select marks_obt from education where fid=%s'
        mycursor.execute(strr,(fid))
        marksval= mycursor.fetchall()
        marksobtentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        marksobtentry1.insert(0,marksval)
        marksobtentry1.place(x=200,y=570,width=450,height=25)

        yrofpasslabel1=Label(submiteditroot,text='Year of Passing : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        yrofpasslabel1.place(x=25,y=610)
        strr='select yr_of_pass from education where fid=%s'
        mycursor.execute(strr,(fid))
        yr_passval= mycursor.fetchall()
        yrofpassentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        yrofpassentry1.insert(0,yr_passval)
        yrofpassentry1.place(x=200,y=610,width=450,height=25)

        collegelabel=Label(submiteditroot,text='College Studied : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        collegelabel.place(x=25,y=650)
        strr='select college from education where fid=%s'
        mycursor.execute(strr,(fid))
        clg_stdval= mycursor.fetchall()
        collegeentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        collegeentry1.insert(0,clg_stdval)
        collegeentry1.place(x=200,y=650,width=450,height=25)

        clgcitylabel1=Label(submiteditroot,text='City : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        clgcitylabel1.place(x=25,y=690)
        strr='select clg_city from education where fid=%s'
        mycursor.execute(strr,(fid))
        clgcityval= mycursor.fetchall()
        clgcityentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        clgcityentry1.insert(0,clgcityval)
        clgcityentry1.place(x=200,y=690,width=450,height=25)
#..................................................................................................................................

#....................................................................................................................................LEFT

#........................................................................................................................................PRVS EXP
        prvsexplabel=Label(submiteditroot,text="Previous Experience (if any)",font=('Times New Roman Bold Italic',20),bg='darkturquoise')
        prvsexplabel.place(x=700,y=5)
        
        orgofficelabel1=Label(submiteditroot,text='Institution/Office : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        orgofficelabel1.place(x=715,y=50)
        strr='select org_office from prvs_exp where fid=%s'
        mycursor.execute(strr,(fid))
        ofcval= mycursor.fetchall()
        orgofficeentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        orgofficeentry1.insert(0,ofcval)
        orgofficeentry1.place(x=890,y=50,width=450,height=25)

        postlabel1=Label(submiteditroot,text='Post : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        postlabel1.place(x=715,y=90)
        strr='select post from prvs_exp where fid=%s'
        mycursor.execute(strr,(fid))
        postval= mycursor.fetchall()
        postentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        postentry1.insert(0,postval)
        postentry1.place(x=890,y=90,width=450,height=25)

        citylabel1=Label(submiteditroot,text='City : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        citylabel1.place(x=715,y=130)
        strr='select city from prvs_exp where fid=%s'
        mycursor.execute(strr,(fid))
        cityval= mycursor.fetchall()
        cityentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        cityentry1.insert(0,cityval)
        cityentry1.place(x=890,y=130,width=450,height=25)

        noofyrworkedlabel1=Label(submiteditroot,text='No. of Years Worked : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        noofyrworkedlabel1.place(x=715,y=170)
        strr='select yrs_workd from prvs_exp where fid=%s'
        mycursor.execute(strr,(fid))
        yr_wrkdval= mycursor.fetchall()
        noofyrworkedentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        noofyrworkedentry1.insert(0,yr_wrkdval)
        noofyrworkedentry1.place(x=890,y=170,width=450,height=25)

#...........................................................................................................................PERSONAL   
        personallabel1=Label(submiteditroot,text="Personal*",font=('Times New Roman Bold Italic',20),bg='darkturquoise')
        personallabel1.place(x=700,y=220)
        
        phnolabel1=Label(submiteditroot,text='Phone Number : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        phnolabel1.place(x=715,y=265)
        strr='select phno from personal where fid=%s'
        mycursor.execute(strr,(fid))
        phnoval= mycursor.fetchall()
        phnoentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        phnoentry1.insert(0,phnoval)
        phnoentry1.place(x=890,y=265,width=450,height=25)

        emaillabel1=Label(submiteditroot,text='E-mail : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        emaillabel1.place(x=715,y=305)
        strr='select email from personal where fid=%s'
        mycursor.execute(strr,(fid))
        emailval= mycursor.fetchall()
        emailentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        emailentry1.insert(0,emailval)
        emailentry1.place(x=890,y=305,width=450,height=25)

        addresslabel1=Label(submiteditroot,text='Address : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        addresslabel1.place(x=715,y=345)
        strr='select address from personal where fid=%s'
        mycursor.execute(strr,(fid))
        addval= mycursor.fetchall()
        addressentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        addressentry1.insert(0,addval)
        addressentry1.place(x=890,y=345,width=450,height=25)

        doblabel1=Label(submiteditroot,text='DOB : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        doblabel1.place(x=715,y=385)
        strr='select dob from personal where fid=%s'
        mycursor.execute(strr,(fid))
        dobval= mycursor.fetchall()
        dobentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        dobentry1.insert(0,dobval)
        dobentry1.place(x=890,y=385,width=450,height=25)

        bldgrplabel1=Label(submiteditroot,text='Blood Group : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        bldgrplabel1.place(x=715,y=425)
        strr='select bld_grp from personal where fid=%s'
        mycursor.execute(strr,(fid))
        bldgrpval= mycursor.fetchall()
        bldgrpentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        bldgrpentry1.insert(0,bldgrpval)
        bldgrpentry1.place(x=890,y=425,width=450,height=25)

#........................................................................................................................OTHERS
        otherslabel=Label(submiteditroot,text="Others",font=('Times New Roman Bold Italic',20),bg='darkturquoise')
        otherslabel.place(x=700,y=475)
        
        hobbieslabel1=Label(submiteditroot,text='Hobbies : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        hobbieslabel1.place(x=715,y=520)
        strr='select hobbies from others where fid=%s'
        mycursor.execute(strr,(fid))
        hobval= mycursor.fetchall()
        hobbiesentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        hobbiesentry1.insert(0,hobval)
        hobbiesentry1.place(x=890,y=520,width=450,height=25)

        maritalstatuslabel1=Label(submiteditroot,text='Marital Status : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        maritalstatuslabel1.place(x=715,y=560)
        strr='select marital_status from others where fid=%s'
        mycursor.execute(strr,(fid))
        marval= mycursor.fetchall()
        maritalstatusentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        maritalstatusentry1.insert(0,marval)
        maritalstatusentry1.place(x=890,y=560,width=450,height=25)

        extradeglabel1=Label(submiteditroot,text='Extra Degree : ',font=('Times New Roman Italic',15),bg='darkturquoise')
        extradeglabel1.place(x=715,y=600)
        strr='select extra_deg from others where fid=%s'
        mycursor.execute(strr,(fid))
        extraval= mycursor.fetchall()
        extradegentry1=Entry(submiteditroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
        extradegentry1.insert(0,extraval)
        extradegentry1.place(x=890,y=600,width=450,height=25)

        submiteditbtn=Button(submiteditroot,text='Submit',font=('times new roman',15),bg='deepskyblue',borderwidth=5,command=submitentryedit).place(x=1100,y=650)
        
        submiteditroot.mainloop()
         

    editroot=Tk()
    editroot.title("Edit Details")
    editroot.grab_set()
    editroot.geometry('450x300+30+260')
    editroot.resizable(0,0)
    editroot.configure(bg='mediumslateblue')
    #.....................................labels for edit.....................

    fnamelabel=Label(editroot, text='Faculty Name :',font=('Times New Roman',20),bg='mediumslateblue').place(x=15,y=45)

    fidlabel=Label(editroot, text='Faculty ID :',font=('Times New Roman',20),bg='mediumslateblue').place(x=15,y=145)

    #.....................................entry for edit.............................

    fnameeditentry=Entry(editroot,font=('Times New Roman',20),relief=RIDGE)
    fnameeditentry.place(x=220,y=47,width=200,height=30)

    fideditentry=Entry(editroot,font=('Times New Roman',20),relief=RIDGE)
    fideditentry.place(x=220,y=147,width=200,height=30)

    #......................................edit button...............................

    submitbtn=Button(editroot, text='Submit',font=('times new roman',15),bg='darkslateblue',borderwidth=5,command=submitedit).place(x=180,y=230) 

    editroot.mainloop()

#############################################################################################################################################################################
################################################################################# ADD #####################################################################################
################################################################################# ADD ############################################################################################
################################################################################# ADD ########################################################################################
################################################################################# ADD #############################################################################################

def addfac():
    def submitadd():
        fid = fidentry.get()
        fname = fnameentry.get()
        mname = mnameentry.get()
        lname = lnameentry.get()
        yr_joined = yrjoinedentry.get()   #.........basic
        subject = subjectentry.get()
        salary = salaryentry.get()
        yr_exp = prvsyrexpentry.get()
        domain_id = domainentry.get()     #.......official
        degree = degreeentry.get()
        marks_obt = marksobtentry.get()
        yr_of_pass = yrofpassentry.get()
        college = collegeentry.get()
        clg_city = clgcityentry.get()    #......education
        org_office = orgofficeentry.get()
        post = postentry.get()
        city = cityentry.get()
        yrs_workd = noofyrworkedentry.get()   #......prvs exp
        phno = phnoentry.get()
        email = emailentry.get()
        address = addressentry.get()
        dob = dobentry.get()
        bld_grp = bldgrpentry.get()    #.......personal
        hobbies = hobbiesentry.get()
        marital_status = maritalstatusentry.get()
        extra_deg = extradegentry.get()     #......others
        
        try:
            strr='insert into  basic_details values(%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(fid,fname,mname,lname,yr_joined))
            strr='insert into  education values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(fid,degree,marks_obt,yr_of_pass,college,clg_city))
            strr='insert into  official values(%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(fid,subject,salary,yr_exp,domain_id))
            strr='insert into  personal values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(fid,phno,email,address,dob,bld_grp))
            strr='insert into  prvs_exp values(%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(fid,org_office,post,city,yrs_workd))
            strr='insert into  others values(%s,%s,%s,%s)'
            mycursor.execute(strr,(fid,hobbies,marital_status,extra_deg))
            con.commit()
            messagebox.showinfo('Notification','Data added to database successfully',parent=addroot)
            strr='select fname,fid from basic_details'
            mycursor.execute(strr)
            datas=mycursor.fetchall()
            facultytable.delete(*facultytable.get_children())
            for i in datas:
                vv=[i[0],i[1]]
                facultytable.insert('',END,values=vv)
            addroot.destroy()
                
        except:
            messagebox.showerror('Error','Something went wrong... Try again',parent=addroot)
            addroot.destroy()
                
            
#...............................................................................................................................................
    addroot=Tk()
    addroot.title("Add Details")
    addroot.geometry('1360x730')
    addroot.config(bg='darkgreen')
    addroot.resizable(0,0)
#############################################################.......................................................................
#..........................................................................................................................................
#......................................................................................................................BASIC DETAILS
    basiclabel=Label(addroot,text="Basic Details*",font=('Times New Roman Bold Italic',20),bg='darkgreen')
    basiclabel.place(x=10,y=5)
    fidlabel=Label(addroot,text='Faculty ID : ',font=('Times New Roman Italic',15),bg='darkgreen')
    fidlabel.place(x=25,y=50)
    fidentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    fidentry.place(x=200,y=50,width=450,height=25)
    fnamelabel=Label(addroot,text='First Name : ',font=('Times New Roman Italic',15),bg='darkgreen')
    fnamelabel.place(x=25,y=90)
    fnameentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    fnameentry.place(x=200,y=90,width=450,height=25)
    mnamelabel=Label(addroot,text='Middle Name : ',font=('Times New Roman Italic',15),bg='darkgreen')
    mnamelabel.place(x=25,y=130)
    mnameentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    mnameentry.place(x=200,y=130,width=450,height=25)
    lnamelabel=Label(addroot,text='Last Name : ',font=('Times New Roman Italic',15),bg='darkgreen')
    lnamelabel.place(x=25,y=170)
    lnameentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    lnameentry.place(x=200,y=170,width=450,height=25)
    yrjoinedlabel=Label(addroot,text='Year Joined : ',font=('Times New Roman Italic',15),bg='darkgreen')
    yrjoinedlabel.place(x=25,y=210)
    yrjoinedentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    yrjoinedentry.place(x=200,y=210,width=450,height=25)

#......................................................................................................................OFFICIAL    
    officiallabel=Label(addroot,text="Official*",font=('Times New Roman Bold Italic',20),bg='darkgreen')
    officiallabel.place(x=10,y=260)
    subjectlabel=Label(addroot,text='Subject : ',font=('Times New Roman Italic',15),bg='darkgreen')
    subjectlabel.place(x=25,y=305)
    subjectentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    subjectentry.place(x=200,y=305,width=450,height=25)
    salarylabel=Label(addroot,text='Salary : ',font=('Times New Roman Italic',15),bg='darkgreen')
    salarylabel.place(x=25,y=345)
    salaryentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    salaryentry.place(x=200,y=345,width=450,height=25)
    prvsyrexplabel=Label(addroot,text='''Previous Years
of Experience : ''',font=('Times New Roman Italic',15),bg='darkgreen')
    prvsyrexplabel.place(x=23,y=375)
    prvsyrexpentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    prvsyrexpentry.place(x=200,y=385,width=450,height=25)
    domainlabel=Label(addroot,text='Domain ID : ',font=('Times New Roman Italic',15),bg='darkgreen')
    domainlabel.place(x=25,y=435)
    domainentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    domainentry.place(x=200,y=435,width=450,height=25)

#........................................................................................................................EDUCATION
    educationlabel=Label(addroot,text="Education*",font=('Times New Roman Bold Italic',20),bg='darkgreen')
    educationlabel.place(x=10,y=485)
    degreelabel=Label(addroot,text='Degree : ',font=('Times New Roman Italic',15),bg='darkgreen')
    degreelabel.place(x=25,y=530)
    degreeentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    degreeentry.place(x=200,y=530,width=450,height=25)
    marksobtlabel=Label(addroot,text='Marks Obtained : ',font=('Times New Roman Italic',15),bg='darkgreen')
    marksobtlabel.place(x=25,y=570)
    marksobtentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    marksobtentry.place(x=200,y=570,width=450,height=25)
    yrofpasslabel=Label(addroot,text='Year of Passing : ',font=('Times New Roman Italic',15),bg='darkgreen')
    yrofpasslabel.place(x=25,y=610)
    yrofpassentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    yrofpassentry.place(x=200,y=610,width=450,height=25)
    collegelabel=Label(addroot,text='College Studied : ',font=('Times New Roman Italic',15),bg='darkgreen')
    collegelabel.place(x=25,y=650)
    collegeentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    collegeentry.place(x=200,y=650,width=450,height=25)
    clgcitylabel=Label(addroot,text='City : ',font=('Times New Roman Italic',15),bg='darkgreen')
    clgcitylabel.place(x=25,y=690)
    clgcityentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    clgcityentry.place(x=200,y=690,width=450,height=25)
#..................................................................................................................................

#....................................................................................................................................LEFT

#........................................................................................................................................PRVS EXP
    prvsexplabel=Label(addroot,text="Previous Experience (if any)",font=('Times New Roman Bold Italic',20),bg='darkgreen')
    prvsexplabel.place(x=700,y=5)
    orgofficelabel=Label(addroot,text='Institution/Office : ',font=('Times New Roman Italic',15),bg='darkgreen')
    orgofficelabel.place(x=715,y=50)
    orgofficeentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    orgofficeentry.place(x=890,y=50,width=450,height=25)
    postlabel=Label(addroot,text='Post : ',font=('Times New Roman Italic',15),bg='darkgreen')
    postlabel.place(x=715,y=90)
    postentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    postentry.place(x=890,y=90,width=450,height=25)
    citylabel=Label(addroot,text='City : ',font=('Times New Roman Italic',15),bg='darkgreen')
    citylabel.place(x=715,y=130)
    cityentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    cityentry.place(x=890,y=130,width=450,height=25)
    noofyrworkedlabel=Label(addroot,text='No. of Years Worked : ',font=('Times New Roman Italic',15),bg='darkgreen')
    noofyrworkedlabel.place(x=715,y=170)
    noofyrworkedentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    noofyrworkedentry.place(x=890,y=170,width=450,height=25)

#...........................................................................................................................PERSONAL   
    personallabel=Label(addroot,text="Personal*",font=('Times New Roman Bold Italic',20),bg='darkgreen')
    personallabel.place(x=700,y=220)
    phnolabel=Label(addroot,text='Phone Number : ',font=('Times New Roman Italic',15),bg='darkgreen')
    phnolabel.place(x=715,y=265)
    phnoentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    phnoentry.place(x=890,y=265,width=450,height=25)
    emaillabel=Label(addroot,text='E-mail : ',font=('Times New Roman Italic',15),bg='darkgreen')
    emaillabel.place(x=715,y=305)
    emailentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    emailentry.place(x=890,y=305,width=450,height=25)
    addresslabel=Label(addroot,text='Address : ',font=('Times New Roman Italic',15),bg='darkgreen')
    addresslabel.place(x=715,y=345)
    addressentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    addressentry.place(x=890,y=345,width=450,height=25)
    doblabel=Label(addroot,text='DOB : ',font=('Times New Roman Italic',15),bg='darkgreen')
    doblabel.place(x=715,y=385)
    dobentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    dobentry.place(x=890,y=385,width=450,height=25)
    bldgrplabel=Label(addroot,text='Blood Group : ',font=('Times New Roman Italic',15),bg='darkgreen')
    bldgrplabel.place(x=715,y=425)
    bldgrpentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    bldgrpentry.place(x=890,y=425,width=450,height=25)

#........................................................................................................................OTHERS
    otherslabel=Label(addroot,text="Others",font=('Times New Roman Bold Italic',20),bg='darkgreen')
    otherslabel.place(x=700,y=475)
    hobbieslabel=Label(addroot,text='Hobbies : ',font=('Times New Roman Italic',15),bg='darkgreen')
    hobbieslabel.place(x=715,y=520)
    hobbiesentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    hobbiesentry.place(x=890,y=520,width=450,height=25)
    maritalstatuslabel=Label(addroot,text='Marital Status : ',font=('Times New Roman Italic',15),bg='darkgreen')
    maritalstatuslabel.place(x=715,y=560)
    maritalstatusentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    maritalstatusentry.place(x=890,y=560,width=450,height=25)
    extradeglabel=Label(addroot,text='Extra Degree : ',font=('Times New Roman Italic',15),bg='darkgreen')
    extradeglabel.place(x=715,y=600)
    extradegentry=Entry(addroot,font=('Times New Roman',15),relief=RIDGE,borderwidth=2)
    extradegentry.place(x=890,y=600,width=450,height=25)

    submitbtn=Button(addroot,text='Submit',font=('times new roman',15),bg='mediumseagreen',borderwidth=5,command=submitadd).place(x=1100,y=650)
#..................................................................................................................................
#....................................................................................................................................RIGHT
    addroot.mainloop()
        
##########################################################################################################################################################################
################################################################################ DELETE ######################################################################################
################################################################################ DELETE ############################################################################################
################################################################################ DELETE #########################################################################################
################################################################################ DELETE ##############################################################################################


def deletefac():
    def  submitdelete():
                   
        try:
            fid=fidentry.get()
            fname=fnameentry.get()

            strr='select fid from basic_details where fid=%s and fname=%s'
            mycursor.execute(strr,(fid,fname))
            check= mycursor.fetchall()         #.............................................(to make sure fid n fname belongs to same faculty)

            if(check==()):
                messagebox.showerror('Error','Data entered is incorrect... Try again')
                deleteroot.destroy()

            else:
                strr='delete from basic_details where fid=%s and fname=%s'
                mycursor.execute(strr,(fid,fname))
                datas= mycursor.fetchall()
                con.commit()
                messagebox.showinfo('Notification','Deletion successful')
                deleteroot.destroy()
                strr='select fname,fid from basic_details'
                mycursor.execute(strr)
                datas=mycursor.fetchall()
                facultytable.delete(*facultytable.get_children())
                for i in datas:
                    vv=[i[0],i[1]]
                    facultytable.insert('',END,values=vv)

        except:
            deleteroot.destroy()
            messagebox.showerror('Error','Something went wrong... Try again')

            

    deleteroot=Tk()
    deleteroot.title("Delete Details")
    deleteroot.grab_set()
    deleteroot.geometry('450x300+30+260')
    deleteroot.resizable(0,0)
    deleteroot.configure(bg='salmon')
    #.....................................labels for delete.....................

    fnamelabel=Label(deleteroot, text='Faculty Name :',font=('Times New Roman',20),bg='salmon').place(x=15,y=45)

    fidlabel=Label(deleteroot, text='Faculty ID :',font=('Times New Roman',20),bg='salmon').place(x=15,y=145)

    #.....................................entry for delete.............................
   
    fnameentry=Entry(deleteroot,font=('Times New Roman',20),relief=RIDGE)
    fnameentry.place(x=220,y=47,width=200,height=30)

    fidentry=Entry(deleteroot,font=('Times New Roman',20),relief=RIDGE)
    fidentry.place(x=220,y=147,width=200,height=30)

    #......................................delete button...............................

    submitbtn=Button(deleteroot, text='Submit',font=('times new roman',15),bg='tomato',borderwidth=5,command=submitdelete).place(x=180,y=230) 

    deleteroot.mainloop()

######################################################################################################################################################################
#################################################################### LOGIN #########################################################################################################
#################################################################### LOGIN ####################################################################################################
#################################################################### LOGIN ##########################################################################################################
#################################################################### LOGIN ############################################################################################
#################################################################### LOGIN ###########################################################################################
def connect_win():
    def submitdb(usernameentry,passwordentry):
        global con, mycursor
        user=usernameentry.get()
        password=passwordentry.get()

        if(user== "East@Point" and password== "@#$%asdf*&^%"):
            con=pymysql.connect(host='localhost',user='root',password='Root@Password')
            mycursor=con.cursor()
        else:
            messagebox.showerror('Error','Data entered is incorrect..! Please try again')

        try:
            strr = 'create database facultymngmentsystem'
            mycursor.execute(strr)
            strr = 'use facultymngmentsystem'
            mycursor.execute(strr)
            strr = 'create table basic_details(fid varchar(10) primary key,fname varchar(100) not null,mname varchar(100),lname varchar(100) not null,yr_joined varchar(100) not null)'
            mycursor.execute(strr)
            strr = 'create table official(fid varchar(10),subject varchar(200) not null,salary varchar(100) not null,yr_exp varchar(100) not null,domain_id varchar(100) primary key,foreign key (fid) references basic_details (fid) on delete cascade)'
            mycursor.execute(strr)
            strr = 'create table education(fid varchar(10),degree varchar(200) not null,marks_obt varchar(100) not null,yr_of_pass varchar(100) not null,college varchar(200) not null,clg_city varchar(100) not null,foreign key (fid) references basic_details (fid) on delete cascade)'
            mycursor.execute(strr)
            strr = 'create table prvs_exp(fid varchar(10),org_office varchar(100),post varchar(100),city varchar(100),yrs_workd varchar(100),foreign key (fid) references basic_details (fid) on delete cascade)'
            mycursor.execute(strr)
            strr = 'create table personal(fid varchar(10),phno varchar(100),email varchar(100),address varchar(300),dob varchar(100),bld_grp varchar(100),foreign key (fid) references basic_details (fid) on delete cascade)'
            mycursor.execute(strr)
            strr = 'create table others(fid varchar(10),hobbies varchar(100),marital_status varchar(100),extra_deg varchar(200),foreign key (fid) references basic_details (fid) on delete cascade)'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database Created and Connected',parent=dbroot)
        except:
            strr = 'use facultymngmentsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Connected to the database ....',parent=dbroot)

        dbroot.destroy()
        strr='select fname,fid from basic_details'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        facultytable.delete(*facultytable.get_children())
        for i in datas:
            vv=[i[0],i[1]]
            facultytable.insert('',END,values=vv)

  #.............................................................................................................................................................
    dbroot=Tk()
    dbroot.title("Connect to Database")
    dbroot.geometry('340x250+760+300')
    dbroot.resizable(0,0)
    dbroot.configure(bg='deepskyblue')
          #................................................ connect root labels...................................... 
    usernamelabel=Label(dbroot, text='Username:',font=('Times New Roman Bold Italic',15),bg='deepskyblue').place(x=10,y=20)
    
    passwordlabel=Label(dbroot, text='Password:',font=('Times New Roman Bold Italic',15),bg='deepskyblue').place(x=10,y=100)
    
          #.................................................entry for connectdb.........................................

     
    usernameentry=Entry(dbroot,font=('Times New Roman',15),bd=2)
    usernameentry.place(x=120,y=20,width=200,height=30)

    passwordentry=Entry(dbroot,font=('Times New Roman',15),show='*',bd=2)
    passwordentry.place(x=120,y=100,width=200,height=30)

         #.................................................button for connectdb..........................................
    
    submitbutton=Button(dbroot, text='Connect',font=('Times New Roman',15),bg='cyan',borderwidth=5,command=lambda: submitdb(usernameentry,passwordentry)).place(x=140,y=170)

    dbroot.mainloop()

############################################################################################################################################################################
############################################################################## MAIN PROGRAM ####################################################################################################
############################################################################## MAIN PROGRAM ########################################################################################
############################################################################## MAIN PROGRAM ###############################################################################################
############################################################################## MAIN PROGRAM ###########################################################################################
############################################################################## MAIN PROGRAM ################################################################################################    

import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql

root = tkinter.Tk()
root.geometry("1360x730")
root.title("Faculty Management System")
root.resizable(0,0)
root.configure(bg='whitesmoke')
image1 = ImageTk.PhotoImage(Image.open('C:\\Users\\padmakumari\\Downloads\\Engineering.png'))
panel=tkinter.Label(root, image= image1)
panel.place(x=10,y=10)
heading=tkinter.Label(root, text="Faculty Management System",font=("Times New Roman Bold Italic",45),bg='whitesmoke')
heading.place(x=420,y=10)

#................................FRAMES............................................
#.............................................data entry frame detailing..........................

DataEntryFrame= Frame(root,bg='indigo',relief=GROOVE,borderwidth=5).place(x=30,y=130,width=450,height=570)

viewbtn=Button(DataEntryFrame,text='View Details',font=('Times New Roman',20),bg='violet',borderwidth=3,command=viewfac).place(x=170,y=220)    #..... view

editbtn=Button(DataEntryFrame,text='Edit Details',font=('Times New Roman',20),bg='violet',borderwidth=3,command=editfac).place(x=175,y=320)     #......edit

addbtn=Button(DataEntryFrame,text='Add Details',font=('Times New Roman',20),bg='violet',borderwidth=3,command=addfac).place(x=175,y=420)       #.......add

deletebtn=Button(DataEntryFrame,text='Delete Details',font=('Times New Roman',20),bg='violet',borderwidth=3,command=deletefac).place(x=165,y=520)    #......delete

  #.......................................................show data frame...............................................

ShowDataFrame=Frame(root,bg='gold',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=520,y=130,width=800,height=570)

style = ttk.Style()
style.configure('Treeview.Heading',font=('Times New Roman',25,'bold','italic'),foreground='olive')
style.configure('Treeview',font=('times',20,'bold'),rowheight=35)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
facultytable = Treeview(ShowDataFrame,columns=('Faculty Name','Faculty ID'),yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=facultytable.yview)
facultytable.heading('Faculty Name',text='Faculty Name')
facultytable.heading('Faculty ID',text='Faculty ID')
facultytable['show']='headings'
facultytable.column('Faculty Name',width=450)
facultytable.column('Faculty ID',width=350)

facultytable.pack(fill=BOTH,expand=1)


connectbtn=tkinter.Button(root, text=' Connect ',font=('Times New Roman Bold',15),bg='black',fg='white',command=connect_win,borderwidth=5).place(x=1210,y=20)  #connect button
#####################################################################################################################################


root.mainloop()
