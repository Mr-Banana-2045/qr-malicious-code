from http.server import BaseHTTPRequestHandler, HTTPServer
import qrcode
import os
class color:
    red='\033[91m'
    green='\033[92m'
    blue='\033[94m'
print(f"""{color.blue}
'.................:KWx.,kMMMMK:.lNMMMMMMMK:......:KMMMMMMMMM0;.................'
.  ,:::::::::::;. '0Wo .xMMMMXo:loxXMMMMMXd:'  .:oXMKxdddxKM0' .;:::::::::::,  .
. 'OMWNXXXXXXWMN: 'OWo .xMMWNNWWx..kMMMMMWNXo..dWMMWd..   oW0' :NMWXXXXXXNWMO' .
. '0Wx,.....'xWN: '0Wo .xMWd':0MN0KNMMMMMKc..  dMMMMN00l. oW0' cNWx'.....,xW0' .
. '0Wo       lWN: '0M0lclol' .:ooodKMMMMMXxc'  ,okNMMMMx. oW0' :NWl       oW0' .
. 'OWo       lWN: '0MNXO,   ......'kMWXXXXXKl    .xKXXXd'.xW0' :NWl       oWO' .
. '0Wd.     .oWN: '0Wk,.   c0K00000NM0:.....      .....cOKNMO' :NWo.     .dW0' .
. '0MXOOOOOOOXMN: '0MXOd'  oWKl''';OMN0OOd.    :kl. ,kOKWMMM0' cNMXOOOOOOOXM0' .
. .cdddddddddddo' '0MKxoc::ldoc:. .xMXkddoc:'  dMO. cNMXxxKM0' 'odddddddddddc.  
.   ............  ,0Wd..dXKc.'kXo..dXk'  'xXo. dM0,.cKNd. oW0,   ...  ......   .
000000000000000000KWMN0k:.'lOx;.cOkc.:x00k:.. .dWWKOl'..  oWWK000000000000000000
. .xXNMXc.       ..   .....oKk. ;00; ,0MMMMMWX0c.;KWo  ,O0c.;0MWXKc .kMx.  ..  .
.  ..oNWXKo.    cKd. ;0KKKKK00kxk00xlcxkkk0NXKKKKXWMKxxkkcoKXWWx'.  .kMx. cKx. .
l:,  cNMMMk. .:cldoc:ldKMMMMMMMWX0kkkOKXXKOkkOKNWMMMMMMMNkOWMMWd  .:codoccOMXd:l
K0x;.cO000o. lWNo.;x0c.dWMMWNKOkkOKNWMMMMMMWX0kkkOKNWMMMMWXKXWWx'.dWK, ;XMMMWK0K
..,kXo....   lWMNXk,. .dNKOkkk0XWMMMMMMMMMMMMMMNX0kxk0XWMNl.;0MWXXWMK, ;XMMM0;..
doocclooooooolcccc,  .o0OokXWMMMMMMMMMMMMMMMMMMMMMWNKxoKNd.  ,ccccOWK, ;XWkc,  .
MMO. ,kOOOOOOl'''''''dNWkoKMMMMWNWMMMMMMMMMMMMWWWMMMM0o0X;.'.     ;kx:'lXNd'.  .
MMO'        .lXNNNNNNNWWkoKMMMMXkk  MMMMMMMWM  0NMMMM0o0XclXk.      .xNWWWWNk. .
c;coxxxxxx:. lWWx:;;;;ckxoKMMMMMWK   MMMMMWK   WMMMMM0o0WOl:'       .kM0c;;;'  .
  .;lOWMMMXdo0WWOo;.   oxoKMMMMMMMMMMMMMMMMMMMMMMMMMM0o0Nkll:. .cllllll,  'lllld
'....cOKNMMMMNK000d.  'xxoKMMMMMMMMMMMMMMMMMMMWNXWMMMOo0KcoWK:.cOKNMXc...'o0KWMM
XXXXXo.'kMMMWo....   :KNkoKMMMMMMMMMMMMMMMMMWK   WMMMOo0KcoWWNXo..oWWNXXXKc.,0MM
lccccloolcxNWl  ,oood0WWklONMMMMMMMMN          NWMMWNxoKN0KMMMMKdolccccxNNc  ,cl
.    cNX; .dk;  :OKWMX0XXOkxk0XWMMMMWXKKKKKKXWMWNKOkkk0NMMMMMMMMMWx,.  'xkc'.   
     :X0,  ...  ..;ONo.dWMWNKOkxk0NWMMMMMMMMWX0kkkOXNMMMMMWNWMMMMMNXO,   .lKk' .
.    .'.  .dOOOOOOd;'..dWMMMMMWX0kkkOKNWWN0kkkOKNWMMMMMMMWd'cKMMMWx,;dOc  .';xO0
.         .okkkkkkd:,,:OMMMX0000XWNOocccccldkO000KWMN0000x, .lkkkx; .ckc    .lkO
Okkkkkkkkkkkkkkkkk0NWk;:0MNc    :NWKkl.  .lkkkd'  ',lxkc  ;kkkkkkx;            .              QR malicious code
.                 '0Wo .xMMMM0'   .xMO.  .xNWMMWNNNXl     oW0,.lNWl      .dWWNNN         --------------------------
. .oOOOOOOOOOOOk, '0Wo .xMMMM0' ,x0NMk.   .'oNNo''''.     oWWKOXWWl .lOOO0XMKc';      A tool to build qr malicious code
. '0MKdoooood0WN: '0Wo .xMW0doccloooo:.   ,cxNX:          ,ooooooo'  ;dOWMMMXdcl            Add file on locals
. '0Wo       lWN: 'OWo  ckxl,cKWd.    ',,c0MMMN:    .,,,,'.  .,.  .,'  .dkkk0NMM         See file without problems
. '0Wo       lWN: '0Wd.   .lXNWWd.   '0WWWWWWMN:    cXNNNK: .ONo  cXO'      'OWW               god developer
. '0Wo       lWNc '0MXOd.  .,cKMXOd' ,0MMXl,dNN: .okl;,,,'. 'OWd  .,'  .dx,  .,:      https://github.com/Mr-Banana-2045
. '0WOc;;;;;:kWNc '0MMMX;    .OMXko. .lxxdc:cdo' .cdl:;;;;;;cod;       .odl:'  .
. .kNNNNNNNNNNNK: 'OMWN0;    'kNd.       'kNd.     .cKNNNNWM0,           .dW0, .
.  .'''''''''''.. '0Mk,,dOOOOx:'ckOOOOOOOx:'ckx, .dOl,''',kWWKOOOO;    'x0XMWKO0
.                 '0Wo .xMMMM0' :NMMMMMMM0' :XX: '0Wo     oWMMMMMWl    ;KMMMMMMM
{color.green}        [0] file QRcode          [1] add localhost
""")
go = input(f"{color.red}inter add number > ")
if go >= '0':
    if go == '0':
        mtn = input(f"{color.red}add file And txt > ")
        address = input("add Extension file > ")
        img = qrcode.make(mtn)
        type(img)
        img.save(address)
        print(f"{color.green}[+]add files")
        file = input(f"{color.red}View File [y/n] > ")
        if file =='y':
            os.system(f"display batch {address}")
        else:
            print(f"{color.green}OK")
else:
    print("")
namer = input(f"{color.red}add name link > ")
mtne = input("add file And txt > ")
addresse = input("add link And txt > ")
img = qrcode.make(mtne)
type(img)
img.save(addresse)
class MyServere(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.log_message('online')
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("<html><head><title>QR-malicious-code</title></head>", "utf-8"))
    self.wfile.write(bytes(addresse))
    self.wfile.write(bytes("</body></html>", "utf-8"))
if __name__ == "__main__":
    webServere = HTTPServer(('127.0.0.1', 2020), MyServere)
    print(f"{color.red}Server host :{color.green} http://%s:%s%s%s{color.green}" % ('127.0.0.1', 2020,'/', namer))
    try:
        webServere.serve_forever()
    except KeyboardInterrupt:
        pass