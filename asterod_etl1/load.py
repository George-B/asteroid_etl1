import psycopg2
from config import DB_CONFIG
from logger import logger

def load_data(data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        print("TOTAL ROWS TO INSERT:", len(data))

        inserted_count = 0

        for row in data:
            try:
                print("INSERTING:", row["id"])

                cur.execute("""
                    INSERT INTO asteroids 
                    (id, name, magnitude, hazardous, approach_date, velocity, miss_distance, orbiting_body)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING;
                """, (
                    row["id"],
                    row["name"],
                    row["magnitude"],
                    row["hazardous"],
                    row["approach_date"],
                    row["velocity"],
                    row["miss_distance"],
                    row["orbiting_body"]
                ))

                # 👇 IMPORTANT: check if row was actually inserted
                if cur.rowcount == 1:
                    print("INSERTED:", row["id"])
                    inserted_count += 1
                else:
                    print("SKIPPED (duplicate):", row["id"])

            except Exception as e:
                print("INSERT ERROR:", e)
                logger.error(f"Insert failed: {e}")

        print("COMMITTING...")
        conn.commit()

        print(f"TOTAL INSERTED: {inserted_count}")

        cur.close()
        conn.close()

        logger.info("Data loaded successfully")

    except Exception as e:
        print("DB CONNECTION ERROR:", e)
        logger.error(f"Database connection failed: {e}")
