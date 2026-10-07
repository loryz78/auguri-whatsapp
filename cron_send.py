from app import init_db, process_birthdays, setting

if __name__ == '__main__':
    init_db()
    if setting('auto_send','1') == '1':
        for name, status in process_birthdays(force=False):
            print(f'{name}: {status}')
    else:
        print('Invio automatico disattivato.')
