

#message = input("Message to encode: ")
message = r"""
Me to myself : "You can't make memes in Intcode"

Me : *makes meme in Intcode*

Me :

####&&&&&((((((((((#####%%###########################################%/////////////////////////////
####&&&&&&((((((#######%%##########################################%///////((((((//////((//////((
###%%&&&&***,&(########%%##########################################%%///////(((((((((((((/(//((((
##%%//&&&***,,,,,&%#######%###########################################%//////((((((//(///(/////////
##%(///&&%**,,,,,,,,####%%##########################################%//////((((/(/(/////////////(
#%%(////&&***,,,,,,,,,/#%%##########################################%%//////////(////////////(&&,
%%(//////&&/**,,,,,,,,,,,#&%###########################################%/////////(/(((((((/&&/,,,,,
%#(//////(&//*,,,,,,,,,,,,,,#########################################%%/////((((((((&&%,,,,,,,,,,
%((((((((((&//*,,,,,,,,,,,,,,,,#######################################%#(((((((&&*,,,,,,,,,,,,,,,
#######(((((&///*,,,,,,,,,,,,,,,,######################################%((((&*,,,,,,,,,,,,,,,,,,,
#########((((&(//*,,,,,,,,,,,,,,,,,&%####################################&&%,,,,,,,,,,,,,,,,,,,,,,,
###########((##&//*,,,,,,,,,,,,,,,,,,*#############&&&&&&&&&%##&&&&&&/,,,,,,,,,,,,,,,,,,,,,,,,,,,
################&%/**,,,,,,,,,,,,,,,,,,*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
##################&***,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&
###################&&**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&#
%####################&***,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**####
%#%%%#####%###########&&**,%%*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,***######
%%%%%%%%%%%%%%%%%#######&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,****(########
%%%%%%%%%%%%%%%%%%%%####&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,***###########
%%%%%%%%%%%%%%%%%%%%%###&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/############
%%%%%%%%%%%%%%%%%%%%###&*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*############
%%%%%%%%%%%%%%%%%%%###%%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*(%&*,,,,,,,,,,,,**###########
%%%%%%%%%%%%%%%%%%####&,,,,,,,,,/&/ ,&,,,,,,,,,,,,,,,,,,,,,,,,#&   .&&%,,,,,,,,,,,,*%############
%%%%%%%%%%%%%%%%#####%%,,,,,,,,,&&  ,&&&/,,,,,,,,,,,,,,,,,,,,,,,&&   &&&&*,,,,,,,,,,,,*######((((
&&&&&&&&%%%%#########&,,,,,,,,,,%&&%&&&&/,,,,,,,,,,,,,,,,,,,,,,,*&&%&&&&(,,,,,,,,,,,,,*####((((((
&&&&&&&&&&%%%########&,,,,,,,,,,,/%&&&%*,,,,,,,,,,,,,,,,,,,,,,,,,,*((/*,,,,,,,,,,,,,,,,*&((((((((((
&&&&&&&&&&&%%#######&*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*&((((((((((
&&&&&&&&&&%%########&,,,,,,,,,,,,,,,,,,,,,,,,,,%%%%%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*%((((((((((
&&&&&&&&&&%%#######&*****,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*//*,,,,,,,,/%(((((((((
%%&&&&%%%%#########&((((((##*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,##(((((((,,,,,,*&(((((((((
###################(((((((((#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(((((((((((/,,,,*(&((((((((
####%%%###########&((((((((((,,,,,,,,,,,,,,,,,,,,**,,,,,,,,,,,,,,,,,,,,,((((((((((((,,,,*/&((((((((
%%%%%%%%%%%#######%((((((((((*,,,,,,,,,,,,,,,,%((((/*//(/,,,,,,,,,,,,,,,((((((((((((,,,,,*/&(((((((
%%%%%%%%%%%%%%####&*((((((((,,,,,,,,,,,,,,,,,%((*********(,,,,,,,,,,,,,,,((((((((((*,,,,,*/%#((((((
%%%%%%%%%%%%%%%%##&,,,,,,,,,,,,,,,,,,,,,,,,,,%(**********(,,,,,,,,,,,,,,,,*((((((/,,,,,,,*//&((((((
%%%%%%%%%%%%%%%###&*,,,,,,,,,,,,,,,,,,,,,,,,,%(**********(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,//##(((((
%%%%%####%%%#######&**,,,,,,,,,,,,,,,,,,,,,,,,#((*******((,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*//&(((((
#########((#((((((((&***,,,,,,,,,,,,,,,,,,,,,,,,(%##((((,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*//%#((((
((((((((((((((((((((((&//*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,////###"""

prevchar = ""
char = ""
templine = ""
data = []
for x in range(len(message)):
    char = message[x]
    if x == 0:
        prevchar = message[x]
    else:
        if char == "\n":
            data.append(templine)
            data.append(char)
            templine = ""
            prevchar = ""
        else:
            if prevchar == char:
                templine = templine+char
                prevchar = char
            else:
                data.append(templine)
                templine = char
                prevchar = char

if len(templine) != 1:
    data.append(templine)
finalprogram = []
for x in data:
    if x == "":
        pass
    elif x == "\n":
        finalprogram.append("1")
        finalprogram.append("10")
    else:
        finalprogram.append(str(len(x)))
        finalprogram.append(str(ord(x[0])))


print("109,48,1201,0,0,44,1001,3,2,3,1201,1,0,19,1001,11,2,11,104,0,1001,43,1,43,8,43,44,45,1006,45,18,1101,0,0,43,8,3,47,40,1106,0,2,99,0,0,0,0," + str(len(finalprogram)) + "," + ",".join(finalprogram))