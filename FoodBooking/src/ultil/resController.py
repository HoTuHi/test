# add restaurant
def addRestaurant(conn, resName, email, phoneNum, imgId, posID):
    sql = """
        INSERT INTO Restaurants(resName,email,phoneNum,imgId,posID)
        VALUES (?,?,?,?,?)
    """
    try:
        conn.execute(sql, (resName, email, phoneNum, imgId, posID))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"

# get all restaurant


def getAllRestaurants(conn):
    sql = """
        SELECT * FROM Restaurants
    """
    cur = conn.execute(sql).fetchall()
    return cur

# update restaurant


def updateRestaurant(conn, resId, resName, email, phoneNum, imgId, posID):
    sql = """
        UPDATE Restaurants
        SET resName=?,email=?,phoneNum=?,imgId=?,posID=?
        WHERE resId =?
    """
    try:
        conn.execute(sql, (resName, email, phoneNum, imgId, posID, resId))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"


def getFoodsOfRestaurant(conn, resId):
    sql = """
        SELECT * FROM Restaurants INNER JOIN Foods
        ON  Foods.resID = (?) WHERE Restaurants.resID = (?)
    """
    try:
        cur = conn.execute(sql, (resId,resId)).fetchall()
        return cur
    except Exception as e:
        print(e)
        return "Failed"
