import MySQLdb
import os
import smtplib
from termcolor import colored, cprint
conn=MySQLdb.connect(host="localhost",user="root",passwd="270777",db="trasporti")
cursore=conn.cursor()

def googlesearch():
    import webbrowser
    import os
    usc = ''
    while usc != ('S') and usc != ('s'):
        os.system('cls')
        print'******************'
        print'Google Maps Search'
        print'******************'
        print('Ricerca itinerario fino a 5 destinazioni diverse')
        print''
        print''
        scelta = input('N.R Tappe Itinerario -  Scegli da 1 a 5: ')
        if scelta == 5:
            print''
            partenza = raw_input('Inserire Partenza:')
            print''
            destinazione1 = raw_input('Inserire Destinazione1:')
            print''
            destinazione2 = raw_input('Inserire Destinazione2:')
            print''
            destinazione3 = raw_input('Inserire Destinazione3:')
            print''
            destinazione4 = raw_input('Inserire Destinazione4:')
            webbrowser.open('https://www.google.it/maps/dir/' + partenza + '/' + destinazione1 + '/' + destinazione2 + '/' + destinazione3 + '/' + destinazione4)
        elif scelta == 1:
            print''
            partenza = raw_input('Inserire Partenza:')
            print''
            webbrowser.open('https://www.google.it/maps/place/' + partenza)
        elif scelta == 2:
            print''
            partenza = raw_input('Inserire Partenza:')
            print''
            destinazione1 = raw_input('Inserire Destinazione1:')
            webbrowser.open('https://www.google.it/maps/dir/' + partenza + '/' + destinazione1)
        elif scelta == 3:
            print''
            partenza = raw_input('Inserire Partenza:')
            print''
            destinazione1 = raw_input('Inserire Destinazione1:')
            print''
            destinazione2 = raw_input('Inserire Destinazione2:')
            webbrowser.open('https://www.google.it/maps/dir/' + partenza + '/' + destinazione1 + '/' + destinazione2)
        elif scelta == 4:
            print''
            partenza = raw_input('Inserire Partenza:')
            print''
            destinazione1 = raw_input('Inserire Destinazione1:')
            print''
            destinazione2 = raw_input('Inserire Destinazione2:')
            print''
            destinazione3 = raw_input('Inserire Destinazione3:')
            webbrowser.open('https://www.google.it/maps/dir/' + partenza + '/' + destinazione1 + '/' + destinazione2 + '/' + destinazione3)
        print""
        usc = raw_input('Vuoi uscire da GOOGLE SEARCH E TORNARE A MAIN MENU?(s/n)')

