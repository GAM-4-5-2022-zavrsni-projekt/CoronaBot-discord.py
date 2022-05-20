# CoronaBot

https://discord.com/api/oauth2/authorize?client_id=975867444583350343&permissions=51264&scope=bot

Corona bot programiran je korištenjem discord.py modula u pythonu. Glavni korišteni moduli su bili sljedeći:

discord.py https://discordpy.readthedocs.io/en/stable/

beautiful soup(povlačenje podataka s web-stranica) https://beautiful-soup-4.readthedocs.io/en/latest/

asyncio(modul koji dopušta izradu koda i komanda koje se mogu izvoditi istovremeno) https://docs.python.org/3/library/asyncio.html

Inače discord je jedan veoma napredan messenger koji uostalom daje mogućnost izrade botova i aplikacija koje korisnici mogu ubacivati u svoje kanale. Ti botovi imaju beskonačno primjena od organizacije igara na kanalima do moderacije i slušanje glazbe. Botove na servere mogu stavljati samo administratori te ih mogu maknuti u bilo kojem trenutku. Pri dodavanju bota veoma je važno provjeriti dopuštenja i ovlasti koje mu dajete jer u protivnom bi mogao nanijeti štetu kanalu i korisnicima.

CoronaBot je bot koji služi davanju svakodnevnih obavijesti o broju zaraženih SARS Cov-2 virusom u Hrvatskoj. Ne zahtijeva nikakve posebne ovlasti te bi trebao raditi 24/7. Pozivni znak CoronaBot-a je % te se treba stavljati ispred svake komande. Dostupne komande su:

%help - daje popis svih komanda bota

%info - daje kratku informaciju o botu

%ping - vrača ping bota

%corona [država] - vrača relevantne podatke o epidemiji korone za neku državu. Default država je Hrvatska

%subscribe [ime kanala] - pretplačuje upisani kanal na svakodnevne informacije o kovidu u Hrvatskoj

%unsubscribe [ime kanala] - otkazuje pretplatu na upisanom kanalu

Sam bot je hostan na web stranici repl.it te se uz pomoć servera keep_alive.py drži na životu. Također uz pomoć monitora uptimerobot.com stalno se šalju pingovi koji ne daju repl.it-u da izgasi robota. Sve to omogućuje neprekinut i besplatan rad bota. Također je bitno napomenuti da nije moguće samo skopirati kod iz ovoga kompjutora te pokrenuti vlastitog bota jer se prvo svaki bot treba registrirati na developer portalu dicorda da bi se dobio ključ neophodan za rad s discord.py-em.




# TLDR:
Kliknite link koji se nalazi gore i stavite bota na neki server te upišite %info ili % help. Bot služi dobivanju informacija o novozaraženim od kovida. Podatci dolaze s wordlometers-a.
