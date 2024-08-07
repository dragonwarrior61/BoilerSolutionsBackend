import logging
import requests
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import psycopg2
from app.config import settings
from psycopg2 import sql

async def insert_postal_code_into_db(group_str, postal_code_str_array):
    try:
        conn = psycopg2.connect(
            dbname=settings.DB_NAME,
            user=settings.DB_USERNAME,
            password=settings.DB_PASSWORD,  # Corrected spelling from DB_PASSOWRD to DB_PASSWORD
            host=settings.DB_URL,
            port=settings.DB_PORT
        )
        conn.set_client_encoding('UTF8')
        cursor = conn.cursor()

        insert_query = sql.SQL("""
            INSERT INTO {} (
                group_number,
                detail_area,
                postal_code      
            ) VALUES (
                %s, %s, %s
            )
        """).format(sql.Identifier("postal_codes"))

        group_number = group_str

        for i in range(len(postal_code_str_array)):
            if group_str == "Group A":
                detail_area = f"Leicester Area {chr(65 + i)}"
            else:
                detail_area = f"Batley Area {chr(65 + i)}"

            postal_code_str = postal_code_str_array[i]
            postal_code_array = [item.strip() for item in postal_code_str.split(',')]
            for code in postal_code_array:
                postal_code = code

                values = (
                    group_number,
                    detail_area,
                    postal_code
                )

                cursor.execute(insert_query, values)
                conn.commit()

        print("Successfully inserted postal code")

        cursor.close()
        conn.close()
    except Exception as inner_e:
        print(f"Error inserting postal_code: {inner_e}")

async def refresh_postal_code():

    Group_A = ["CV13, LE1, LE10, LE11, LE12, LE14, LE16, LE17, LE18, LE19, LE2, LE21, LE3, LE4, LE41, LE5, LE55, LE6, LE67, LE7, LE8, LE87, LE9, LE95",
               "CV10, CV11, CV12, CV23, CV7, CV9, DE12, LE13, LE15, LE65, LE94, NG12, NN6",
               "CV2, CV21, CV22, CV3, CV5, CV6, DE7, DE72, DE73, DE74, NG11, NN14",
               "B46, B76, B77, B78, B79, CV1, CV32, CV33, CV4, CV47, CV8, DE1, DE11, DE13, DE14, DE15, DE2, DE21, DE22, DE23, DE24, DE3, DE6, DE65, DE99, LE95, NG1, NG10, NG11, NG12, NG13, NG14, NG2, NG20, NG3, NG32, NG33, NG4, NG5, NG7, NG8, NG80, NG9, NG90, NN11, NN14, NN15, NN16, NN17, NN18, NN2, NN3, NN6, NN7, PE8, PE9, WS13",
               "B23, B24, B25, B26, B33, B34, B35, B36, B37, B4, B40, B42, B6, B72, B73, B74, B75, B8, B9, B91, B92, B93, B94, CV31, CV34, CV35, DE5, DE56, DE75, NG1, NG10, NG13, NG14, NG15, NG16, NG17, NG2, NG20, NG23, NG25, NG3, NG31, NG32, NG33, NG4, NG5, NG6, NG7, NG8, NG80, NG9, NG90, NN1, NN11, NN15, NN16, NN17, NN18, NN2, NN29, NN3, NN4, NN5, NN7, NN8, NN9, NN99, PE10, PE8, PE9, WS13, WS14, WS7 "]

    Group_B = ["BD1, BD11, BD12, BD19, BD4, HD5, HD6, LS1, LS10, LS11, LS12, LS25, LS27, LS28, LS88, LS98, WF1, WF12, WF13, WF14, WF15, WF16, WF17, WF2, WF3, WF4, WF5",
               "BD10, BD13, BD14, BD15, BD16, BD17, BD18, BD2, BD3, BD5, BD6, BD7, BD8, BD9, BD97, BD98, BD99, HD1, HD2, HD3, HD4, HD7, HD8, HD9, HX1, HX2, HX3, HX4, HX5, HX6, LS13, LS14, LS15, LS16, LS17, LS18, LS19, LS2, LS26, LS3, LS4, LS5, LS6, LS7, LS8, LS9, LS99, S75, WF10, WF6, WF7, WF90",
               "BD20, BD21, BD22, HD5, HD6, HG3, HX7, LS20, LS21, LS22, LS23, LS24, S30, S35, S36, S70, S71, S72, S73, WF11, WF8, WF9, WF90",
               "BD19, BD23, DN14, DN5, DN6, , HG1, HG2, , HG5, LS29, OL14, OL15, OL16, OL3, S1, S6, S61, S62, S63, S64, S74, S75, S95, S97, SK13, SK14, YO23, YO5, YO8"]

    await insert_postal_code_into_db("Group A", Group_A)
    await insert_postal_code_into_db("Group B", Group_B)