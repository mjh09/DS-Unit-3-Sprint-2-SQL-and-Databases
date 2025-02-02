import sqlite3

path = "C:/Users/Cactuar/Projects/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3"
conn = sqlite3.connect(path)
curs = conn.cursor()

query = "SELECT COUNT(character_id) FROM charactercreator_character;"
curs.execute(query)
print("Total Characters:", curs.fetchall()[0][0])

query = "SELECT COUNT(character_ptr_id) FROM charactercreator_cleric"
curs.execute(query)
print("Total Cleric Characters:", curs.fetchall()[0][0])

query = "SELECT COUNT(character_ptr_id) FROM charactercreator_fighter"
curs.execute(query)
print("Total Fighter Characters:", curs.fetchall()[0][0])

query = "SELECT COUNT(character_ptr_id) FROM charactercreator_mage"
curs.execute(query)
print("Total Mage Characters:", curs.fetchall()[0][0])

query = "SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer"
curs.execute(query)
print("Total Necromancer Characters:", curs.fetchall()[0][0])

query = "SELECT COUNT(character_ptr_id) FROM charactercreator_thief"
curs.execute(query)
print("Total Thief Characters:", curs.fetchall()[0][0])

query = "SELECT COUNT(item_id) FROM armory_item"
curs.execute(query)
print("Total Items:", curs.fetchall()[0][0])

query = '''SELECT COUNT(item_ptr_id) FROM armory_weapon
 INNER JOIN armory_item ON item_id = item_ptr_id'''
curs.execute(query)
print("Total Weapons in Items:", curs.fetchall()[0][0])


query = "SELECT item_id FROM armory_item EXCEPT SELECT item_ptr_id FROM armory_weapon"
curs.execute(query)
print("Total Items minus Weapons:", len(curs.fetchall()))

query = '''SELECT COUNT(item_id) FROM charactercreator_character_inventory
 GROUP BY character_id'''
curs.execute(query)
print("First 20 Items per Character:", curs.fetchmany(20))

query = '''SELECT COUNT(item_id) FROM charactercreator_character_inventory
 INNER JOIN armory_weapon ON item_id = item_ptr_id GROUP BY character_id'''
curs.execute(query)
print("First 20 Weapons per Character:", curs.fetchmany(20))

query = '''SELECT AVG(item_count) FROM (SELECT COUNT(item_id) 
 AS item_count FROM charactercreator_character_inventory GROUP BY character_id);'''
curs.execute(query)
print('Average Items per Character:', curs.fetchall()[0][0])

query = '''SELECT AVG(weapon_count) FROM (SELECT COUNT(item_id)
 AS weapon_count FROM charactercreator_character_inventory 
 INNER JOIN armory_weapon ON item_id = item_ptr_id GROUP BY character_id)'''
curs.execute(query)
print('Average Weapons per Character:', curs.fetchall()[0][0])
