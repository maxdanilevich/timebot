from datetime import date
import sqlite3


def day_of_week(date_list: list) -> str:
    date_ = date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    short = date_.ctime()[:3]

    with sqlite3.connect('sqlite_week_day.db') as con:
        query = 'SELECT full_day FROM week_day WHERE short_day = ?'
        cursor = con.cursor()
        cursor.execute(query, (short,))
        week_day = cursor.fetchone()[0]
        cursor.close()
    return week_day