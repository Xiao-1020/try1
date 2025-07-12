def movingtower(total,origin,middle,goal):
    if total>1:
        movingtower(total-1,origin,goal,middle)
        process(total,origin,goal)
        movingtower(total-1,middle,origin,goal)
    elif total==1:
        process(total,origin,goal)
def process(total,origin,goal):
    print("put {} from {} to {}".format(str(total),origin,goal))
total=int(input())
origin="1"
middle="2"
goal="3"
movingtower(total,origin,middle,goal)