def ricerche():
    usc = ''
    while usc != ('S') and usc != ('s'):
        os.system('cls')
        print''
        print'''
         *****************************************************
         *                                                   *
         *               RICERCA TRASPORTI                   *
         *                                                   *
         *****************************************************

        MENU

        1 - Ricerca per Vettore
        2 - Ricerca per Vettore e Data
        3 - Ricerca per Cliente
        4 - Ricerca per Cliente e Data
        5 - Ricerca per Regione
        6 - Ricerca per Regione e Data
        7 - Ricerca per Citta'
        8 - Ricerca per Citta' e Data
        9 - Trasporti per Data
        10- Trasporti fatturati per periodo
        11- Visualizza Clienti con Trasporto in Fattura
        12- Ricerca per Vettore e Regione
        13- Ricerca per Vettore e Citta'
        14- Ricerca andata e Ritorno Vettore per Regione
        15- Ricerca andata e Ritorno per Regione
        16- Ricerca per numero Fattura di Vendita
        17- Riepilogo Totale Trasporti per Vettore
        18- Riepilogo A/R per Vettore
        19- Riepilogo solo Ritorno per Vettore
      '''
        def ar():
            print''
            print'***RIEPILOGO Andata/Ritorno PER DATA***'
            data1 = input("Data iniziale: ")
            data2 = input("Data   finale: ")
            r = ("select count(*),vettore,sum(prezzo) from trasportatori where andataritorno='s' and data >=%d and data <=%d group by vettore " % (data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '=' * 30
                print'Numero Viaggi:',colored(x[0],'cyan',attrs=['bold'])
                print'Vettore:', colored(x[1],'green',attrs=['bold'])
                print'Costo:',colored(x[2],'red',attrs=['bold'])
                print''

        def riepilogo():
            print''
            print'***RIEPILOGO TRASPORTI PER DATA***'
            data1 = input("Data iniziale: ")
            data2 = input("Data   finale: ")
            r = (" select count(*), vettore,sum(prezzo),sum(totale_fatturato) from trasportatori where data >=%d and data<=%d group by vettore order by vettore asc" % (data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '=' * 30
                print'Nr. Viaggi:',x[0]
                print'Vettore:',colored(x[1],'yellow',attrs=['bold'])
                print'Totale Costo:',colored(x[2],'red',attrs=['bold'])
                print'Fatturato Consegnato:',colored(x[3],'green',attrs=['bold'])
                print'Incidenza:',round(x[2]/x[3]*100),'%'
                print''
        def ritorno():
            print''
            print'***RIEPILOGO RITORNO PER DATA***'
            data1 = input("Data iniziale: ")
            data2 = input("Data   finale: ")
            r = ( "select count(*),vettore,sum(prezzo),data from trasportatori where andataritorno='r' and data >=%d and data <=%d group by vettore " % (data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '=' * 30
                print'Numero Viaggi:',colored(x[0],'cyan',attrs=['bold'])
                print'Vettore:',colored(x[1],'green',attrs=['bold'])
                print'Costo:', colored(x[2],'red',attrs=['bold'])
                print'Data:', colored(x[3],'yellow',attrs=['bold'])
                print''


        def ricercavettore():
            print''
            print'***RICERCA TRASPORTATORE***'
            cognome = raw_input("Trasportatore da ricercare: ")
            r = """select*from trasportatori where vettore like'""" + "%" + cognome + "%'"
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]

        def ricercacliente():
            print''
            print'***RICERCA CLIENTE***'
            nome = raw_input("Cliente da ricercare: ")
            r = """select*from trasportatori where clienti like'""" + "%" + nome + "%'"
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def ricercaregione():
            print''
            regione = raw_input("Regione da ricercare: ")
            r = """select*from trasportatori where regione like'""" + "%" + regione + "%'"
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def ricercacitta():
            print''
            print'***RICERCA DESTINAZIONE***'
            citta = raw_input("Citta' da ricercare: ")
            r = """select*from trasportatori where destinazione like'""" + "%" + citta + "%'"
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def ricercavettoredata():
            print''
            print'***RICERCA PER VETTORE E PERIODO***'
            print''
            cognome = raw_input("Vettore:")
            data1 = input("Data iniziale: ")
            data2 = input("Data finale: ")
            r = ("select *from trasportatori where vettore='%s'and data>= %d and data <= %d " % (cognome, data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def ricercaclientedata():
            print''
            print'***RICERCA PER CLIENTE E DATA***'
            print''
            cognome = raw_input("Cliente:")
            data1 = input("Data iniziale: ")
            data2 = input("Data   finale: ")
            r = ("select *from trasportatori where clienti='%s'and data>= %d and data <= %d " % (cognome, data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def trasportidata():
            print''
            print'***RICERCA TRASPORTI PER DATA***'
            print''
            data1 = input("Data iniziale: ")
            data2 = input("Data   finale: ")
            r = ("select *from trasportatori where  data>= %d and data <= %d order by data" % (data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def regionedata():
            print''
            print'***RICERCA REGIONE PER DATA***'
            print''
            regione=raw_input("Inserire regione:")
            data1 = input("Data iniziale: ")
            data2 = input("Data   finale: ")
            r = ("select *from trasportatori where regione ='%s'and data>= %d and data <= %d order by data" % (regione,data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def esci():
            esci=raw_input("Premi un tasto uscire")

        def trasportofatturato():
            print''
            print'***CALCOLA COSTO TRASPORTI IN FATTURA PER PERIODO***'
            print''
            data1 = input("Data iniziale: ")
            data2 = input("Data finale  : ")
            r = ("select sum(trasporto_fatturato)from trasportatori where  data>= %d and data <= %d " % ( data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print'***************************************'
                print 'Totale Trasporto Fatturato :', x[0]
                print'***************************************'
            clienti=raw_input('Vuoi visualizzare i Clienti Fatturati? S/N:')
            if clienti== 's'or 'S':
                c = ("select*from trasportatori where trasporto_fatturato>0 and data>= %d and data <= %d " % (data1, data2))
                cursore.execute(c)
                totale = cursore.fetchall()
                for y in totale:
                    print '=' * 70
                    print'Data:', y[1]
                    print'Vettore:', y[2]
                    print'Clienti:', y[3]
                    print'Destinazione:', y[4]
                    print'Regione:', y[5]
                    print'Prezzo:', y[6]
                    print'Tipo:', y[7]
                    print'A/R:', y[8]
                    print'Fatture:', y[9]
                    print'Trasporto in Fattura:', y[10]
                    print'Totale Fatturato:', y[11]
                    print''
            if clienti == 'N'or 'n':
                print'ciao'


        def prezzofatturato():
            print''
            print'***RICERCA TRASPORTI FATTURATI PER DATA***'
            print''
            data1 = input("Data iniziale: ")
            data2 = input("Data   finale: ")
            r = ("select *from trasportatori where trasporto_fatturato>0 and data>= %d and data <= %d order by data" % (data1, data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def cittadata():
            print''
            print'***RICERCA CITTA DURANTE PERIODO***'
            print''
            cognome = raw_input("Citta':")
            data1 = input("Data iniziale: ")
            data2 = input("Data finale: ")
            r = """select*from trasportatori where destinazione like'""" + "%" + cognome + "%'and data>= %d and data <= %d" % (cognome, data1, data2)
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '=' * 70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:', x[10]
                print'Totale Fatturato:', x[11]
                print''

        def vettoreregione():
            print''
            print'***RICERCA REGIONE PER VETTORE***'
            print''
            regione = raw_input("Inserire regione:")
            vettore= raw_input("Vettore:")
            r = ("select *from trasportatori where regione ='%s'and vettore='%s'order by data")% (regione, vettore)
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '=' * 70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:', x[10]
                print'Totale Fatturato:', x[11]
                print''

        def vettorecitta():
            print''
            print'***RICERCA CITTA E VETTORE***'
            citta = raw_input("Citta' da ricercare: ")
            vettore = raw_input("Vettore:")
            r = ("select *from trasportatori where destinazione ='%s'and vettore='%s'order by data")% (citta, vettore)
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def andataritorno():
            print''
            print'***RICERCA VETTORE A/R REGIONE***'
            citta = raw_input("Regione: ")
            vettore = raw_input("Vettore: ")
            ar=raw_input("A/R:")
            r = ("select *from trasportatori where regione ='%s'and vettore='%s'and andataritorno='%s'order by data")% (citta, vettore,ar)
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def andataritorno2():
            print''
            print'***RICERCA VETTORE A/R REGIONE***'
            citta = raw_input("Regione: ")
            ar=raw_input("A/R:")
            r = ("select *from trasportatori where regione ='%s'and andataritorno='%s'order by data")% (citta,ar)
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '='*70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:',x[10]
                print'Totale Fatturato:',x[11]
                print''

        def ricercafattura():
            print'''
                  ================================
                  ***RICERCA PER NUMERO FATTURA***
                  ================================
            '''
            fattura = raw_input("Numero Fattura di Vendita: ")
            r = """select*from trasportatori where fatture like'""" + "%" + fattura + "%'"
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print '=' * 70
                print'Data:', x[1]
                print'Vettore:', x[2]
                print'Clienti:', x[3]
                print'Destinazione:', x[4]
                print'Regione:', x[5]
                print'Prezzo:', x[6]
                print'Tipo:', x[7]
                print'A/R:', x[8]
                print'Fatture:', x[9]
                print'Trasporto in Fattura:', x[10]
                print'Totale Fatturato:', x[11]
                print''

        operazione = input("Inserisci il tipo di operazione da effettuare: ")
        if operazione==1:
            ricercavettore()
        if operazione==2:
            ricercavettoredata()
        if operazione==3:
            ricercacliente()
        if operazione==4:
            ricercaclientedata()
        if operazione==5:
            ricercaregione()
        if operazione==6:
            regionedata()
        if operazione==7:
            ricercacitta()
        if operazione==8:
            cittadata()
        if operazione==9:
            trasportidata()
        if operazione==10:
            trasportofatturato()
        if operazione==11:
            prezzofatturato()
        if operazione==12:
            vettoreregione()
        if operazione==13:
            vettorecitta()
        if operazione==14:
            andataritorno()
        if operazione==15:
            andataritorno2()
        if operazione==16:
            ricercafattura()
        if operazione==17:
            riepilogo()
        if operazione==18:
            ar()
        if operazione==19:
            ritorno()


        usc=raw_input("Vuoi uscire da RICERCA TRASPORTI e tornare al MAIN MENU? (s/n):")

def visualizza():
    cursore.execute("select*from trasportatori")
    riga=cursore.fetchall()
    for x in riga:
        print''
        print '='*70
        print'Id:',x[0]
        print'Data:',x[1]
        print'Vettore:',colored(x[2],'yellow', attrs=['bold'])
        print'Clienti:',colored(x[3], 'magenta', attrs=['bold'])
        print'Destinazione:',x[4]
        print'Regione:',x[5]
        print'Prezzo:',colored(x[6],'red', attrs=['bold'])
        print'Tipo:',x[7]
        print'A/R:',x[8]
        print'Fatture:', x[9]
        print'Trasporto Fatturato:',x[10]
        print'Totale Fatturato:',colored(x[11],'green', attrs=['bold'])

def ricercavettore():
    print''
    print'***RICERCA TRASPORTATORE***'
    cognome=raw_input("Trasportatore da ricercare: ")
    r="""select*from trasportatori where vettore like'"""+"%"+cognome+"%'"
    cursore.execute(r)
    risultato=cursore.fetchall()
    for x in risultato:
        print''
        print '='*70
        print'Data:', x[1]
        print'Vettore:', x[2]
        print'Clienti:', x[3]
        print'Destinazione:', x[4]
        print'Regione:', x[5]
        print'Prezzo:', x[6]
        print'Tipo:', x[7]
        print'A/R:', x[8]

def inserimento():
    print''
    print'***REGISTRA TRASPORTO***'
    print''
    d=input("Numero Trasporto: ")
    i=input('Data:')
    a=raw_input("Vettore: ")
    b=raw_input("Clienti: ")
    c=raw_input("Destinazione:")
    e=raw_input('Regione: ')
    f=float(input('Prezzo:'))
    g=raw_input('Tipo..es. Bilico intero o n.cav:')
    h=raw_input('A/R:')
    l=raw_input('Fatture:')
    m=float(input('Trasporto Fatturato:'))
    n=float(input('Totale Fatturato:'))
    print''
    print colored('***GESTIONE PARZIALI***','yellow',attrs=['bold'])
    print''
    o=raw_input("Trasporto Parziale? (S/n):")
    p=float(input("Quota Prezzo:"))
    q=raw_input("Motivo Parziale:")
    x="insert into trasportatori values(%d,%d,'%s','%s','%s','%s',%d,'%s','%s','%s',%d,%d,'%s',%d,'%s')"%(d,i,a,b,c,e,f,g,h,l,m,n,o,p,q)#Inserimento istruzioni Sql#
    cursore.execute(x)#esecuzione istruzioni sql#
    conn.commit()#scrittura delle istruzioni nel database#
    print'''
    ***OPERAZIONE EFFETTUATA***
    '''

def pesovetri():
    usc = ''
    while usc != 's' and usc != 'S':
        os.system('cls')
        print'                      **********************'
        print '                     * Calcolo Peso Vetro *'
        print'                      **********************'
        print''
        try:
            vetro1 = input('Spessore vetro 1: ')
            vetro2 = input('Spessore vetro 2: ')
            vetro3 = input('Spessore vetro 3: ')
            print'----------------------------'
            base = input('Base Vetro in cm.: ')
            altezza = input('Altezza Vetro in cm.: ')
            pezzi = input('Inserire numero Pezzi:')
            print'----------------------------'
        except:
            print'ATTENZIONE: Inserire tutti i dati richiesti'
        metriq = base * altezza
        mq = input('Mq totali dell''Ordine: ')
        totvetri = vetro1 + vetro2 + vetro3
        pesovetri = metriq * totvetri * pezzi * 2.5
        mq2 = mq * totvetri * 2.5
        if mq > 0:
            print''
            print'*********************************'
            print'Totale Mq. ordine Kg.=', mq2
            print'*********************************'
        else:
            print''
            print'*********************************'
            print'Totale Mq. ordine Kg.=', pesovetri
            print'*********************************'
        print''
        usc = raw_input('Vuoi uscire da peso vetri? (s/n)')

def costotrasporto():
    print''
    print '***CALCOLA COSTO TRASPORTI PER VETTORE***'
    print''
    cognome = raw_input("Vettore:")
    data1 = input("Data iniziale: ")
    data2 = input("Data   finale: ")
    r = ("select sum(prezzo)from trasportatori where vettore ='%s'and data>= %d and data <= %d " % (cognome, data1, data2))
    cursore.execute(r)
    risultato = cursore.fetchall()
    for x in risultato:
        print''
        print'**************************'
        print 'Costo Trasporto :', colored(x[0],'yellow', attrs=['bold'])
        print'**************************'
    print''

    print'***FATTURATO TRASPORTATO PER VETTORE***'
    print''
    c = ("select sum(totale_fatturato)from trasportatori where vettore ='%s'and data>= %d and data <= %d " % (cognome, data1, data2))
    cursore.execute(c)
    risultato = cursore.fetchall()
    for y in risultato:
        print''
        print'*********************************'
        print 'Fatturato Trasportato :',  colored(y[0],'magenta', attrs=['bold'])
        print'*********************************'

    incidenza1= (x[0]/y[0])
    print''
    print 'Totale Incidenza Costo Trasporto:', round(incidenza1 * 100), '%'

def costoperiodo():
    print''
    print'***CALCOLA COSTO TRASPORTI PER PERIODO***'
    print''
    data1 = input("Data iniziale: ")
    data2 = input("Data   finale: ")
    r = ("select sum(prezzo)from trasportatori where  data>= %d and data <= %d " % ( data1, data2))
    cursore.execute(r)
    risultato = cursore.fetchall()
    for x in risultato:
        print''
        print'**************************'
        print 'Totale Periodo :', x[0]
        print'**************************'

def gestionecasse():

    def vedi():
        cursore.execute("select*from casse")
        riga = cursore.fetchall()
        for x in riga:
            print'='*50
            print'Commessa:', x[0]
            print'Riferimento:', x[1]
            print'Data Arrivo:', x[2]
            print'Pezzi:', x[3]
            print'Lunghezza:', x[4]
            print'Larghezza:', x[5]
            print'Altezza:', x[6]
            print'Bolla n.:', x[7]
            print'Uscita Cassa:', x[8]
            print''
    def vedimagazzino():
        cursore.execute("select*from casse where Uscita_cassa is NULL or Uscita_cassa=0;")
        riga = cursore.fetchall()
        for x in riga:
            print'='*50
            print'Commessa:',colored(x[0],'red',attrs=['bold'])
            print'Riferimento:',colored(x[1],'yellow',attrs=['bold'])
            print'Data Arrivo:',colored(x[2],'green',attrs=['bold'])
            print'Pezzi:',colored(x[3],'cyan',attrs=['bold'])
            print'Uscita Cassa:', x[8]
            print''

    def riepilogo():
        cursore.execute("select count(*),riferimento,commessa from casse where Uscita_cassa=0 group by riferimento")
        riga = cursore.fetchall()
        for x in riga:
            print'='*50
            print'Pezzi:',colored(x[0],'red',attrs=['bold'])
            print'Riferimento:',colored(x[1],'yellow',attrs=['bold'])
            print'Commessa:',colored(x[2],'green',attrs=['bold'])
            print''

    def ricercariferimento():
        print''
        print'***RICERCA RIFERIMENTO***'
        cognome = raw_input("Riferimento da ricercare: ")
        r = """select*from casse where riferimento like'""" + "%" + cognome + "%'"
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Commessa:', x[0]
            print'Riferimento:', x[1]
            print'Data Arrivo:', x[2]
            print'Pezzi:', x[3]
            print'Lunghezza:', x[4]
            print'Larghezza:', x[5]
            print'Altezza:', x[6]
            print'Uscita Cassa:', x[8]
            print''
    def ricercacommessa():
        print'***RICERCA RIFERIMENTO***'
        cognome = str(input("Riferimento da ricercare: "))
        r = """select*from casse where commessa like'""" + "%" + cognome + "%'"
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Commessa:', x[0]
            print'Riferimento:', x[1]
            print'Data Arrivo:', x[2]
            print'Pezzi:', x[3]
            print'Lunghezza:', x[4]
            print'Larghezza:', x[5]
            print'Altezza:', x[6]
            print'Bolla n.:', x[7]
            print'Uscita Cassa:', x[8]
            print''

    def inserisci():
        print''
        print'***REGISTRA CASSE***'
        print''
        d = input("Commessa: ")
        i = raw_input('Riferimento:')
        a = input("Data Arrivo: ")
        b = input("Pezzi: ")
        c = input("Lunghezza:")
        e = input('Larghezza: ')
        f = input('Altezza:')
        g = input('Bolla n.:')
        h = input('Uscita Cassa:')
        x = "insert into casse values(%d,'%s',%d,%d,%d,%d,%d,%d,%d)" % (d, i, a, b, c, e, f, g, h)  # Inserimento istruzioni Sql#
        cursore.execute(x)  # esecuzione istruzioni sql#
        conn.commit()  # scrittura delle istruzioni nel database#
        print ""
        print"***REGISTRAZIONE EFFETTUATA***"
        print""

    def uscitacasse():
        print''
        print'***USCITA CASSE***'
        print''
        d = input("Commessa: ")
        r =("select*from casse where commessa=%d") %(d)
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Commessa:', x[0]
            print'Riferimento:', x[1]
            print'Data Arrivo:', x[2]
            print'Pezzi:', x[3]
            print'Lunghezza:', x[4]
            print'Larghezza:', x[5]
            print'Altezza:', x[6]
            print'Bolla n.:', x[7]
            print'Uscita Cassa:', x[8]
            print''
        i = input('Data uscita:')
        x = "UPDATE `trasporti`.`casse` SET `Uscita_cassa`=%d WHERE  `Commessa`=%d" % (i, d)  # Inserimento istruzioni Sql#
        cursore.execute(x)  # esecuzione istruzioni sql#
        conn.commit()  # scrittura delle istruzioni nel database#
        print''
        print "***Operazione Effettuata!***"
        print''

    def lunghezza():
        print''
        print'***RICERCA PER Lunghezza***'
        print''
        data1 = input("Lunghezza Da: ")
        data2 = input("Lunghezza A: ")
        r = ("select *from casse where lunghezza>= %d and lunghezza<= %d and Uscita_cassa is null or Uscita_cassa=0 " % (data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Commessa:', x[0]
            print'Riferimento:', x[1]
            print'Data Arrivo:', x[2]
            print'Pezzi:', x[3]
            print'Lunghezza:', x[4]
            print'Larghezza:', x[5]
            print'Altezza:', x[6]
            print'Bolla n.:', x[7]
            print'Uscita Cassa:', x[8]
            print''

    def altezza():
        print''
        print'***RICERCA PER Altezza***'
        print''
        data1 = input("Altezza Da: ")
        data2 = input("Altezza A: ")
        r = ("select *from casse where altezza>= %d and altezza<= %d " % (data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Commessa:', x[0]
            print'Riferimento:', x[1]
            print'Data Arrivo:', x[2]
            print'Pezzi:', x[3]
            print'Lunghezza:', x[4]
            print'Larghezza:', x[5]
            print'Altezza:', x[6]
            print'Bolla n.:', x[7]
            print'Uscita Cassa:', x[8]
            print''

    def ricercadata():
        print''
        print'***RICERCA PER DATA DI ARRIVO***'
        print''
        data1 = input("Data da: ")
        data2 = input("Data  A: ")
        r = ("select *from casse where data_arrivo>= %d and data_arrivo<= %d " % (data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Commessa:', x[0]
            print'Riferimento:', x[1]
            print'Data Arrivo:', x[2]
            print'Pezzi:', x[3]
            print'Uscita Cassa:', x[8]
            print''

    def datauscita():
        print''
        print'***RICERCA PER DATA DI USCITA***'
        print''
        data1 = input("Data da: ")
        data2 = input("Data  A: ")
        r = ("select *from casse where Uscita_cassa>= %d and Uscita_cassa<= %d order by Uscita_cassa " % (data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Commessa:', x[0]
            print'Riferimento:', x[1]
            print'Data Arrivo:', x[2]
            print'Pezzi:', x[3]
            print'Uscita Cassa:', x[8]
            print''
    def ordinicasse():

        usc = ''
        while usc != ('S') and usc != ('s'):
            os.system('cls')
            print''
            print'''
            *****************************************************
            *                                                   *
            *                   ORDINI CASSE                    *
            *                                                   *
            *****************************************************

            MENU
            1 - Visualizza
            2 - Inserisci nuove casse ordinate
            3 - Ricerca per Commessa
            4 - Ricerca per Cliente di riferimento
            5 - Ricerca Riferimento


                 '''
            print''
            def vedi():
                cursore.execute("select*from ordinicasse;")
                riga = cursore.fetchall()
                for x in riga:
                    print'='*50
                    print'Id:', x[0]
                    print'Commessa:', x[1]
                    print'Cliente:', x[2]
                    print'Riferimento Cassa:', x[3]
                    print'Tipologia:', x[4]
                    print'Pezzi:', x[5]
                    print'Lunghezza:', x[6]
                    print'Larghezza:', x[7]
                    print'Altezza:', x[8]
                    print 'Data Ordine:',x[9]
                    print''

            def inserisci():
                print''
                print'***REGISTRA ORDINI CASSE***'
                print'='*50
                d = input("Id: ")
                i = input('Commessa:')
                a = raw_input("Cliente: ")
                b = raw_input("Riferimento: ")
                c = raw_input("Tipologia es.(con o senza Cavalletto):")
                m = input('Pezzi:')
                e = input('Lunghezza: ')
                f = input('Larghezza:')
                g = input('Altezza:')
                h = input('Data Ordine:')
                x = "insert into ordinicasse values(%d,%d,'%s','%s','%s',%d,%d,%d,%d,%d)" % (d, i, a, b, c, m, e, f, g,h)  # Inserimento istruzioni Sql#
                cursore.execute(x)  # esecuzione istruzioni sql#
                conn.commit()  # scrittura delle istruzioni nel database#
                print''
                print'***Operazione effettuata***'
                print''

            def ricercacommessa():
                print'***RICERCA COMMESSA***'
                cognome = str(input("Riferimento da ricercare: "))
                r = """select*from ordinicasse where commessa like'""" + "%" + cognome + "%'"
                cursore.execute(r)
                risultato = cursore.fetchall()
                for x in risultato:
                    print'='*50
                    print'Id:', x[0]
                    print'Commessa:', x[1]
                    print'Cliente:', x[2]
                    print'Riferimento Cassa:', x[3]
                    print'Tipologia:', x[4]
                    print'Pezzi:', x[5]
                    print'Lunghezza:', x[6]
                    print'Larghezza:', x[7]
                    print'Altezza:', x[8]
                    print 'Data Ordine:',x[9]
                    print''

            def ricercacliente():
                print''
                print'***RICERCA RIFERIMENTO***'
                cognome = raw_input("Riferimento da ricercare: ")
                r = """select*from ordinicasse where cliente like'""" + "%" + cognome + "%'"
                cursore.execute(r)
                risultato = cursore.fetchall()
                for x in risultato:
                    print'='*50
                    print'Id:', x[0]
                    print'Commessa:', x[1]
                    print'Cliente:', x[2]
                    print'Riferimento Cassa:', x[3]
                    print'Tipologia:', x[4]
                    print'Pezzi:', x[5]
                    print'Lunghezza:', x[6]
                    print'Larghezza:', x[7]
                    print'Altezza:', x[8]
                    print 'Data Ordine:',x[9]
                    print''

            def ricercariferimento():
                print''
                print'***RICERCA RIFERIMENTO***'
                cognome = raw_input("Riferimento da ricercare: ")
                r = """select*from ordinicasse where riferimento_cassa like'""" + "%" + cognome + "%'"
                cursore.execute(r)
                risultato = cursore.fetchall()
                for x in risultato:
                    print'='*50
                    print'Id:', x[0]
                    print'Commessa:', x[1]
                    print'Cliente:', x[2]
                    print'Riferimento Cassa:', x[3]
                    print'Tipologia:', x[4]
                    print'Pezzi:', x[5]
                    print'Lunghezza:', x[6]
                    print'Larghezza:', x[7]
                    print'Altezza:', x[8]
                    print 'Data Ordine:',x[9]
                    print''




            operazione = input('Scegliere il tipo di operazione da effettuare: ')
            if operazione == 1:
                vedi()
            if operazione == 2:
                inserisci()
            if operazione == 3:
                ricercacommessa()
            if operazione==4:
                ricercacliente()
            if operazione==5:
                ricercariferimento()



            usc = raw_input("Vuoi Uscire da GESTIONE CASSE e tornare al MAIN MENU (s/n): ")









    usc = ''
    while usc != ('S') and usc != ('s'):
        os.system('cls')
        print''
        print'''        *****************************************************
        *                                                   *
        *                   GESTIONE CASSE                  *
        *                                                   *
        *****************************************************

        MENU
        1 - Archivio Casse
        2 - Inserisci nuove casse
        3 - Ricerca Commessa
        4 - Ricerca per Cliente di riferimento
        5 - Ricerca per Lunghezza
        6 - Ricerca per Altezza
        7 - Ricerca Per Data di Arrivo
        8 - ORDINI CASSE
        9 - Uscita Casse
        10- Casse a Magazzino
        11- Ricerca per Data di uscita
        12- Riepilogo casse a Magazzino

             '''
        print''
        operazione = input('Scegliere il tipo di operazione da effettuare: ')
        if operazione == 1:
            vedi()
        if operazione == 2:
            inserisci()
        if operazione == 3:
            ricercacommessa()
        if operazione==4:
            ricercariferimento()
        if operazione==5:
            lunghezza()
        if operazione==6:
            altezza()
        if operazione==7:
            ricercadata()
        if operazione==8:
            ordinicasse()
        if operazione==9:
            uscitacasse()
        if operazione==10:
            vedimagazzino()
        if operazione==11:
            datauscita()
        if operazione==12:
            riepilogo()



        usc = raw_input("Vuoi Uscire da GESTIONE CASSE e tornare al MAIN MENU (s/n): ")

def gestioneveneziane():
    def vedi():
        cursore.execute("select*from veneziane1")
        riga = cursore.fetchall()
        for x in riga:
            print'='*50
            print'Id:', x[0]
            print'Codice Pellini:', x[1]
            print'Cliente:', x[2]
            print'Ordine:', x[3]
            print'Pezzi:', x[4]
            print'Data Arrivo:', x[5]
            print'Bolla n.:', x[6]
            print'Accessori:', x[7]
            print''

    def ricercariferimento():
        print''
        print'***RICERCA CLIENTE***'
        cognome = raw_input("Riferimento da ricercare: ")
        r = """select*from veneziane1 where cliente like'""" + "%" + cognome + "%'"
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Id:', x[0]
            print'Codice Pellini:', x[1]
            print'Cliente:', x[2]
            print'Ordine:', x[3]
            print'Pezzi:', x[4]
            print'Data Arrivo:', x[5]
            print'Bolla n.:', x[6]
            print'Accessori:', x[7]
            print''

    def ricercacommessa():
        print'***RICERCA ORDINE***'
        print''
        cognome = str(input("Numero Ordine: "))
        r = """select*from veneziane1 where ordine like'""" + "%" + cognome + "%'"
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Id:', x[0]
            print'Codice Pellini:', x[1]
            print'Cliente:', x[2]
            print'Ordine:', x[3]
            print'Pezzi:', x[4]
            print'Data Arrivo:', x[5]
            print'Bolla n.:', x[6]
            print'Accessori:', x[7]
            print''

    def inserisci():
        print''
        print'***REGISTRA VENEZIANE***'
        print''
        d = input("Id:")
        i = input('Codice Pellini:')
        a = raw_input("Cliente: ")
        b = input("Ordine: ")
        c = input("Pezzi:")
        e = input('Data Arrivo: ')
        f = input('Bolla n.:')
        g = raw_input("Accessori (s/n):")
        x = "insert into veneziane1 values(%d,%d,'%s',%d,%d,%d,%d,'%s')" % (d, i, a, b, c, e, f,g)  # Inserimento istruzioni Sql#
        cursore.execute(x)  # esecuzione istruzioni sql#
        conn.commit()  # scrittura delle istruzioni nel database#

    def inviomail():
        print''
        print'***INVIO MAIL VENEZIANE***'
        print''
        data1 = input("Id iniziale: ")
        data2 = input("Id finale: ")
        r = ("select *from veneziane1 where id>= %d and id <= %d " % (data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print'Id:', x[0]
            print'Codice Pellini:', x[1]
            print'Cliente:', x[2]
            print'Ordine:', x[3]
            print'Pezzi:', x[4]
            print'Data Arrivo:', x[5]
            print'Bolla n.:', x[6]
            print''

        oggetto = "Subject: Arrivo Veneziane"
        contenuto =str(x)
        messaggio = oggetto+contenuto
        email = smtplib.SMTP("smtp.gmail.com", 587)
        email.ehlo()
        email.starttls()
        email.login("alessandro.maruzzella@gmail.com", "Alex270777")
        email.sendmail("alessandro.maruzzella@gmail.com","a.maruzzella@latecnicanelvetro.it",contenuto)
        email.quit()
        print'***Messaggio Inviato***'

    def datarrivo():
        print''
        print'***RICERCA PER DATA DI ARRIVO VENEZIANE***'
        print''
        data1 = input("Data da: ")
        data2 = input("Data  A: ")
        r = ("select *from veneziane1 where data_arrivo>= %d and data_arrivo<= %d " % (data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Id:', x[0]
            print'Codice Pellini:', x[1]
            print'Cliente:', x[2]
            print'Ordine:', x[3]
            print'Pezzi:', x[4]
            print'Data Arrivo:', x[5]
            print'Bolla n.:', x[6]
            print'Accessori:', x[7]
            print''




    def esci():
        esci=raw_input("Premi un tasto per uscire")
    def ricercapellini():
        print''
        print'***RICERCA CODICE PELLINI***'
        cognome = raw_input("Riferimento da ricercare: ")
        r = """select*from veneziane1 where codice_pellini like'""" + "%" + cognome + "%'"
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print'='*50
            print'Id:', x[0]
            print'Codice Pellini:', x[1]
            print'Cliente:', x[2]
            print'Ordine:', x[3]
            print'Pezzi:', x[4]
            print'Data Arrivo:', x[5]
            print'Bolla n.:', x[6]
            print'Accessori:', x[7]
            print''




    usc = ''
    while usc != ('S') and usc != ('s'):
        os.system('cls')
        print''
        print'''        *****************************************************
        *                                                   *
        *                   GESTIONE VENEZIANE              *
        *                                                   *
        *****************************************************

        MENU
        1 - Visualizza
        2 - Inserisci nuove veneziane
        3 - Ricerca Ordine
        4 - Ricerca Cliente
        5 - Ricerca per data arrivo Veneziane
        6 - Ricerca Codice Pellini
        7 - Invio Mail Veneziane
        8 - Esci

             '''
        print''
        operazione = input('Scegliere il tipo di operazione da effettuare: ')
        if operazione == 1:
            vedi()
        if operazione == 2:
            inserisci()
        if operazione == 3:
            ricercacommessa()
        if operazione == 4:
            ricercariferimento()
        if operazione==5:
            datarrivo()
        if operazione==6:
            ricercapellini()
        if operazione==7:
            inviomail()
        if operazione == "":
            print"Scegli tra le operazioni in MENU"
        usc = raw_input("Vuoi Uscire da GESTIONE VENEZIANE e tornare al MAIN MENU (s/n): ")

def gestionecavalletti():
    usc = ''
    while usc != ('S') and usc != ('s'):
        os.system('cls')
        print''
        print'''
        *****************************************************
        *                                                   *
        *               GESTIONE CAVALLETTI                 *
        *                                                   *
        *****************************************************

        MENU
        1 - Visualizza carrelli fatturati
        2 - Inserisci nuovi carrelli fatturati
        3 - Ricerca Cavalletto
        4 - Ricerca Cliente
        5 - Rientro Carrelli
        6 - Cavalletti non Rientrati
        7 - Cavalletti Rientrati per Data
        8 - Esci


                '''

        def visualizza():
            cursore.execute("select*from Cavalletti")
            riga = cursore.fetchall()
            for x in riga:
                print''
                print'='*75
                print'Id:', x[0]
                print'Carrello:', x[1]
                print'Bolla:', x[2]
                print'Data Bolla:', x[3]
                print'Cliente:', x[4]
                print'Fatturato il:', x[5]
                print'Fattura n.:', x[6]
                print'Data rientro',x[7]
                print''

        def inserimento():
            print''
            print'***REGISTRA CAVALLETTI***'
            print''
            print'='*50
            d = input("Id:")
            i = input('Carrello:')
            a = input("Bolla: ")
            b = input("Data Bolla: ")
            c = raw_input("Cliente:")
            e = input('Fatturato il: ')
            f = input('Fattura n.:')
            h = input('Data Rientro:')
            x = "insert into cavalletti values(%d,'%s',%d,%d,'%s',%d,%d,%d)" % (d,i, a, b, c, e, f,h)  # Inserimento istruzioni Sql#
            cursore.execute(x)  # esecuzione istruzioni sql#
            conn.commit()  # scrittura delle istruzioni nel database#
            print'***OPERAZIONE EFFETTUATA***'

        def ricercacliente():
            print'***RICERCA Cliente***'
            cognome = str(raw_input("Cliente da ricercare: "))
            r = """select*from cavalletti where cliente like'""" + "%" + cognome + "%'"
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print'='*50
                print'Id:', x[0]
                print'Carrello:', x[1]
                print'Bolla:', x[2]
                print'Data Bolla:', x[3]
                print'Cliente:', x[4]
                print'Fatturato il:', x[5]
                print'Fattura n.:', x[6]
                print'Data rientro',x[7]
                print''

        def ricercacavalletto():
            print'***RICERCA Cavalletto***'
            cognome = str(raw_input("Cavalletto da ricercare: "))
            r = """select*from cavalletti where carrello like'""" + "%" + cognome + "%'"
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print'='*50
                print'Id:', x[0]
                print'Carrello:', x[1]
                print'Bolla:', x[2]
                print'Data Bolla:', x[3]
                print'Cliente:', x[4]
                print'Fatturato il:', x[5]
                print'Fattura n.:', x[6]
                print'Data rientro',x[7]
                print''
        def rientrocavalletto():
            print''
            print'***RIENTRO CAVALLETTO***'
            print''
            d = input("n.CAVALLETTO: ")
            r =("select*from cavalletti where carrello=%d") %(d)
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print'='*50
                print'Id:', x[0]
                print'Carrello:', x[1]
                print'Bolla:', x[2]
                print'Data Bolla:', x[3]
                print'Cliente:', x[4]
                print'Fatturato il:', x[5]
                print'Fattura n.:', x[6]
                print''
            i = input('Data rientro:')
            x = "UPDATE `trasporti`.`cavalletti` SET `Data_rientro`=%d WHERE  `Carrello`=%d" % (i, d)  # Inserimento istruzioni Sql#
            cursore.execute(x)  # esecuzione istruzioni sql#
            conn.commit()  # scrittura delle istruzioni nel database#
            print''
            print "***Operazione Effettuata!***"
            print''

        def cavallettiout():
            cursore.execute("select*from cavalletti where Data_rientro=0 or Data_rientro is null order by cliente;")
            riga = cursore.fetchall()
            for x in riga:
                print'='*50
                print'Id:', x[0]
                print'Carrello:', x[1]
                print'Cliente:', x[4]
                print'Fatturato il:', x[5]
                print'Fattura n.:', x[6]
                print''

        def cavallettirientrati():
            print'***RICERCA CAVALLETTI RIENTRATI***'
            data1=input('Data da:')
            data2=input('Data a :')
            r =("select*from cavalletti where Data_rientro>='%d' and Data_rientro<='%d'"%(data1,data2))
            cursore.execute(r)
            risultato = cursore.fetchall()
            for x in risultato:
                print''
                print'='*50
                print'Id:', x[0]
                print'Carrello:', x[1]
                print'Bolla:', x[2]
                print'Data Bolla:', x[3]
                print'Cliente:', x[4]
                print'Fatturato il:', x[5]
                print'Fattura n.:', x[6]
                print'Data rientro',x[7]
                print''

        operazione = input('Scegliere il tipo di operazione da effettuare: ')
        if operazione == 1:
            visualizza()
        if operazione == 2:
            inserimento()
        if operazione == 3:
            ricercacavalletto()
        if operazione == 4:
            ricercacliente()
        if operazione == 5:
            rientrocavalletto()
        if operazione == 6:
            cavallettiout()
        if operazione == 7:
            cavallettirientrati()
        if operazione == "":
            print"Scegli tra le operazioni in MENU"
        usc = raw_input("Vuoi Uscire da GESTIONE CAVALLETTI e tornare al MAIN MENU (s/n): ")

def incidenza():
    print''
    print'***CALCOLA INCIDENZA TRASPORTI SU FATTURATO PER PERIODO***'
    print''
    data1 = input("Data iniziale: ")
    data2 = input("Data finale  : ")
    r = ("select sum(prezzo)from trasportatori where  data>= %d and data <= %d " % ( data1, data2))
    s = ("select sum(Totale_fatturato/1.22)from trasportatori where  data>= %d and data <= %d " % ( data1, data2))
    z = ("select sum(Trasporto_fatturato)from trasportatori where  data>= %d and data <= %d " % ( data1, data2))
    cursore.execute(r)
    risultato = cursore.fetchall()
    for x in risultato:
        print''
        print'**************************'
        print 'Costo Trasporti :', x[0]
        print'**************************'
        print'          -'
    cursore.execute(z)
    fatturato = cursore.fetchall()
    for z in fatturato:
        print''
        print'******************************'
        print 'Trasporti Fatturati :', z[0]
        print'******************************'
        print'          :'
    cursore.execute(s)
    totale = cursore.fetchall()
    for y in totale:
        print''
        print'***************************'
        print 'Totale Fatturato :',round (y[0])
        print'***************************'
        print'          ='


    incidenza=((x[0]-z[0])/y[0])

    print''
    print 'Totale Incidenza Costo Trasporto:',round(incidenza*100),'%'

def gestioneautisti():

    def inserimento():
        print''
        print'***REGISTRA TRASPORTO***'
        print''
        d=input("Numero Trasporto: ")
        i=input('Partenza:')
        a=raw_input("Autista: ")
        b=raw_input("Camion: ")
        c=raw_input("Clienti:")
        e=raw_input('Destinazione: ')
        f=raw_input('Regione:')
        g=float(input('Fatturato:'))
        h=raw_input('Numero Documenti:')
        l=input('Arrivo:')
        m=float(input('Costi:'))
        n=float(input('Trasporto Fatturato:'))
        print '''
        ---------------------------
        ***Calcolo Costo Gasolio***
        ---------------------------
        '''
        gasolio=1.58
        km=input('Km da percorrere:')
        totale= float(gasolio*(km/2.4))
        print'Costo Gasolio a Lt:',gasolio,'euro'
        print 'Costo Gasolio:', round(float(totale)),'euro'
        x="insert into autisti values(%d,%d,'%s','%s','%s','%s','%s',%d,'%s',%d,%d,%d,%d)"%(d,i,a,b,c,e,f,g,h,l,m,n,totale)#Inserimento istruzioni Sql#
        cursore.execute(x)#esecuzione istruzioni sql#
        conn.commit()#scrittura delle istruzioni nel database#
        print'''
        ***OPERAZIONE EFFETTUATA***
        '''
    def visualizza():
        cursore.execute("select*from autisti")
        riga=cursore.fetchall()
        for x in riga:
            print''
            print '='*70
            print'Id:',x[0]
            print'Partenza:',x[1]
            print'Autista:',x[2]
            print'Camion:',x[3]
            print'Clienti:',x[4]
            print'Destinazione:',x[5]
            print'Regione:',x[6]
            print'Fatturato:',x[7]
            print'Numero Fatture:',x[8]
            print'Arrivo:', x[9]
            print'Costi:',x[10]
            print'Trasporto Fatturato:',x[11]
            print'Costo Gasolio:', x[12]
            print''

    def arrivocosti():
        print''
        print'***Aggiorna Arrivo e Costi Trasporto***'
        print''
        d = input("id Trasporto: ")
        r =("select*from autisti where id=%d") %(d)
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print '='*70
            print'Id:',x[0]
            print'Partenza:',x[1]
            print'Autista:',x[2]
            print'Camion:',x[3]
            print'Clienti:',x[4]
            print'Destinazione:',x[5]
            print'Regione:',x[6]
            print'Fatturato:',x[7]
            print'Numero Fatture:',x[8]
            print'Arrivo:', x[9]
            print'Costi:',x[10]
            print'Trasporto Fatturato:',x[11]
            print'Costo Gasolio:', x[12]
            print''

        i = input('Data di Arrivo:')
        e = input('Costi Trasporto:')
        x = "UPDATE `trasporti`.`autisti` SET `Arrivo`=%d WHERE`Id`=%d" % (i, d)  # Inserimento istruzioni Sql#
        cursore.execute(x)  # esecuzione istruzioni sql#
        conn.commit()  # scrittura delle istruzioni nel database#
        n = "UPDATE `trasporti`.`autisti` SET `Costi`=%d WHERE`Id`=%d" % (e, d)  # Inserimento istruzioni Sql#
        cursore.execute(n)  # esecuzione istruzioni sql#
        conn.commit()  # scrittura delle istruzioni nel database#
        print''
        print "***Operazione Effettuata!***"
        print''

    def regione():
        print''
        print'***RICERCA PER  REGIONE***'
        citta = raw_input("Regione da ricercare: ")
        r = """select*from autisti where regione like'""" + "%" + citta + "%'"
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print '=' * 70
            print'Id:', x[0]
            print'Partenza:', x[1]
            print'Autista:', x[2]
            print'Camion:', x[3]
            print'Clienti:', x[4]
            print'Destinazione:', x[5]
            print'Regione:', x[6]
            print'Fatturato:', x[7]
            print'Numero Fatture:', x[8]
            print'Arrivo:', x[9]
            print'Costi:', x[10]
            print'Trasporto Fatturato:', x[11]
            print'Costo Gasolio:', x[12]
            print''

    def regioneautista():
        print''
        print'***RICERCA REGIONE E AUTISTA***'
        print''
        regione = raw_input("Inserire regione:")
        vettore= raw_input("Autista:")
        r = ("select*from trasporti.autisti where regione ='%s'and autista='%s'")% (regione, vettore)
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print '=' * 70
            print'Id:', x[0]
            print'Partenza:', x[1]
            print'Autista:', x[2]
            print'Camion:', x[3]
            print'Clienti:', x[4]
            print'Destinazione:', x[5]
            print'Regione:', x[6]
            print'Fatturato:', x[7]
            print'Numero Fatture:', x[8]
            print'Arrivo:', x[9]
            print'Costi:', x[10]
            print'Trasporto Fatturato:', x[11]
            print'Costo Gasolio:', x[12]
            print''
    def data():
        print''
        print'***RICERCA TRASPORTI PER DATA***'
        print''
        data1 = input("Data iniziale: ")
        data2 = input("Data   finale: ")
        r = ("select *from trasporti.autisti where  partenza>= %d and partenza <= %d order by partenza" % (data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print '=' * 70
            print'Id:', x[0]
            print'Partenza:', x[1]
            print'Autista:', x[2]
            print'Camion:', x[3]
            print'Clienti:', x[4]
            print'Destinazione:', x[5]
            print'Regione:', x[6]
            print'Fatturato:', x[7]
            print'Numero Fatture:', x[8]
            print'Arrivo:', x[9]
            print'Costi:', x[10]
            print'Trasporto Fatturato:', x[11]
            print'Costo Gasolio:', x[12]
            print''

    def citta():
        print''
        print'***RICERCA DESTINAZIONE***'
        citta = raw_input("Citta' da ricercare: ")
        r = """select*from autisti where destinazione like'""" + "%" + citta + "%'"
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print '=' * 70
            print'Id:', x[0]
            print'Partenza:', x[1]
            print'Autista:', x[2]
            print'Camion:', x[3]
            print'Clienti:', x[4]
            print'Destinazione:', x[5]
            print'Regione:', x[6]
            print'Fatturato:', x[7]
            print'Numero Fatture:', x[8]
            print'Arrivo:', x[9]
            print'Costi:', x[10]
            print'Trasporto Fatturato:', x[11]
            print'Costo Gasolio:', x[12]
            print''

    def clienti():
        print''
        print'***RICERCA CLIENTE***'
        nome = raw_input("Cliente da ricercare: ")
        r = """select*from autisti where clienti like'""" + "%" + nome + "%'"
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print '=' * 70
            print'Id:', x[0]
            print'Partenza:', x[1]
            print'Autista:', x[2]
            print'Camion:', x[3]
            print'Clienti:', x[4]
            print'Destinazione:', x[5]
            print'Regione:', x[6]
            print'Fatturato:', x[7]
            print'Numero Fatture:', x[8]
            print'Arrivo:', x[9]
            print'Costi:', x[10]
            print'Trasporto Fatturato:', x[11]
            print'Costo Gasolio:', x[12]
            print''

    def calcolofatturato():
        print''
        print'***CALCOLA COSTO TRASPORTI PER PERIODO***'
        print''
        data1 = input("Data iniziale: ")
        data2 = input("Data   finale: ")
        r = ("select sum(fatturato)from trasporti.autisti where  partenza>= %d and partenza<= %d " % ( data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print'**************************'
            print 'Totale Periodo :', x[0]
            print'**************************'

    def riepilogomensile():
        print''
        print colored('***RIEPILOGO TRASPORTI MENSILI***','magenta',attrs=['bold'])
        print''
        data1 = input("Data iniziale: ")
        data2 = input("Data   finale: ")
        r = ("select count(*),autista,sum(fatturato/1.22),sum(costi),sum(gasolio)from autisti where partenza>=%d and partenza <=%d group by autista" % (data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print '=' * 70
            print'Viaggi:',x[0]
            print('Autista:'),colored(x[1],'cyan',attrs=['bold'])
            print('Totale Fatturato:'),colored(round(x[2]),'green',attrs=['bold'])
            print('Totale Costi:'),colored(x[3],'red',attrs=['bold'])
            print('Totale Gasolio:'),colored(x[4],'yellow',attrs=['bold'])
            print('')


    usc = ''
    while usc != ('S') and usc != ('s'):
        os.system('cls')
        print''
        print'''        *****************************************************
        *                                                   *
        *             GESTIONE TRASPORTI INTERNI            *
        *                                                   *
        *****************************************************

        MENU
        1 - Visualizza Trasporti
        2 - Nuovo Trasporto
        3 - Aggiorna Arrivo e Costi Trasporto
        9 - Totale Fatturato trasportato per periodo
        10- Riepilogo Mensile


        *****RICERCHE*****
        4 - Ricerca Regione
        5 - Ricerca Autista e Regione
        6 - Ricerca per Data
        7 - Ricerca per Citta'
        8 - Ricerca per Cliente


             '''
        print''
        operazione = input('Scegliere il tipo di operazione da effettuare: ')
        if operazione == 2:
            inserimento()
        if operazione == 1:
            visualizza()
        if operazione == 3:
            arrivocosti()
        if operazione == 4:
            regione()
        if operazione == 5:
            regioneautista()
        if operazione == 6:
            data()
        if operazione == 7:
            citta()
        if operazione == 8:
            clienti()
        if operazione == 9:
            calcolofatturato()
        if operazione == 10:
            riepilogomensile()


        usc = raw_input("Vuoi Uscire da TRASPORTI INTERNI e tornare al MAIN MENU (s/n): ")

def costogasolio():
    print''
    print '***Costo Medio Viaggio***'
    print''
    gasolio=input('Costo Gasolio a Litro:')
    km=input('Km da percorrere:')
    totale= float(gasolio*(km/2.5))
    print 'Costo Gasolio:', float(totale),'euro'
    print''

def trasportoparziale():

    def vediparziali():
        cursore.execute("select*from trasportatori where trasporto_parziale ='s'or trasporto_parziale='S'or trasporto_parziale='si'")
        riga=cursore.fetchall()
        for x in riga:
            print''
            print '='*70
            print'Id:',x[0]
            print'Data:',x[1]
            print'Vettore:',x[2]
            print'Clienti:',x[3]
            print'Destinazione:',x[4]
            print'Prezzo:',x[6]
            print'Fatture:', x[9]
            print'Trasporto Fatturato:',x[10]
            print'Totale Fatturato:',x[11]
            print'Trasporto Parziale:',x[12]
            print'Quota Prezzo Parziale:',x[13]
            print'Motivazione:',colored(x[14],'yellow',attrs=['bold'])
            print''
        cursore.execute("select sum(Quota_prezzo_parz)from trasportatori where trasporto_parziale ='s'or trasporto_parziale='S'or trasporto_parziale='si'")
        riga=cursore.fetchall()
        for y in riga:
            print''
            print'*************************************************'
            print'Totale Costo Trasporto Parziali:', colored(y[0],'red',attrs=['bold']),'euro'
            print'*************************************************'
            print''

    def parzialidata():
        print''
        print'***TRASPORTI PARZIALI PER DATA***'
        print''
        data1 = input("Data iniziale: ")
        data2 = input("Data   finale: ")
        r = ("select*from trasportatori where trasporto_parziale ='s' and trasporto_parziale='S' and data>= %d and data <= %d " % ( data1, data2))
        cursore.execute(r)
        risultato = cursore.fetchall()
        for x in risultato:
            print''
            print '='*70
            print'Id:',x[0]
            print'Data:',x[1]
            print'Vettore:',x[2]
            print'Clienti:',x[3]
            print'Destinazione:',x[4]
            print'Prezzo:',x[6]
            print'Fatture:', x[9]
            print'Trasporto Fatturato:',x[10]
            print'Totale Fatturato:',x[11]
            print'Trasporto Parziale:',x[12]
            print'Quota Prezzo Parziale:',x[13]
            print'Motivazione:',colored(x[14],'yellow',attrs=['bold'])
            print''
        cursore.execute("select sum(Quota_prezzo_parz)from trasportatori where trasporto_parziale ='s' and data>= %d and data <= %d " % ( data1, data2))
        riga=cursore.fetchall()
        for y in riga:
            print''
            print'*************************************************'
            print'Totale Costo Parziali per Periodo:',colored(y[0],'red',attrs=['bold']),'euro'
            print'*************************************************'






    usc = ''
    while usc != ('S') and usc != ('s'):
        os.system('cls')
        print''
        print'''        *****************************************************
        *                                                   *
        *                   TRASPORTO PARZIALE              *
        *                                                   *
        *****************************************************

        MENU
        1 - Visualizza Trasporti Parziali
        2 - Trasporti parziali per Data


             '''

        operazione = input('Scegliere il tipo di operazione da effettuare: ')
        if operazione == 1:
            vediparziali()
        if operazione == 2:
            parzialidata()
            print''
        usc = raw_input("Vuoi Uscire da GESTIONE VENEZIANE e tornare al MAIN MENU (s/n): ")

usc=''
while usc!=('N') and usc!=('n'):
    os.system('cls')
    print''
    print colored('''             *****************************************************
             *               GESTIONE LOGISTICA                  *
             *           Vers.01.19 by A. Maruzzella             *
             *          aggiornato a data 05.01.2019             *
             *****************************************************
     ''','cyan', attrs=['bold'])
    print colored('''
    MAIN MENU

    1 - Visualizza Tutti i trasporti
    2 - Inserimento Nuovo Trasporto
    3 - MENU RICERCHE TRASPORTI
    4 - Calcola Costo Trasporti per Vettore
    5 - Calcola Costo Trasporti per Periodo
    6 - Calcolo Peso Vetri
    7 - GOOGLE MAPS SEARCH
    8 - GESTIONE CASSE IN LEGNO
    9 - GESTIONE VENEZIANE
    10- GESTIONE CAVALLETTI
    11- Calcolo Incidenza Trasporti su fatturato
    12- GESTIONE TRASPORTI INTERNI
    13- Costo Gasolio
    14- TRASPORTO PARZIALE

    ''','green', attrs=['bold'])


    print''
    try:
        print''
        operazione=input('Scegliere il tipo di operazione da effettuare: ')
        if operazione==1:
            visualizza()
        if operazione==2:
            inserimento()
        if operazione==3:
            ricerche()
        if operazione==4:
            costotrasporto()
        if operazione==5:
            costoperiodo()
        if operazione==6:
            pesovetri()
        if operazione==7:
            googlesearch()
        if operazione==8:
            gestionecasse()
        if operazione==9:
            gestioneveneziane()
        if operazione==10:
            gestionecavalletti()
        if operazione==11:
            incidenza()
        if operazione==12:
            gestioneautisti()
        if operazione==13:
            costogasolio()
        if operazione==14:
            trasportoparziale()



    except:
        print'****************************************************************************'
        print"       Errore!!!...Inserire Correttamente tutti i dati richiesti            "
        print'****************************************************************************'



    print''
    print''
    print'==========================MAIN MENU================================'
    usc=raw_input("Effettuare una nuova operazione? (s)Continua (n)Esci dal programma: ")
