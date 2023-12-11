import pywhatkit
from datetime import timedelta, date, time
import pyautogui as pg

def send_registration_link():
    # The registration link will be sent on Thursday 10:00 AM once a week
    # Session date will be 2 days after the registration link is sent to the WhatsApp group
    today = date.today()
    session_date = today + timedelta(days=2)

    # Naming of the day, etc., Monday, Wednesday
    name_of_day = session_date.strftime("%A")

    # Format date to dd/mm/yyyy, etc., 17/05/2023
    formatted_date = session_date.strftime('%d-%m-%Y')

    # Registration link message content to be sent on Whatsapp
    register_link_msg = (
        'Driving Range Session ⛳⛳ \n\nDate => ' + name_of_day + ' | ' + formatted_date + '\nTimings => 2pm to 4pm \nVenue => X Park PJ South (Taman Medan)'
            '\nRegistration is based on a first-come, first-served basis‼️'
            '\nThis session has a limit of 20 people\n'
            '\nPLAYER WITH GOLF SET (limit 10)*'
            '\nStudents that have their own golf set and know the basics of golf'
            '\n- Register using this link'
            '\nhttps://forms.gle/TzZ3dKRyaygLm4HH6\n'
            '\nBeginner player (limit 10)'
            '\nStudent that doesn’t have their own golf set and doesn’t know the basics of golf'
            '\n- Register using this link'
            '\nhttps://forms.gle/wurxVXMhhWQwfnu69\n'
            '\nPlease DO NOT ATTEND the session if you did not fill in the Google form else we will charge RM 5 penalty fee on top of the session fee.\n'
            '\nLocation of the Venue:'
            '\nhttps://goo.gl/maps/gJF5VYCojatNEbKRA\n'
            '\nNote: In case of any queries or removal of your name you are required to PM me (Bai Wei 016-575-7315). Removal of name '
            'must be at most 24 hours before the session or else we won’t be able to refund‼️'
    )
    # Whatsapp Group Invitation Link ID to enter group
    wa_group_id = "KKVOgfy0IdNJQRTz0zKpFE"
    # Schedule Time (Hour) of the day eg. 0-23. 00-09 not acceptable only 0-9 is accepted
    wa_time_hour = 10
    # Schedule Time (Min) of the day eg. 0-59. 00-09 not acceptable only 0-9 is accepted
    wa_time_min = 0

    pywhatkit.sendwhatmsg_to_group(wa_group_id, register_link_msg, wa_time_hour, wa_time_min)

    # Waiting time has been added to accommodate delays when opening Whatsapp Web on the browser
    # Disclaimer: if no waiting time is added the script will paste the message while the Whatsapp Web is loading resulting in it not being able load message into chat.
    time.sleep(15)

    # I included pyautogui library due to some reasons in which there are bugs in pywhatkit library when sending messages to groups.
    # Disclaimer: The message is not able to paste at the correct location in the chatbox of Whatsapp Web, therefore I tweaked it to paste at the correct location.
    # You have to tweak the location according your browser view of chatbox in Whatsapp Web. 
    # You can use this website to check cursor location: http://www.brenz.net/snippets/xy.asp

    # Cursor Location moved to chat box, then mouse will click once
    pg.moveTo(1000, 840)
    pg.click()
    # Press Enter after 60 seconds to allow time for message to be loaded into chatbox
    time.sleep(60)
    pg.press('enter') 

# Call the function to execute the task
send_registration_link()
