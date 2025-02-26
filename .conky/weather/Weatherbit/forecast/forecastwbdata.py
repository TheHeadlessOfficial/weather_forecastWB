import os
import requests
import time
# Lock file to tell conky that the script is running
lock_file = "/tmp/script_wbforecast.lock"
# Check for file lock
try:
    open(lock_file, 'w').close()
    ################################ set your latitude, longitude and APPID (don't delete apostrophes)
    mylat = 
    mylon = 
    myAPPID = ''
    ################################ pattern url forecast
    url = 'https://api.weatherbit.io/v2.0/forecast/daily?lat=' + str(mylat) + '&lon=' + str(mylon) + '&key=' + myAPPID
    res = requests.get(url).json()
    data = res
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set paths
    home = '/home/'
    conky = '/.conky/'
    ptemp = conky + "weather/Weatherbit/forecast/"
    ptemp2 = conky + "weather/Weatherbit/"
    ptemp3 = " $HOME" + conky + "weather/Weatherbit/"
    ptemp4 = " $HOME" + conky + "weather/Weatherbit/forecast/"
    #                   set the paths for the ERROR
    perr = home + homename + ptemp + '-error.txt'
    #                   set the paths for the GENERAL section
    pgen = home + homename + ptemp + '-general.txt'
    #                   set the paths for the FORECAST section
    pforecast = home + homename + ptemp + "-forecastraw.txt"
    #                   set the paths for the FORECAST clean data section
    pforecastclean = home + homename + ptemp + "forecastclean.txt"
    #                   set the paths for the FORECAST section
    pforecastc = home + homename + ptemp + 'forecastconky.txt'
    #                   set the paths for the DEW POINT
    pdewp = home + homename + ptemp + 'forecastdewpt.txt'
    #                   set the paths for the UVI INDEX
    puvi = home + homename + ptemp + 'forecastuv.txt'
    ################################ get data for ERROR section
    responseHTTP = requests.get(url)
    # get status code
    status_code = responseHTTP.status_code
    ################################ write raw data for ERROR section
    fo = open(perr, 'w')
    fo.write('error: {}\n'.format(status_code))
    fo.close()
    ################################ set variables
    vforecast = 7 # number of days
    groupd = 45 # number of rows for 1 day
    temporary = ''
    vtext = 'n/a'
    ################################ insert angle of your North in 'myd'
    myd = 72
    tdeg = 0
    ################################ create variables for GENERAL data
    lat = 0
    lon = 0
    tz = ''
    cityname = ''
    countrycode = ''
    statecode = ''
    ################################ get data for GENERAL section
    lat = data['lat']
    lon = data['lon']
    tz = data['timezone']
    cityname = data['city_name']
    countrycode = data['country_code']
    statecode = data['state_code']
    ################################ write raw data for GENERAL section
    fo = open(pgen, 'w')
    fo.write('lat: {}\n'.format(lat))
    fo.write('lon: {}\n'.format(lon))
    fo.write('TimeZone: {}\n'.format(tz))
    fo.write('Cityname: {}\n'.format(cityname))
    fo.write('Countrycode: {}\n'.format(countrycode))
    fo.write('Statecode: {}\n'.format(statecode))
    fo.close()
    ################################ create array for FORECAST daily data
    fmoonrisets = []
    fmoonrisets2 = []
    fwindcdir = []
    frh = []
    fpres = []
    fhightemp = []
    fsunsetts = []
    fsunsetts2 = []
    fozone = []
    fmoonphase = []
    fwindgustspd = []
    fsnowdepth = []
    fclouds = []
    fts = []
    fts2 = []
    fsunrisets = []
    fsunrisets2 = []
    fappmintemp = []
    fwindspd = []
    fpop = []
    fwindcdirfull = []
    fslp = []
    fmoonlunation = []
    fvaliddate = []
    fappmaxtemp = []
    fvis = []
    fdewpt = []
    fsnow = []
    fuv = []
    fwicon = []
    fwcode = []
    fwdesc = []
    fwinddir = []
    fmaxdhi = []
    fcloudshi = []
    fprecip = []
    flowtemp = []
    fmaxtemp = []
    fmoonsetts = []
    fmoonsetts2 = []
    fdatetime = []
    ftemp = []
    fmintemp = []
    cloudsmid = []
    fcloudslow = []
    ################################ get data for FORECAST section
    for i in range(0, vforecast):
        fappmaxtemp.append(data['data'][i]['app_max_temp'])
        fappmintemp.append(data['data'][i]['app_min_temp'])
        fclouds.append(data['data'][i]['clouds'])
        fcloudshi.append(data['data'][i]['clouds_hi'])
        fcloudslow.append(data['data'][i]['clouds_low'])
        cloudsmid.append(data['data'][i]['clouds_mid'])
        fdatetime.append(data['data'][i]['datetime'])
        fdewpt.append(data['data'][i]['dewpt'])
        fhightemp.append(data['data'][i]['high_temp'])
        flowtemp.append(data['data'][i]['low_temp'])
        try:
            fmaxdhi.append(data['data'][i]['max_dhi'])
            if fmaxdhi[i] is None:
                fmaxdhi[i] = vtext
        except:
            fmaxdhi.append(vtext) 
        fmaxtemp.append(data['data'][i]['max_temp'])
        fmintemp.append(data['data'][i]['min_temp'])
        fmoonphase.append(data['data'][i]['moon_phase'])
        fmoonlunation.append(data['data'][i]['moon_phase_lunation'])
        fmoonrisets.append(data['data'][i]['moonrise_ts'])
        fmoonrisets2.append(data['data'][i]['moonrise_ts'])
        fmoonsetts.append(data['data'][i]['moonset_ts'])
        fmoonsetts2.append(data['data'][i]['moonset_ts'])
        fozone.append(data['data'][i]['ozone'])
        fpop.append(data['data'][i]['pop'])
        fprecip.append(data['data'][i]['precip'])
        fpres.append(data['data'][i]['pres'])
        frh.append(data['data'][i]['rh'])
        fslp.append(data['data'][i]['slp'])
        fsnow.append(data['data'][i]['snow'])
        fsnowdepth.append(data['data'][i]['snow_depth'])
        fsunrisets.append(data['data'][i]['sunrise_ts'])
        fsunrisets2.append(data['data'][i]['sunrise_ts'])
        fsunsetts.append(data['data'][i]['sunset_ts'])
        fsunsetts2.append(data['data'][i]['sunset_ts'])
        ftemp.append(data['data'][i]['temp'])
        fts.append(data['data'][i]['ts'])
        fts2.append(data['data'][i]['ts'])
        fuv.append(data['data'][i]['uv'])
        fvaliddate.append(data['data'][i]['valid_date'])
        fvis.append(data['data'][i]['vis'])
        fwcode.append(data['data'][i]['weather']['code'])
        fwicon.append(data['data'][i]['weather']['icon'])
        fwdesc.append(data['data'][i]['weather']['description'])
        fwindcdir.append(data['data'][i]['wind_cdir'])
        fwindcdirfull.append(data['data'][i]['wind_cdir_full'])
        fwinddir.append(data['data'][i]['wind_dir'])
        fwindgustspd.append(data['data'][i]['wind_gust_spd'])
        fwindspd.append(data['data'][i]['wind_spd'])
    ################################ write raw data for FORECAST section
    fo = open(pforecast, 'w')
    for i in range(0, vforecast):
        fo.write('moonrisetime: {}\n'.format(fmoonrisets[i]))
        fmoonrisets2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fmoonrisets2[i]))
        fo.write('moonrisetime2: {}\n'.format(fmoonrisets2[i]))
        fo.write('winddirectionabb: {}\n'.format(fwindcdir[i]))
        fo.write('humidity: {}\n'.format(frh[i]))
        fo.write('pressure: {}\n'.format(fpres[i]))
        fo.write('hightemp: {}\n'.format(fhightemp[i]))
        fo.write('sunsettime: {}\n'.format(fsunsetts[i]))
        fsunsetts2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fsunsetts2[i]))
        fo.write('sunsettime2: {}\n'.format(fsunsetts2[i]))
        fo.write('ozone: {}\n'.format(fozone[i]))
        fo.write('moonphaseillumi: {}\n'.format(fmoonphase[i]))
        #                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
        fwindgustspd[i] = float(round(fwindgustspd[i] * 3.6, 2))
        fo.write('windgustspd: {}\n'.format(fwindgustspd[i]))
        fo.write('snowdepth: {}\n'.format(fsnowdepth[i]))
        fo.write('clouds: {}\n'.format(fclouds[i]))
        fo.write('forecaststart: {}\n'.format(fts[i]))
        fts2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fts2[i]))
        fo.write('forecaststart2: {}\n'.format(fts2[i]))
        fo.write('sunrisetime: {}\n'.format(fsunrisets[i]))
        fsunrisets2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fsunrisets2[i]))
        fo.write('sunrisetime2: {}\n'.format(fsunrisets2[i]))
        fo.write('tempfeelsmin: {}\n'.format(fappmintemp[i]))
        #                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
        fwindspd[i] = float(round(fwindspd[i] * 3.6, 2))
        fo.write('windspd: {}\n'.format(fwindspd[i]))
        fo.write('pop: {}\n'.format(fpop[i]))
        fo.write('winddirectionalfull: {}\n'.format(fwindcdirfull[i]))
        fo.write('sealevelpressure: {}\n'.format(fslp[i]))
        fo.write('moonlunation: {}\n'.format(fmoonlunation[i]))
        fo.write('forecastvalidity: {}\n'.format(fvaliddate[i]))
        fo.write('tempfeelsmax: {}\n'.format(fappmaxtemp[i]))
        fo.write('visibility: {}\n'.format(fvis[i]))
        fo.write('dewpoint: {}\n'.format(fdewpt[i]))
        fo.write('snow: {}\n'.format(fsnow[i]))
        fo.write('uvindex: {}\n'.format(fuv[i]))
        fo.write('weathericon: {}\n'.format(fwicon[i]))
        fo.write('weathercode: {}\n'.format(fwcode[i]))
        fo.write('weatherdesc: {}\n'.format(fwdesc[i]))
        fo.write('windirection: {}\n'.format(fwinddir[i]))
        fo.write('maxDHI: {}\n'.format(fmaxdhi[i]))
        fo.write('cloudshigh: {}\n'.format(fcloudshi[i]))
        # round the decimal for precipitation
        fprecip[i] = str(round(fprecip[i], 2))
        fo.write('precipitation: {}\n'.format(fprecip[i]))
        fo.write('lowtemp: {}\n'.format(flowtemp[i]))
        fo.write('tempmax: {}\n'.format(fmaxtemp[i]))
        fo.write('moonsettime: {}\n'.format(fmoonsetts[i]))
        fmoonsetts2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fmoonsetts2[i]))
        fo.write('moonsettime2: {}\n'.format(fmoonsetts2[i]))
        fo.write('forecastvaliddate: {}\n'.format(fdatetime[i]))
        fo.write('temp: {}\n'.format(ftemp[i]))
        fo.write('tempmin: {}\n'.format(fmintemp[i]))
        fo.write('cloudsmid: {}\n'.format(cloudsmid[i]))
        fo.write('cloudslow: {}\n'.format(fcloudslow[i]))
    fo.close()
    ################################ write clean data for FORECAST section
    fo = open(pforecastclean, 'w')
    for i in range(0, vforecast):
        fo.write('{}\n'.format(fmoonrisets[i]))
        fo.write('{}\n'.format(fmoonrisets2[i]))
        fo.write('{}\n'.format(fwindcdir[i]))
        fo.write('{}\n'.format(frh[i]))
        fo.write('{}\n'.format(fpres[i]))
        fo.write('{}\n'.format(fhightemp[i]))
        fo.write('{}\n'.format(fsunsetts[i]))
        fo.write('{}\n'.format(fsunsetts2[i]))
        fo.write('{}\n'.format(fozone[i]))
        fo.write('{}\n'.format(fmoonphase[i]))
        fo.write('{}\n'.format(fwindgustspd[i]))
        fo.write('{}\n'.format(fsnowdepth[i]))
        fo.write('{}\n'.format(fclouds[i]))
        fo.write('{}\n'.format(fts[i]))
        fo.write('{}\n'.format(fts2[i]))
        fo.write('{}\n'.format(fsunrisets[i]))
        fo.write('{}\n'.format(fsunrisets2[i]))
        fo.write('{}\n'.format(fappmintemp[i]))
        fo.write('{}\n'.format(fwindspd[i]))
        fo.write('{}\n'.format(fpop[i]))
        fo.write('{}\n'.format(fwindcdirfull[i]))
        fo.write('{}\n'.format(fslp[i]))
        fo.write('{}\n'.format(fmoonlunation[i]))
        fo.write('{}\n'.format(fvaliddate[i]))
        fo.write('{}\n'.format(fappmaxtemp[i]))
        fo.write('{}\n'.format(fvis[i]))
        fo.write('{}\n'.format(fdewpt[i]))
        fo.write('{}\n'.format(fsnow[i]))
        fo.write('{}\n'.format(fuv[i]))
        fo.write('{}\n'.format(fwicon[i]))
        fo.write('{}\n'.format(fwcode[i]))
        fo.write('{}\n'.format(fwdesc[i]))
        fo.write('{}\n'.format(fwinddir[i]))
        fo.write('{}\n'.format(fmaxdhi[i]))
        fo.write('{}\n'.format(fcloudshi[i]))
        fo.write('{}\n'.format(fprecip[i]))
        fo.write('{}\n'.format(flowtemp[i]))
        fo.write('{}\n'.format(fmaxtemp[i]))
        fo.write('{}\n'.format(fmoonsetts[i]))
        fo.write('{}\n'.format(fmoonsetts2[i]))
        fo.write('{}\n'.format(fdatetime[i]))
        fo.write('{}\n'.format(ftemp[i]))
        fo.write('{}\n'.format(fmintemp[i]))
        fo.write('{}\n'.format(cloudsmid[i]))
        fo.write('{}\n'.format(fcloudslow[i]))
    fo.close()
    ################################ calculate FORECAST dew point color and write it
    color = 'white'
    #      calculate the DEW POINT color font based on index
    fo = open(pdewp, 'w')
    for i in range(0, vforecast):
        value = fdewpt[i]
        if (value < 19):
            color = 6
        elif (value >=19 and value < 22):
            color = 9
        elif (value >=22):
            color = 4
        else:
            color = 'white'
        fo.write('{}\n'.format(value))
        fo.write('{}\n'.format(color))
    fo.close()
    ################################ calculate FORECAST UV index color and write it
    fo = open(puvi, 'w')
    for i in range(0, vforecast):
        value = fuv[i]
        if (value >=0 and value < 3):
            color = 6
        elif (value >=3 and value < 6):
            color = 9
        elif (value >=6 and value < 8):
            color = 3
        elif (value >=8 and value < 11):
            color = 4
        elif (value >= 11):
            color = 0
        else:
            color = 2
        fo.write('{}\n'.format(value))
        fo.write('{}\n'.format(color))
    fo.close()
    ################################ create FORECAST section
    #                 general variables
    firstd = 1
    blokd = 1
    #                 general settings
    rowgoto = '${goto '
    gotonumh = 100
    gotonumd = 100
    gotoplus = 20
    rowgraph = '}'
    rowcolor = '${color}'
    rowcolor1 = '${color1}'
    rowcolor2 = '${color2}'
    rowcolor3 = '${color3}'
    rowcolor4 = '${color4}'
    rowcolor5 = '${color5}'
    rowcolor6 = '${color6}'
    rowcolor9 = '${color9}'
    rowinfo = "${execpi 900 sed -n '"
    rowp = "p'"
    #rowpathh = ptemp4 + '-hourly.txt'
    rowpathd = ptemp4 + 'forecastclean.txt'
    rowprint2 = " | awk '{print $2}'"
    rowprint3 = " | awk '{print $3}'"
    rowbar = '/'
    rowfont6 = '${font URW Gothic L:size=6}'
    rowfont7 = '${font URW Gothic L:size=7}'
    rowfont8 = '${font URW Gothic L:size=8}'
    rowalignr = '${alignr}'
    rowalignc = '${alignc}'
    rowalignl = '${alignl}'
    rowvoffset = '${voffset 15}'
    #                 time settings
    gotohourh = 50
    gotohourd = 35
    rowhour = "h${execpi 900 sed -n '"
    rowcut = ' | cut -c1-5'
    #                 icons settings
    pi = '${image /home/'
    pi2 = homename
    pi3 = ptemp2 + 'icons/'
    est = '.png -p '
    y = 0
    virg = ','
    zh = 325
    zd = 0
    size = 100 # icons size
    pfh = ' -s ' + str(size) + 'x' + str(size) + '}'
    pfd = ' -s ' + str(size) + 'x' + str(size) + '}'
    #                 sunrise, sunset, moonrise, moonset
    rowsunrised = "Sr ${execpi 900 sed -n '"
    rowsunsetd = "Ss ${execpi 900 sed -n '"
    rowmoonrised = "Mr ${execpi 900 sed -n '"
    rowmoonsetd = "Ms ${execpi 900 sed -n '"
    #                 moon phase settings
    rowmoonphillud = "MoonLum ${execpi 900 sed -n '"
    rowmoonlund = "MoonLun ${execpi 900 sed -n '"
    #                 wind settings
    rowwindsd= "Ws ${execpi 900 sed -n '"
    rowwindsd2= "Wg ${execpi 900 sed -n '"
    rowwindsd4= "Wdir ${execpi 900 sed -n '"
    rowwindsd4b= "Wdir ${execpi 900 sed -n '"
    rowwindsd5 = 'm/s'
    rowwindsd6 = 'Km/h'
    #                 wind gust settings
    rowwindgd= "Wg ${execpi 900 sed -n '"
    #                 humidity settings
    rowhumd = "H ${execpi 900 sed -n '"
    rowhumd2 = '%'
    #                 pressure settings
    rowpresd = "P ${execpi 900 sed -n '"
    rowpresd2 = 'hPa'
    rowpresd3 = 'mb'
    #                 temperature, feellike settings
    rowtempd = "${execpi 900 sed -n '"
    rowtemphid = "Thi ${execpi 900 sed -n '"
    rowtemplowd = "Tlow ${execpi 900 sed -n '"
    rowtempmind = "min ${execpi 900 sed -n '"
    rowtempmaxd = "max ${execpi 900 sed -n '"
    rowtempfmaxd = "fmax ${execpi 900 sed -n '"
    rowtempfmind = "fmin ${execpi 900 sed -n '"
    rowtempfd = "Tf ${execpi 900 sed -n '"
    rowtempdd = "Td ${execpi 900 sed -n '"
    rowtempnd = "Tn ${execpi 900 sed -n '"
    rowtemped = "Te ${execpi 900 sed -n '"
    rowtempmd = "Tm ${execpi 900 sed -n '"
    rowtempdfd = "Tdf ${execpi 900 sed -n '"
    rowtempnfd = "Tnf ${execpi 900 sed -n '"
    rowtempefd = "Tef ${execpi 900 sed -n '"
    rowtempmfd = "Tmf ${execpi 900 sed -n '"
    rowtempd2 = '°C'
    rowtempd3 = '°'
    #                 ozone settings
    rowozoned = "Oz ${execpi 900 sed -n '"
    rowozoned2 = 'Du'
    #                 maxDHI settings
    rowmaxdhi = "DHImax ${execpi 900 sed -n '"
    rowmaxdhi2 = 'W/m^2'
    #                 dew point settings
    rowdew = "Dp ${eval $${color${execpi 900 sed -n '"
    rowdewpathcolor1f = ptemp4 + "forecastdewpt.txt}}}"
    rowdewpathcolor1h = ptemp4 + "hourlyowmdewpoint.txt}}}"
    rowdewpathcolor1d = ptemp4 + "dailyowmdewpoint.txt}}}"
    #rowdewpathcolor2h = "${execpi 900 sed -n '"
    rowdewpathvalue1f = ptemp4 + "forecastdewpt.txt}"
    rowdewpathvalue1h = ptemp4 + "hourlyowmdewpoint.txt}"
    rowdewpathvalue1d = ptemp4 + "dailyowmdewpoint.txt}"
    #rowdewpathvalue2h = '${color}'
    #                 uvi settings
    rowuvi = "UV ${eval $${color${execpi 900 sed -n '"
    rowuvipathcolor1f = ptemp4 + "forecastuv.txt}}}"
    rowuvipathcolor1h = ptemp4 + "hourlyowmuvindex.txt}}}"
    rowuvipathcolor1d = ptemp4 + "dailyowmuvindex.txt}}}"
    #rowuvipathcolor2h = "${execpi 900 sed -n '"
    rowuvipathvalue1f = ptemp4 + "forecastuv.txt}"
    rowuvipathvalue1h = ptemp4 + "hourlyowmuvindex.txt}"
    rowuvipathvalue1d = ptemp4 + "dailyowmuvindex.txt}"
    #rowuvipathvalue2h = '${color}'
    #                 cloudness settings
    rowclo= "Cl ${execpi 900 sed -n '"
    rowclolow= "Cllow ${execpi 900 sed -n '"
    rowclomid= "Clmid ${execpi 900 sed -n '"
    rowclohi= "Clhi ${execpi 900 sed -n '"
    rowclo2 = '%'
    #                 visibility settings
    rowvis= "Vis ${execpi 900 sed -n '"
    rowvis2 = 'm'
    rowvis3 = 'Km'
    
    #                 pop settings
    rowpop= "Pop ${execpi 900 sed -n '"
    #                 rain1h settings
    rowrain1= "R1 ${execpi 900 sed -n '"
    rowrain1a= "Prec ${execpi 900 sed -n '"
    rowrain2 = 'mm'
    #                 snow1h settings
    rowsnowd= "Snow ${execpi 900 sed -n '"
    rowsnowdepthd = "Sdepth:${execpi 900 sed -n '"
    rowsnow2 = 'mm'
    #                 forecast settings
    rowforecast= "${execpi 900 sed -n '"
    rowforecastval= "${execpi 900 sed -n '"
    #                 main DAILY
    y = 0
    counter = 0
    fo = open(pforecastc, 'w')
    for i in range(firstd, vforecast):
        if (fwicon[i][3:4]) == 'd':
            i2 = 1 + (groupd * i)
            # row n. 1 and multiples not present
            vtemp = i2 + 1
            if i == 1:
                totrowmrd = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowmoonrised + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
                fo.write('{}\n'.format(totrowmrd))
                vtemp = vtemp + 1
            elif i != 1:
                totrowmrd = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowmoonrised + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
                fo.write('{}\n'.format(totrowmrd))
                vtemp = vtemp + 1
            totrowwinddirabbd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowwindsd4 + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowwinddirabbd))
            vtemp = vtemp + 1
            totrowhumd = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowhumd + str(vtemp) + rowp + rowpathd + rowgraph + rowhumd2
            fo.write('{}\n'.format(totrowhumd))        
            vtemp = vtemp + 1
            totrowpresd = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowpresd + str(vtemp) + rowp + rowpathd + rowgraph + rowpresd3
            fo.write('{}\n'.format(totrowpresd))
            vtemp = vtemp + 1
            totrowtemphid = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowtemphid + str(vtemp) + rowp + rowpathd +  rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowtemphid))
            vtemp = vtemp + 2
            # row n. 7 and multiples not present
            totrowssd = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowsunsetd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
            fo.write('{}\n'.format(totrowssd))
            vtemp = vtemp + 1
            totrowozoned = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowozoned + str(vtemp) + rowp + rowpathd + rowgraph + rowozoned2
            fo.write('{}\n'.format(totrowozoned))
            vtemp = vtemp + 1
            totrowmoonphillud = rowgoto + str(gotonumd * 7 + gotoplus) + rowgraph + rowmoonphillud + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowmoonphillud))
            vtemp = vtemp + 1
            totrowwindgd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowwindgd + str(vtemp) + rowp + rowpathd + rowgraph + rowwindsd6
            fo.write('{}\n'.format(totrowwindgd))
            vtemp = vtemp + 1
            totrowsnowdepthd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowsnowdepthd + str(vtemp) + rowp + rowpathd + rowgraph + rowsnow2
            fo.write('{}\n'.format(totrowsnowdepthd))
            vtemp = vtemp + 1
            totrowclod = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowclo + str(vtemp) + rowp + rowpathd + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowclod))
            vtemp = vtemp + 2
            # row n. 14 and multiples not present
            totrowforecast = rowforecast + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowforecast))
            vtemp = vtemp + 2
            # row n. 16 and multiples not present
            totrowsunrised = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowsunrised + str(vtemp) + rowp + rowpathd + rowprint2 +  rowgraph
            fo.write('{}\n'.format(totrowsunrised))
            vtemp = vtemp + 1
            totrowtempfmind = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor1 + rowtempfmind + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempfmind))
            vtemp = vtemp + 1
            totrowwinsd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowwindsd + str(vtemp) + rowp + rowpathd + rowgraph + rowwindsd6
            fo.write('{}\n'.format(totrowwinsd))
            vtemp = vtemp + 1
            totrowpopd = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowpop + str(vtemp) + rowp + rowpathd + rowgraph + rowhumd2
            fo.write('{}\n'.format(totrowpopd))        
            vtemp = vtemp + 1
            totrowwindsd4b = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowwindsd4b + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowwindsd4b))        
            vtemp = vtemp + 1
            totrowpresd = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowpresd + str(vtemp) + rowp + rowpathd + rowgraph + rowpresd3
            fo.write('{}\n'.format(totrowpresd))
            vtemp = vtemp + 1
            totrowmoonlund = rowgoto + str(gotonumd * 7 + gotoplus) + rowgraph + rowmoonlund + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowmoonlund))
            vtemp = vtemp + 1
            totrowforecast = rowforecast + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowforecast))
            vtemp = vtemp + 1
            totrowtempfmaxd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor4 + rowtempfmaxd + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempfmaxd))
            vtemp = vtemp + 1
            totrowvis = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowvis + str(vtemp) + rowp + rowpathd + rowgraph + rowvis3
            fo.write('{}\n'.format(totrowvis))
            vtemp = vtemp + 1
            vtemp1 = 1 + (i * 2)
            vtemp2 = 2 + (i * 2)
            totrowdewd = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1f + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1f + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowdewd))
            vtemp = vtemp + 1        
            totrowsnowd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowsnowd + str(vtemp) + rowp + rowpathd + rowgraph + rowsnow2
            fo.write('{}\n'.format(totrowsnowd))
            vtemp = vtemp + 1
            vtemp1 = 1 + (i * 2)
            vtemp2 = 2 + (i * 2)
            totrowuvid = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowuvi + str(vtemp2) + rowp + rowuvipathcolor1f + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1f + rowcolor
            fo.write('{}\n'.format(totrowuvid))
            vtemp = vtemp + 3
            #           rows 30 and 31 are used to create the weather icons path
            totico = pi + pi2 + pi3 + str(fwicon[i]) + est + str(y) + virg + str(zd) + pfd
            fo.write('{}\n'.format(totico))        
            totrowinfo = rowgoto + str(gotonumd * 1 + gotoplus) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowinfo))        
            vtemp = vtemp + 2
            # row n. 33 and multiples not present
            totrowmaxdhi = rowgoto + str(gotonumd * 7 + gotoplus) + rowgraph + rowmaxdhi + str(vtemp) + rowp + rowpathd + rowgraph + rowmaxdhi2
            fo.write('{}\n'.format(totrowmaxdhi))
            vtemp = vtemp + 1
            totrowclohi = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowclohi + str(vtemp) + rowp + rowpathd + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowclohi))
            vtemp = vtemp + 1
            totrowrain1a = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowrain1a + str(vtemp) + rowp + rowpathd + rowgraph + rowrain2
            fo.write('{}\n'.format(totrowrain1a))        
            vtemp = vtemp + 1
            totrowtemplowd = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowtemplowd + str(vtemp) + rowp + rowpathd + rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowtemplowd))
            vtemp = vtemp + 1
            totrowtempmaxd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor4 + rowtempmaxd + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempmaxd))
            vtemp = vtemp + 2
            # row n. 39 and multiples not present
            totrowmoonsetd = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowmoonsetd + str(vtemp) + rowp + rowpathd + rowprint2 +  rowgraph
            fo.write('{}\n'.format(totrowmoonsetd))
            vtemp = vtemp + 1
            totrowforecastval = rowalignc + rowforecastval + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowforecastval))
            vtemp = vtemp + 1
            totrowtempd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowtempd + str(vtemp) + rowp + rowpathd + rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowtempd))
            vtemp = vtemp + 1
            totrowtempmind = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor1 + rowtempmind + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempmind))
            vtemp = vtemp + 1
            totrowclomid = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowclomid + str(vtemp) + rowp + rowpathd + rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowclomid))
            vtemp = vtemp + 1
            totrowclolow = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowclolow + str(vtemp) + rowp + rowpathd + rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowclolow))
            if i == 4 or i == 8 or i == 12 or i == 16:
                zd = 0
            else:
                zd = zd + 115        
        elif (fwicon[i][3:4]) == 'n':
            i2 = 1 + (groupd * i)
            # row n. 1 and multiples not present
            vtemp = i2 + 1
            if i == 1:
                totrowmrd = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowmoonrised + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
                fo.write('{}\n'.format(totrowmrd))
                vtemp = vtemp + 1
            elif i != 1:
                totrowmrd = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowmoonrised + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
                fo.write('{}\n'.format(totrowmrd))
                vtemp = vtemp + 1
            totrowwinddirabbd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowwindsd4 + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowwinddirabbd))
            vtemp = vtemp + 1
            totrowhumd = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowhumd + str(vtemp) + rowp + rowpathd + rowgraph + rowhumd2
            fo.write('{}\n'.format(totrowhumd))        
            vtemp = vtemp + 1
            totrowpresd = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowpresd + str(vtemp) + rowp + rowpathd + rowgraph + rowpresd3
            fo.write('{}\n'.format(totrowpresd))
            vtemp = vtemp + 1
            totrowtemphid = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowtemphid + str(vtemp) + rowp + rowpathd +  rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowtemphid))
            vtemp = vtemp + 2
            # row n. 7 and multiples not present
            totrowssd = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowsunsetd + str(vtemp) + rowp + rowpathd + rowprint2 + rowgraph
            fo.write('{}\n'.format(totrowssd))
            vtemp = vtemp + 1
            totrowozoned = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowozoned + str(vtemp) + rowp + rowpathd + rowgraph + rowozoned2
            fo.write('{}\n'.format(totrowozoned))
            vtemp = vtemp + 1
            totrowmoonphillud = rowgoto + str(gotonumd * 7 + gotoplus) + rowgraph + rowmoonphillud + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowmoonphillud))
            vtemp = vtemp + 1
            totrowwindgd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowwindgd + str(vtemp) + rowp + rowpathd + rowgraph + rowwindsd6
            fo.write('{}\n'.format(totrowwindgd))
            vtemp = vtemp + 1
            totrowsnowdepthd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowsnowdepthd + str(vtemp) + rowp + rowpathd + rowgraph + rowsnow2
            fo.write('{}\n'.format(totrowsnowdepthd))
            vtemp = vtemp + 1
            totrowclod = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowclo + str(vtemp) + rowp + rowpathd + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowclod))
            vtemp = vtemp + 2
            # row n. 14 and multiples not present
            totrowforecast = rowforecast + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowforecast))
            vtemp = vtemp + 2
            # row n. 16 and multiples not present
            totrowsunrised = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowsunrised + str(vtemp) + rowp + rowpathd + rowprint2 +  rowgraph
            fo.write('{}\n'.format(totrowsunrised))
            vtemp = vtemp + 1
            totrowtempfmind = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor1 + rowtempfmind + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempfmind))
            vtemp = vtemp + 1
            totrowwinsd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowwindsd + str(vtemp) + rowp + rowpathd + rowgraph + rowwindsd6
            fo.write('{}\n'.format(totrowwinsd))
            vtemp = vtemp + 1
            totrowpopd = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowpop + str(vtemp) + rowp + rowpathd + rowgraph + rowhumd2
            fo.write('{}\n'.format(totrowpopd))        
            vtemp = vtemp + 1
            totrowwindsd4b = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowwindsd4b + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowwindsd4b))        
            vtemp = vtemp + 1
            totrowpresd = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowpresd + str(vtemp) + rowp + rowpathd + rowgraph + rowpresd3
            fo.write('{}\n'.format(totrowpresd))
            vtemp = vtemp + 1
            totrowmoonlund = rowgoto + str(gotonumd * 7 + gotoplus) + rowgraph + rowmoonlund + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowmoonlund))
            vtemp = vtemp + 1
            totrowforecast = rowforecast + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowforecast))
            vtemp = vtemp + 1
            totrowtempfmaxd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor4 + rowtempfmaxd + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempfmaxd))
            vtemp = vtemp + 1
            totrowvis = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowvis + str(vtemp) + rowp + rowpathd + rowgraph + rowvis3
            fo.write('{}\n'.format(totrowvis))
            vtemp = vtemp + 1
            vtemp1 = 1 + (i * 2)
            vtemp2 = 2 + (i * 2)
            totrowdewd = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1f + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1f + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowdewd))
            vtemp = vtemp + 1        
            totrowsnowd = rowgoto + str(gotonumd * 5 + gotoplus) + rowgraph + rowsnowd + str(vtemp) + rowp + rowpathd + rowgraph + rowsnow2
            fo.write('{}\n'.format(totrowsnowd))
            vtemp = vtemp + 1
            vtemp1 = 1 + (i * 2)
            vtemp2 = 2 + (i * 2)
            totrowuvid = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowuvi + str(vtemp2) + rowp + rowuvipathcolor1f + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1f + rowcolor
            fo.write('{}\n'.format(totrowuvid))
            vtemp = vtemp + 3
            #           rows 30 and 31 are used to create the weather icons path
            totico = pi + pi2 + pi3 + str(fwicon[i]) + est + str(y) + virg + str(zd) + pfd
            fo.write('{}\n'.format(totico))        
            totrowinfo = rowgoto + str(gotonumd * 1 + gotoplus) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowinfo))        
            vtemp = vtemp + 2
            # row n. 33 and multiples not present
            totrowmaxdhi = rowgoto + str(gotonumd * 7 + gotoplus) + rowgraph + rowmaxdhi + str(vtemp) + rowp + rowpathd + rowgraph + rowmaxdhi2
            fo.write('{}\n'.format(totrowmaxdhi))
            vtemp = vtemp + 1
            totrowclohi = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowclohi + str(vtemp) + rowp + rowpathd + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowclohi))
            vtemp = vtemp + 1
            totrowrain1a = rowgoto + str(gotonumd * 3 + gotoplus) + rowgraph + rowrain1a + str(vtemp) + rowp + rowpathd + rowgraph + rowrain2
            fo.write('{}\n'.format(totrowrain1a))        
            vtemp = vtemp + 1
            totrowtemplowd = rowgoto + str(gotonumd * 2 + gotoplus) + rowgraph + rowtemplowd + str(vtemp) + rowp + rowpathd + rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowtemplowd))
            vtemp = vtemp + 1
            totrowtempmaxd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor4 + rowtempmaxd + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempmaxd))
            vtemp = vtemp + 2
            # row n. 39 and multiples not present
            totrowmoonsetd = rowgoto + str(gotonumd * 6 + gotoplus) + rowgraph + rowmoonsetd + str(vtemp) + rowp + rowpathd + rowprint2 +  rowgraph
            fo.write('{}\n'.format(totrowmoonsetd))
            vtemp = vtemp + 1
            totrowforecastval = rowalignc + rowforecastval + str(vtemp) + rowp + rowpathd + rowgraph
            fo.write('{}\n'.format(totrowforecastval))
            vtemp = vtemp + 1
            totrowtempd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowtempd + str(vtemp) + rowp + rowpathd + rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowtempd))
            vtemp = vtemp + 1
            totrowtempmind = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor1 + rowtempmind + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempmind))
            vtemp = vtemp + 1
            totrowclomid = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowclomid + str(vtemp) + rowp + rowpathd + rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowclomid))
            vtemp = vtemp + 1
            totrowclolow = rowgoto + str(gotonumd * 4 + gotoplus) + rowgraph + rowclolow + str(vtemp) + rowp + rowpathd + rowgraph + rowtempd2
            fo.write('{}\n'.format(totrowclolow))
            if i == 4 or i == 8 or i == 12 or i == 16:
                zd = 0
            else:
                zd = zd + 115
    fo.close()
    ################################ create CONKY statements to copy into the conkyrc file
    vnblock = 38
    vconst = 0
    pconkycopy = home + homename + ptemp + 'conkycopy.txt'
    if status_code == 200:
        fo = open(pconkycopy, 'w')
        for i in range(0, 16):
            v0 = "########################################### show " + str((i + 1)) + "° day"
            fo.write('{}\n'.format(v0))
            v1 = "${execpi 900 sed -n '" + str(27 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(34 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}"
            fo.write('{}\n'.format(v1))
            v2 = "${execpi 900 sed -n '" + str(26 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}"
            fo.write('{}\n'.format(v2))
            v3 = "${execpi 900 sed -n '" + str(35 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(5 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(25 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(22 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(15 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(13 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(28 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}"
            fo.write('{}\n'.format(v3))
            v4 = "${execpi 900 sed -n '" + str(32 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(31 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(23 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(11 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(9 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(6 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}"
            fo.write('{}\n'.format(v4))
            v5 = "${execpi 900 sed -n '" + str(36 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(3 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(7 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(38 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(2 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(1 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(8 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}"
            fo.write('{}\n'.format(v5))
            v6 = "${execpi 900 sed -n '" + str(21 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(4 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(30 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(37 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(24 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(33 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(19 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}"
            fo.write('{}\n'.format(v6))
            v7 = "${execpi 900 sed -n '" + str(14 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(18 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(16 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(29 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}${execpi 900 sed -n '" + str(10 + vconst) + "p' $HOME" + conky + "weather/Weatherbit/forecast/forecastconky.txt}"
            fo.write('{}\n'.format(v7))
            v8 = "${alignc}--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            fo.write('{}\n'.format(v8))
            vconst = vconst + vnblock
        fo.close()
    else:
        fo = open(pconkycopy, 'w')
        for i in range(0, 16):
            v0 = "HTTP STATUS CODE ERROR: " + status_code
            fo.write('{}\n'.format(v0))
            v1 = "HTTP STATUS CODE ERROR: " + status_code
            fo.write('{}\n'.format(v1))
            v2 = "HTTP STATUS CODE ERROR: " + status_code
            fo.write('{}\n'.format(v2))
            v3 = "HTTP STATUS CODE ERROR: " + status_code
            fo.write('{}\n'.format(v3))
            v4 = "HTTP STATUS CODE ERROR: " + status_code
            fo.write('{}\n'.format(v4))
            v5 = "HTTP STATUS CODE ERROR: " + status_code
            fo.write('{}\n'.format(v5))
            v6 = "HTTP STATUS CODE ERROR: " + status_code
            fo.write('{}\n'.format(v6))
            v7 = "HTTP STATUS CODE ERROR: " + status_code
            fo.write('{}\n'.format(v7))
            v8 = "${alignc}--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
            fo.write('{}\n'.format(v8))
            vconst = vconst + vnblock
        fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed