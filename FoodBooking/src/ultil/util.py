import sqlite3
import foodController
import resController
import userController
import Controller
# import orderController

path = "C:\\Users\\Admin\\Documents\\GitHub\\python\\web\\FoodBooking\\FoodBooking\\Database\\FoodBooking.db"
conn = sqlite3.connect(path)
if __name__ == "__main__":
    print(resController.getFoodsOfRestaurant(conn, 2))
