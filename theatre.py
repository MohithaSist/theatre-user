userdetail=[]
Sign_in=[]
movieList=[]
class UserProfile:
    def userprofile(self):
        self.userid=int(input("Enter userid : "))
        self.username=input("Enter username : ")
        self.password=input("Enter password : ")
        self.gender=input("Enter gender : ")
        self.ph_no=int(input("Enter ph_no : "))
        print()
        userdetail.append(self.userid)
        userdetail.append(self.username)
        userdetail.append(self.password)
        userdetail.append(self.gender)
        userdetail.append(self.ph_no)
    def signin(self):
        self.user_name=input("Enter username : ")
        self.pass_word=input("Enter password : ")
        Sign_in.append(self.user_name)
        Sign_in.append(self.pass_word)
        if ((self.username==self.user_name) and (self.password==self.pass_word)):
            print("Welcome",self.username+'!')
        else:
            print("Enter Valid Login Credentials")
            exit()

class MovieListenins:
    def __init__(self,movieid:int,moviename:str,genere:str,timelen:str,releasedate:str):
        self.movieid=movieid
        self.moviename=moviename
        #self.language=language
        self.genere=genere
        self.timelen=timelen
        self.releasedate=releasedate

class MovieList:
    def moviesdetail(self):
        print()
        lang=input("Enter your language : ")
        print()
        if lang=='tamil':
            tam_movie1=MovieListenins(1.1,'Doctor','suspence','2.30','19/7/2019')
            tam_movie2=MovieListenins(1.2,'Kanchana','horror','1.50.55','8/6/2004')
            tam_movie3=MovieListenins(1.3,'Remo','love','2.00','30/8/2016')

            movieList.append(tam_movie1)
            movieList.append(tam_movie2)
            movieList.append(tam_movie3)

        elif lang=='english':
            eng_movie1=MovieListenins(2.1,'John Wick','suspence','2.00','9/9/2005')
            eng_movie2=MovieListenins(2.2,'The Nun','horror','1.50','3/4/2010')
            eng_movie3=MovieListenins(2.3,'Titanic','love','2.15','21/6/2018')
            movieList.append(eng_movie1)
            movieList.append(eng_movie2)
            movieList.append(eng_movie3)

        elif lang=='telugu':
            tel_movie1=MovieListenins(3.1,'Manan','suspence','2.30','27/6/2005')
            tel_movie2=MovieListenins(3.2,'Magadheera','horror','1.40.60','6/9/2010')
            tel_movie3=MovieListenins(3.3,'Pokiri','love','2.15','7/9/2022')
            movieList.append(tel_movie1)
            movieList.append(tel_movie2)
            movieList.append(tel_movie3)

        elif lang=='hindhi':
            hin_movie1=MovieListenins(4.1,'Pathaan','suspence','2.30','27/6/2005')
            hin_movie2=MovieListenins(4.2,'KGF','thriller','1.40.60','6/9/2010')
            hin_movie3=MovieListenins(4.3,'Bahubali','historical','2.15','7/9/2022')
            movieList.append(hin_movie1)
            movieList.append(hin_movie2)
            movieList.append(hin_movie3)

        
            

        for i in movieList:
            print(i.movieid)
            print(i.moviename)
            print(i.genere)
            print(i.timelen)
            print(i.releasedate)
            print()
        
        

    
        


            

userprof=UserProfile()
userprof.userprofile()
userprof.signin()
lis=MovieList()
lis.moviesdetail()

print()
print(userdetail)
print(Sign_in)
