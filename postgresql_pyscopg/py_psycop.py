import psycopg

with psycopg.connect("host=localhost dbname=postgres user=postgres password=mysecretpassword port=5432") as conn:

    
        
        # cur.execute("""
        #     CREATE TABLE languages (language VARCHAR(50), speakers INTEGER, family VARCHAR(50));
        # """)

        # cur.execute("""
        #     INSERT INTO languages (language, speakers, family)
        #     VALUES  ('Spanish', 484, 'Indo-European'),
	    #             ('English', 390, 'Indo-European'),
        #             ('Hindi',   345, 'Indo-European');
        # """)

        # cur.execute("SELECT * FROM languages")
        # langlist = cur.fetchall() 
        # for i in range(len(langlist)):
        #     print(langlist[i][0])
        while True:
            print('Enter exit to exit or enter to continue: ')
            yes_or_not = input()
            if yes_or_not != 'exit':
                print('Enter language: ')    
                language = input()
                print('Enter number of speakers: ')
                speakers = int(input())
                print('Enter language family: ')
                family = input()

                with conn.cursor() as cur:
                    cur.execute("""
                                    INSERT INTO languages 
                                    (language, speakers, family) 
                                    VALUES 
                                    (%(language)s, %(speakers)s, %(family)s)""", 
                                    {
                                    'language':language,
                                    'speakers':speakers,
                                    'family':family
                                    })
                    cur.execute("SELECT * FROM languages")
                    print(cur.fetchall())
            else:
                break