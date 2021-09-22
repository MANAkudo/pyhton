def rensou(num):
    keys = list(num.keys())

    for key in keys:
        value = num.get(key)
        print(key,":",value,sep="")


color = {
    "赤":"red",
    "白":"white",
    "黒":"black",
    "青":"blue",
    "緑":"green",
}

rensou(color)

