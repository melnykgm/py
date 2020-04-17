import datetime


def get_greeting_by_name(name):
    return "Hello " + name


def main():
    print(get_steps(DICT_WITH_DESC))
    step = ask_user("Enter step")
    check_step(step)


def ask_user(ask):
    answer = raw_input(ask + ": ")
    return answer


def get_steps(steps_dict):
    lst = []
    for key in steps_dict.keys():
        lst.append(key)
    return lst


def get_date():
    today = datetime.date.today()
    return today


def get_time():
    time = datetime.datetime.now().time()
    return time


def get_info():
    info = """This is basic interactive command line application
List of supported commands: 
 1. info - prints program usage
 2. greeting - asks your name and greets you
 3. date - shows todays date
 4. time - shows actual time"""
    return info


def check_step(step):
    if "desc" in step:
        print(get_value(DICT_WITH_DESC, step.split(' ')[0]))
    elif not step in get_steps(DICT_WITH_DESC):
        print("No such step, available steps:\n {1}", get_steps(DICT_WITH_DESC))

    else:
        for key in get_steps(DICT_WITH_DESC):
            if step == key:
                function_name = get_value(DICT_WITH_FUNCT, key)
                print(function_name())
                break


def get_value(dictionary, key):
    return dictionary[key]


def get_greeting():
    name = ask_user("What is your name?")
    return get_greeting_by_name(name)


DICT_WITH_DESC = {"greeting": "return greeting base on your name",
                  "info": "printout information about application usage",
                  "date": "date",
                  "time": "time"}
DICT_WITH_FUNCT = {"greeting": get_greeting,
                   "info": get_info,
                   "date": get_date,
                   "time": get_time,
                   }

main()
