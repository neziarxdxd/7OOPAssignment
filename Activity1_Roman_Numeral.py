try:
    import re
except:
    print("Check your module")
    exit()
#Re for regex to easily get the validation for the Roman numeral
roman={'I':1 ,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
class romToNum():
    def __init__ (self,h):
        try:
            pattern = '^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'      
            if re.search(pattern, h):            
                sums=0
                for i in range(len(h)):
                    if i>0 and roman[h[i]] > roman[h[i-1]]:
                        sums+=roman[h[i]]-2*roman[h[i-1]]
                    else:
                        sums+=roman[h[i]]
                print("ANSWER: {}".format(sums))
            else:
                print ('INVALID')
        except SyntaxError:
            print("There is wrong in your coding")
        except IndexError:
            print("Check your index")
        except NameError:
            print("Check your code")
        except ImportError:
            print("Check your import")
        except ModuleNotFoundError:
            print("Check your module")
        except TypeError:
            print("Check your type, it should be string")
        finally:
            print("Continue...")
while True:
    romToNum(input("Enter a roman numeral number: "))
            

