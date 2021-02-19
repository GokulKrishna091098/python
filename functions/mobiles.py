mobile={
    "iphone 11":{"id":"IPHN11","front-cam":"8px","rear-cam":"14px","manufacturer":"Apple","price":80000},
    "samsung s20":{"id":"SMGS20","front-cam":"8px","rear-cam":"40px","manufacturer":"Samsung","price":60000},
    "vivo v20":{"id":"VV20","front-cam":"10px","rear-cam":"60px","manufacturer":"Vivo","price":50000}
}


def getmodeldetails1(**kwargs):
    id = kwargs["mn"]
    if id in mobile:
        if prp in mobile[id]:
            print(prp, " - ", mobile[id][prp])
        else:
            print("Property Doesn't Exist")
    else:
        print("ID ", id, " Doesnt Exist")


def getmodeldetails(**kwargs):
    id = kwargs["mn"]
    if id in mobile:
        print("\t\tMODEL DETAILS")
        print("\t\t-------------")
        print("\tModel Name   :", id)
        print("\tModel ID     :", mobile[id]["id"])
        print("\tFront Cam    :", mobile[id]["front-cam"])
        print("\tRear Cam     :", mobile[id]["rear-cam"])
        print("\tManufacturer :", mobile[id]["manufacturer"])
        print("\tPrice        : Rs.", mobile[id]["price"])

    else:
        print("Model ", id, " Doesnt Exist")


c="y"
while(c=="y"):
    print("OPTIONS")
    print("=======")
    print("Press 1 for Viewing Full Details")
    print("Press 2 for Viewing Particular Details")
    a=int(input())
    if a==1:
        modelname = (input("Enter Model Name :"))
        getmodeldetails(mn=modelname)
    elif a==2:
        modelname = (input("Enter Model Name :"))
        prp=input("Enter Property:")
        getmodeldetails1(mn=modelname,prp=prp)

    c=input("Do you want to continue?[y/n]")





