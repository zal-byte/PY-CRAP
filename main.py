from lib import scrap


def preload():
  #Scrapping <a> tag from website
  crap = scrap.Crap()
  var = crap.scrap();
  for i in var:
      print( i.get("href") )
  

if __name__ == "__main__":
    try:
        preload()
    except KeyboardInterrupt:
        print("[ ! ] Interrupted By CTRL + C")
    except EOFError:
        print("[ ! ] EOFError ")
    except Exception as e:
        print("[ ! ] An exception has occured ")
        print("[ ! ] " + str(e))