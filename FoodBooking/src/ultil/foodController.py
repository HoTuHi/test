# add food
def addFood(conn, fName, fPrice, CategoriesId, resId, imgId):
    sql = """
        INSERT INTO
            Foods(fName,fPrice,CategoriesId,resId,imgId)
        VALUES
            (?,?,?,?,?)
    """
    try:
        conn.execute(sql, (fName, fPrice, CategoriesId, resId, imgId))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"

# get all foods


def getAllFoods(conn):
    sql = """
        SELECT * FROM
            Foods
    """
    cur = conn.execute(sql).fetchall()
    return cur


# get food details

def getFoodDetails(conn, fId):
    sql = """
        SELECT * FROM
            Foods
        WHERE
            Foods.fId = ?
    """
    try:
        cur = conn.execute(sql, (fId,))
        return cur.fetchone()
    except Exception as e:
        print(e)
        return "Failed"


# update food


def updateFood(conn, fId, fName, fPrice, CategoriesId, resId, imgId):
    sql = """
        UPDATE Foods
        SET fName=?,
            fPrice=?,
            CategoriesId=?,
            resId=?,
            imgId=?
        WHERE fId=?
    """
    try:
        conn.execute(sql, (fName, fPrice, CategoriesId, resId, imgId, fId))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"
