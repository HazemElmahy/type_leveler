import os
import sys
import sqlite3
import subprocess

OPERATION=sys.argv[1]

try: 
    connection = sqlite3.connect("/home/hazem/scripts/type.sqlite3")
    cursor = connection.cursor()
    print("Connected To SQLite")

    cursor.execute("SELECT * FROM speed;")
    first_score=cursor.fetchall()[0]
    SCORE=first_score[0]
    STATE=first_score[1]
    cursor.execute("SELECT * FROM accuracy;")
    acc=cursor.fetchall()[0]
    ACC_SCORE=acc[0]
    ACC_STATE=acc[1]
except sqlite3.Error as error:
    subprocess.Popen(['notify-send', f'error {error}'])
except Exception as e:
    subprocess.Popen(['notify-send', f'error {e}'])
    


def update():
    os.system(f'notify-send -r 3 "{SCORE}, {STATE}"')
    cursor.execute(f"UPDATE speed SET score={SCORE}, state={STATE};")
    connection.commit()
    cursor.close()

def acc_update():
    try:
        os.system(f'notify-send -r 3 "{round(ACC_SCORE, 1)}, {ACC_STATE}"')
        cursor.execute(f"UPDATE accuracy SET score={round(ACC_SCORE, 1)}, state={ACC_STATE};")
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        subprocess.Popen(['notify-send', f'error {error}'])
    except Exception as e:
        os.system(f'notify-send -r 3 "Error {e}"')



if OPERATION=="+":
    os.system('notify-send -r 2 -t 1000 "✓ "')
    if STATE < 0:
        STATE = 0
    elif STATE < 9:
        STATE+=1
    else:
        STATE=0
        SCORE+=1

elif OPERATION=="-":
    os.system('notify-send -r 2 -t 1000 "✗"')
    if STATE > 0:
        STATE=0

    else:
        STATE -=1
    
    if STATE < -2:
        SCORE -=1
        STATE = 0

if OPERATION=="A":
    os.system('notify-send -r 2 -t 1000 "✓ "')
    if ACC_STATE < 0:
        ACC_STATE = 0
    elif ACC_SCORE >= 100 or ACC_STATE < 9:
        ACC_STATE+=1
    else:
        ACC_STATE=0
        ACC_SCORE+= 0.1
    acc_update()

elif OPERATION=="D":
    os.system('notify-send -r 2 -t 1000 "✗"')
    if ACC_STATE > 0:
        ACC_STATE=0

    else:
        ACC_STATE -= 1
    
    if ACC_STATE < -2:
        ACC_SCORE -= 0.1
        ACC_STATE = 0
    acc_update()

elif OPERATION == "=":
    os.system(f'notify-send -r 3 "{SCORE}"')
else:
    update()



if connection:
    connection.close()
    print("connection closed")

