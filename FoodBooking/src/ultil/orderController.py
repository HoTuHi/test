import foodController


def addOrder(conn, billId, fId, numb, totalPrice):
    sql = """
        INSERT INTO
            Order(billId, fId, numb,totalPrice)
        VALUES
            (?,?,?,?)
    """
    try:
        totalPrice = int(foodController.getFoodDetails(conn, fid)[2]) * numb
        conn.execute(sql, (billId, fId, numb, totalPrice))
        conn.commit()
    except Exception as e:
        print(e)
        return "Failed to add order"
