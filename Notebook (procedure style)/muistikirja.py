import pickle
import time

user_list = []
filename = "muistio.dat"

def main():

    initialize(filename)

    while True:
        print("(1) Lue muistikirjaa")
        print("(2) Lisää merkintä")
        print("(3) Muokkaa merkintää")
        print("(4) Poista merkintä")
        print("(5) Tallenna ja lopeta")
        print()

        user_input = input("Mitä haluat tehdä?: ")

        if user_input == '1':
            get_all_notices()
        elif user_input == '2':
            put_notice_in_list()
        elif user_input == '3':
            print_length_of_list()
            index_for_changing = input("Mitä niistä muutetaan?: ")
            change_list(index_for_changing)
        elif user_input == '4':
            print_length_of_list()
            index_for_deleting = input("Mitä niistä poistetaan?: ")
            delete_notice_from_list(index_for_deleting)
        elif user_input == '5':
            print("Lopetetaan.")
            dump_user_data_to_file()
            break
        else:
            print("Virhellinen valitus")


def initialize(filename):
    try:
        file = open(filename, 'rb')
        global user_list
        user_list = pickle.load(file)
        file.close()
    except Exception:
        print("Virhe tiedostossa, luodaan uusi muistio.dat.")
        file = open(filename, "w")
        file.write("")
        file.close()

def put_notice_in_list():
    notice = input("Kirjoita uusi merkintä: ")
    notice = notice + get_current_time()
    user_list.append(notice)

def delete_notice_from_list(index_for_deleting):
    try:
        index_for_deleting = int(index_for_deleting) - 1
        notice = user_list.pop(index_for_deleting)
        print("Poistettiin merkintä", notice)
    except Exception:
        print("Virhellinen arvo")

def print_length_of_list():
    print("Listalla on", len(user_list), "merkintää.")

def change_list(index_for_changing):
    try:
        index_for_changing = int(index_for_changing) - 1
        current_notice = user_list.pop(index_for_changing)
        print(current_notice)
        new_notice = input("Anna uusi teksti: ")
        new_notice += get_current_time()
        user_list.insert(index_for_changing, new_notice)
    except Exception:
        print("Virhellinen arvo")

def get_current_time():
    notice_time = time.strftime("%X %x")
    delimeter = ":::"
    return delimeter + notice_time

def get_all_notices():
    for i in user_list:
        print(i)

def dump_user_data_to_file():
    file = open(filename, 'wb')
    pickle.dump(user_list, file)
    file.close()

if __name__ == "__main__":
    main()