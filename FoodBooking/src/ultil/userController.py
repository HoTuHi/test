# add user

def addUser(conn, imgId, userName, passWord, fullName, email, phoneNum, posID):
    sql = """
        INSERT INTO
            Users(imgId,userName,passWord,fullName,email,phoneNum,posID)
        VALUES
            (?,?,?,?,?,?,?)
    """
    try:
        conn.execute(sql, (imgId, userName, passWord,
                           fullName, email, phoneNum, posID))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"


def getUserDetails(conn, userId):
    sql = """
        SELECT * from
             Users
        WHERE
            userId = ?
    """
    try:
        cur = conn.execute(sql, (userId,))
        conn.commit()
        return cur.fetchone()
    except Exception as e:
        print(e)
        return "Failed"


def updateUser(conn, userId, imgId, userName, passWord, fullName, email, phoneNum, posID):
    sql = """
        UPDATE Users
        SET imgId = ?,
            userName = ?,
            passWord = ?,
            fullName = ?,
            email =?,
            phoneNum =?,
            posID =?
        WHERE userId = ?
    """
    try:
        conn.execute(sql, (imgId, userName, passWord,
                           fullName, email, phoneNum, posID))
        conn.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"

