import csv
import sqlite3
import pandas as pd

def create_geonames_db(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS zipcodes
                      (country_code TEXT, postal_code TEXT, place_name TEXT,
                       admin_name1 TEXT, admin_code1 TEXT, admin_name2 TEXT,
                       admin_code2 TEXT, admin_name3 TEXT, admin_code3 TEXT,
                       latitude REAL, longitude REAL, accuracy INTEGER)''')

    # with open(csv_file, 'r', encoding='utf-8') as f:
    #     reader = csv.reader(f, delimiter='\t')
    #     for row in reader:
    #         cursor.execute('''INSERT INTO zipcodes VALUES
    #                           (?,?,?,?,?,?,?,?,?,?,?,?)''', row)

    conn.commit()
    conn.close()

# Usage
create_geonames_db('USZips.csv', 'US.db')

# ```

# 3. Query the database:
#    Once you have created the database, you can query it to find the nearest zip code to a given latitude and longitude. Here's a function to do that:

# ```python
def get_zipcode_geonames(latitude, longitude, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT postal_code, place_name, admin_name1,
               (latitude - ?)*(latitude - ?) + (longitude - ?)*(longitude - ?) AS distance
        FROM zipcodes
        ORDER BY distance
        LIMIT 1
    """, (latitude, latitude, longitude, longitude))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {
            'postal_code': result[0],
            'place_name': result[1],
            'state': result[2],
            'distance': result[3]
        }
    else:
        return None
df = pd.read_csv('trees.csv')
df = df.to_dict(orient='records')

for row in df: 
    print(get_zipcode_geonames(row['lat'], row['lon'], 'US.db'))
