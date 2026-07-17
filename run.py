# --------------     Produção    --------------

from .backend.app import app

# -------------- Desenvolvimento  --------------
#from backend.app import app

 

if __name__ == "__main__":
    
# --------------      Produção    --------------

    app.run(debug=True)


# -------------- Desenvolvimento  --------------
    #app.run(host="127.0.0.1", port=5000, debug=True) 
        