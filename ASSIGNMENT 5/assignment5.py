#!/usr/bin/env python
#-*-coding:utf-8-*-

import os

item = open("u.item", "r")
data = open("u.data", "r")
genre = open("u.genre", "r")
occupation = open("u.occupation", "r")
user = open("u.user", "r")
review3 = open("review.txt", "w", encoding="utf-8", errors="ignore")
film_genre = open("filmGenre.txt","w")

items, datas, genres, occupations, users = [], [], [], [], []

for i1 in item:
    i0 = i1.rstrip("\n").split("|")
    items.append(i0)
for i3 in genre:
    i2 = i3.rstrip("\n").split("|")
    genres.extend(i2)
for i5 in occupation:
    i4 = i5.rstrip("\n").split("|")
    occupations.extend(i4)
for i7 in user:
    i6 = i7.rstrip("\n").split("|")
    users.append(i6)
for i9 in data:
    i8 = i9.rstrip("\n").split("\t")
    datas.append(i8)

item.close(), genre.close(), occupation.close(), user.close(), data.close()

write = open("write.txt","w")
read = open("write.txt","r")

review1,review2 = [],[]
for b in range(len(items)):
    review1.append(items[b][1])
    review2.append(items[b][1][:-6])
    if b == 0:
        write.write(str(items[b][1][:-6])+"!")
    else:
        write.write("\n"+str(items[b][1][:-6])+"!")
    write.write(items[b][3]+"!")
    for c in range(len(items[b][4:])):
        if items[b][4:][c] == "1":
            review1.append(genres[c * 2])
            review2.append(genres[c * 2])
            write.write(str(genres[c * 2])+" ")
        c += 1
    b += 1
write.close()

reads = []
for line in read:
    gen = line.rstrip("\n").split("!")
    reads.append(gen)
read.close()

# Step 3:
film = os.path.abspath(os.getcwd() + "\\film")
filmList = [f for f in os.listdir(film) if f.endswith('.txt')]

films, film_names, film_id = [], [], []
for f in range(len(filmList)):
    file1 = open(os.path.abspath(os.getcwd()) + "\\film\\" + filmList[f], "r")
    for g in file1:
        h = g.rstrip("\n").split("(")
        if h[0].isupper():
            films.append(h)
        else:
            continue
    file1.close()

for i in range(len(films)):
    film_names.append(films[i][0])

for an in film_names:
    for bn in range(len(items)):
        if an == items[bn][1][:-6].upper():
            film_id.append(items[bn][0])

class Error(Exception):
    pass
class FileHasNotFileError(Error):
    # File is not found in Folder
    pass

itemsFilms = []
for k in items:
    if k[1].find("("):
        itemsFilms.append(k[1][:k[1].find("(")].upper())
    else:
        itemsFilms.append(k[1][:-6].upper())

x = [x for x in film_names]
for l in range(len(items)):
    try:
        if items[l][1][:-6].upper() in x:
            review3.write(str(items[l][0])+" "+str(items[l][1][:-6])+"is found in Folder."+"\n")
        else:
            raise FileHasNotFileError
    except FileHasNotFileError:
        review3.write(str(items[l][0])+" "+str(items[l][1][:-6])+"is not found in Folder. Look at "+str(items[l][3])+"\n")
review3.close()

filmGuess = os.path.abspath(os.getcwd() + "\\filmGuess")
filmGuessList = [f for f in os.listdir(filmGuess) if f.endswith('.txt')]

Guess = []
film_guess = []
for x in range(len(filmGuessList)):
    file2 = open(os.path.abspath(os.getcwd()) + "\\filmGuess\\" + filmGuessList[x], "r")
    film_guess.append(file2.readlines())
    file2.seek(0)
    for y in file2:
        z = y.rstrip("\n").split("(director")
        if z[0].isupper():
            Guess.append(z[0])
            break
    file2.close()
film_genre.write("Guess Genres of Movie based on Movies"+"\n")
for ihh in Guess:
    film_genre.write(str(ihh)+" : "+"\n")

aaa = []
for xq in film_id:
    for üş in range(len(datas)):
        if datas[üş][1] == xq:
            aaa.append(datas[üş])

user_detail1 = []
user_detail2 = []
for yq in range(len(aaa)):
    for üş in range(len(users)):
        if aaa[yq][0] == users[üş][0]:
            user_detail1.append(aaa[yq][0:3])
            user_detail2.append(users[üş][1:])

film = os.path.abspath(os.getcwd() + "\\film")
filmList = [f for f in os.listdir(film) if f.endswith('.txt')]

uuu = []# Review File
for il in range(len(film_names)):
    for f in range(len(filmList)):
        file3 = open(os.path.abspath(os.getcwd())+"\\film\\"+filmList[f],"r")
        b = len(file3.readlines())
        file3.seek(0)
        if file3.readlines()[0][:7] == film_names[il][:7]:
            file3.seek(0)
            uuu.append(str(file3.readlines()[1:b])+"\n")
            break
        file3.close()

print(os.makedirs(os.path.abspath(os.getcwd())+"\\filmList"))
for ü in range(len(film_names)):
    with open(os.path.abspath(os.getcwd())+"\\filmList\\"+film_id[ü]+".html", "w") as html:
        html.write("<html>"+"\n")
        html.write("<head>"+"\n")
        html.write("<title>"+str(film_names[ü].lower().title())+"</title>"+"\n"+"</head>"+"\n")
        html.write("<body> <font color='#FF0000' size='6' face='Times New Roman'> "+film_names[ü].lower().title()+"</font> <br>"+"\n")
        for ün in range(len(reads)):
            if reads[ün][0].upper() == film_names[ü]:
                html.write("<b> Genre : </b> "+str(reads[ün][2])+"<br>"+"\n")
                html.write("<b> IMDB Link : </b> <a href="+str(reads[ün][1])+"> "+str(film_names[ü].lower().title())+"</a> <br>"+"\n")
                html.write("<b> Rewiew : <font color='#FFFFFF' size='5' face='Times New Roman'> </font> </b> <br>")
                html.write(uuu[ü][2:len(uuu[ü])-5]+"<br>"+"\n")
                ün += 1
            else:
                ün += 1
        html.write("<br>"+"\n")
        a,total = [],[]
        for klm in range(len(user_detail1)):
            if film_id[ü] == user_detail1[klm][1]:
                a.append(1)
                total.append(int(user_detail1[klm][2]))
        html.write("<b> Total User: </b> "+str(sum(a))+" / "+" <b> Total Rate: </b> "+str(sum(total)/sum(a))+" <br><br> "+"\n")
        html.write("<b> User who rate the film: </b><br>")
        for inş in range(len(user_detail1)):
            if film_id[ü] == user_detail1[inş][1]:
                a = int(user_detail2[inş][2])
                html.write("<b> User: </b> "+str(user_detail1[inş][0])+"<b> Rate: </b> "+str(user_detail1[inş][2])+"<br>")
                html.write("<b> User Detail: </b><b> Age: </b> "+str(user_detail2[inş][0])+"<b> Gender: </b> "+str(user_detail2[inş][1])
                           +"<b> Occupation: </b> "+str(occupations[(2*a)+1])+"<b> Zip Code: </b> "+str(user_detail2[inş][3])+"<br> "+"\n")
        html.write("</body>"+"\n")
        html.write("</html>")

stopwords = open("stopwords.txt", "r", encoding="iso-8859-1", errors="ignore")
stopword = []
for line in stopwords:
    stopword.append(line.rstrip("\n"))
