import base64
import random
import string
seconds = 5
Loop_start = 0
Loop_end = 100
for i in range(Loop_start, Loop_end):
         message = str(i)+"85db7f4-4f2a-9f8e-fe99a"+str(random.randint(1, 1000))+random.choice(string.ascii_letters)+ str(random.randint(1, 200))+random.choice(string.ascii_letters)+random.choice(string.ascii_letters) +random.choice(string.ascii_letters) +random.choice(string.ascii_letters) + str(i)
         dummydata = str( i ) + "85db7f4-4f2c-9f8e-fe99b" + str( random.randint( 1000, 2000 ) ) + random.choice(
             string.ascii_letters ) + str( random.randint( 1, 200 ) ) + random.choice(
             string.ascii_letters ) + random.choice( string.ascii_letters ) + random.choice(
             string.ascii_letters ) + random.choice( string.ascii_letters ) + str( i )
         message_bytes = message.encode('ascii')
         base64s_bytes = base64.b64encode(message_bytes)
         base64s_message = base64s_bytes.decode('ascii')
         mytext = {"Times": message,"Timex":dummydata,"Timed": base64s_message}
         m1 = list(mytext.values())
         s1 = str( m1 )
         s1 = s1.strip( "[']" )
         s1 = s1.replace( "'", "" )
         s1 = s1.replace( " ", "" )
         output_writer = open( 'samplefile.csv', mode='w' )
         output_writer.write(s1)
         output_writer.write( '\n' )
         print( s1 )