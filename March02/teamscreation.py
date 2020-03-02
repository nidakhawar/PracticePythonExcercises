file=open("teams.txt","w")
teams=["England","Man United","Ireland","Wales","Argentina"]
newfile="\n".join(teams)
file.write(newfile)
file.close()
