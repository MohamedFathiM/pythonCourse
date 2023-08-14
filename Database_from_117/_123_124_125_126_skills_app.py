
import sqlite3

db = sqlite3.connect('app.db')
print('Connected')
cr = db.cursor()
db.execute('Create Table if not exists skills(name text,progress integer,user_id integer)')

user_id = 1
input_message = """
What Do You Want to do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A skill
"u" => Update A skill
"q" => Quit
Choose Option :
"""


commands_list = ['s' , 'a' , 'd' , 'u' , 'q']
user_input = input(input_message).strip().lower()

if user_input not in commands_list :
    print("Command is not found")


def commit_and_close():
    db.commit()
    db.close()

def validate_skill_name(name):
    if(len(name) == 0):
         raise Exception('You Should Exist Valid Name')
    if(cr.execute(f'select count(*) from skills where name = "{name}" and user_id = "{user_id}"').fetchone()[0] != 0):
        raise Exception('Skill is already exists')


def list_skills():
    results = cr.execute('select * from skills')
    for skill in results:
        print(f"Skill is {skill[0]} => {skill[1]}%")
    commit_and_close()

def add_skill():
    sk = input('write skill name : ').strip().capitalize()
    prog = input('write skill progress: ').strip()
    validate_skill_name(sk)
    cr.execute(f'insert into skills (name,progress,user_id) values("{sk}","{prog}","{user_id}")')
    commit_and_close()

def delete_skill():
    skill_name = input("Enter Skill Name :").strip().capitalize()
    cr.execute(f'delete from skills where name = "{skill_name}" and user_id ="{user_id}"')
    commit_and_close()
    print(f"All skills with name {skill_name} are deleted when user_id is {user_id}")

def update_skill():
    old_skill_name = input("Input Old Skill Name : ").strip().capitalize()
    prog = input('write skill progress: ').strip()

    cr.execute(f'update skills set progress = "{prog}" where name = "{old_skill_name}" and user_id = "{user_id}"')
    commit_and_close()

def close_app():
    print("Thanks For Joining Us !")
    commit_and_close()


if user_input == 's' :
    list_skills()
elif user_input == 'a' :
    add_skill()
elif user_input == 'd' :
    delete_skill()
elif user_input == 'u' :
    update_skill()
else:
    close_app()
