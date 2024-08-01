import os
from anki import AnkiBot

mail=os.environ["MAIL_ANKI"]
password=os.environ["PASSWORD_ANKI"]
txt_name="YOUR TXT NAME"

anki=AnkiBot(mail,password, txt_name)

anki.get_anki()

anki.adding_phrase()

