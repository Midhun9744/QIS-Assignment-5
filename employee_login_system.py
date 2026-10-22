import logging
logging.basicConfig(level=logging.DEBUG)

class user(Exception):
    pass
class pswd(Exception):
    pass
dict={
    'user@1':'@1234',
    'user@2':'@12345'
}
for i  in range(3):
        try:
            logging.info('enter the correct details...')
            username=input('enter the username ')
            if username not in dict:
                # logging.error('a')
                raise user('user name not found....')
            
            password=input('enter the password ')
            if password !=dict[username]:
                logging.error('password error ')
                raise pswd('password incoorect ')
            elif dict[username]==password:
                print(' login succesfull...')
                break
        except user as e:
            print('error ',e)
            continue
        except pswd as e:
            print('error ',e)
            continue
        finally:
            print('Thank You..')
else:
    print('login attempt exceded')
