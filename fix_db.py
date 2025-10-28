#!/usr/bin/env python
"""
Fix missing meta_description column in home_homepage table
"""
import sqlite3
import os

def fix_database():
    db_path = 'db.sqlite3'
    
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if column exists
        cursor.execute("PRAGMA table_info(home_homepage)")
        columns = [row[1] for row in cursor.fetchall()]
        
        if 'meta_description' not in columns:
            print("Adding meta_description column...")
            cursor.execute(
                "ALTER TABLE home_homepage ADD COLUMN meta_description VARCHAR(160) DEFAULT ''"
            )
            conn.commit()
            print("✅ Column added successfully!")
            return True
        else:
            print("✅ Column already exists!")
            return True
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        conn.close()

if __name__ == '__main__':
    fix_database()

