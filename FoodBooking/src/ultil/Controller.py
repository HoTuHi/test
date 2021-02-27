# add category
def addCategory(conn, CategoriesName):
    sql = """
        INSERT INTO Categories(CategoriesName)
        VALUES (?,?)
    """
    try:
        conn.execute(sql, (CategoriesName))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"
# add Positons


def addPosition(posName, cityId):
    sql = """
        INSERT INTO Positons(posName,cityId)
        VALUES (?,?)
    """
    try:
        conn.execute(sql, (posName, cityId))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"


# add Ads
def addAds(imgId):
    sql = """
        INSERT INTO Ads(imgId)
        VALUES (?)
    """
    try:
        conn.execute(sql, (imgId,))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"


# add city
def addCity(cityName):
    sql = """
        INSERT INTO City(cityName)
        VALUES (?)
    """
    try:
        conn.execute(sql, (cityName))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"
