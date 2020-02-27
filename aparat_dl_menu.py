__author__ = "https://github.com/mehdigudy, https://gitlab.com/frowzyispenguin"
__license__ = "GNU3"
__version__ = "0.1"
__maintainer__ = "Mehdi"
__email__ = "thisismrmehdi@hotmail.com"


import sys
from aparat_dl_Api import AparatDlApi as ap


def main():
	# TODO: add schedule features
	# getting the argumants
	arg = sys.argv[:]
	try:
		if arg.count("-H") or arg.count("--help"):
			print(
	
                '''
            Options:
                -H , --help : Helps you =)
                -A , --allvideos  : Download whole Channel
                        aparat_dl -A [link]
                -L , --playlist : Download whole playlist
                        aparat_dl -L [link]
                -SL, --selectfromlist: Download videos by selection on a playlist : 
                        aparat_dl  -SL [startpoint] [endpoint] [link]


            '''

			)
		elif len(arg) == 1:
			print("""
			There is no link
			Use help -H or --help to see how scripts work
			Aparat-dl.py [argumans][link]
			""")

		elif len(arg) == 2 and arg[-1].count("http") or len(arg) == 2 and arg[-1].count("https"):
			try:
				ap.singleVideo(arg[-1])
			except:
				pass
		elif len(arg) == 3 and arg.count("-L") or len(arg) == 3 and arg.count("--playlist"):
			if arg[-1].count("https://") or arg[-1].count("http://"):
				try:
					ap.playList(arg[-1])
				except Exception as identifier:
					print("Excepiton : " + str(identifier))

		elif len(arg) == 3 and arg.count("-A") or len(arg) == 3 and arg.count("--allvideos"):
			if arg[-1].count("https://") or arg[-1].count("http://"):
				try:
					ap.wholeChannel(arg[-1])
				except Exception as identifier:
					print("Excepiton : " + str(identifier))

		elif len(arg) == 5 and arg.count("-SL") or len(arg) == 5 and arg.count("--selectfromlist"):
			if arg[-1].count("https://") or arg[-1].count("http://"):
				try:
					ap.selectFromPlayList(arg[-1] , int(arg[-3]) ,int(arg[-2]))
				except Exception as identifier:
					print("Excepiton : " + str(identifier))          
		else:
			print(	"""
			Use help -H or --help to see how scripts work
			Aparat-dl.py [argumans][link]
			""")
	except KeyboardInterrupt as e:
		print ("\n you just killed the program mate ")
		sys.exit()
	except Exception as e:
		print(str(e))


if __name__ == "__main__":
	main()
